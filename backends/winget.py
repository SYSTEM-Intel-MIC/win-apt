"""Windows Package Manager (winget) backend"""
import subprocess
import shutil
import json
import re
from typing import List, Optional
from backends.base import PackageBackend
from core.package import Package

class WingetBackend(PackageBackend):
    name = "winget"

    def _check_available(self):
        self.available = shutil.which("winget") is not None

    def _run(self, args: List[str], capture=True, check=True) -> subprocess.CompletedProcess:
        cmd = ["winget"] + args
        if capture:
            return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore", check=check)
        return subprocess.run(cmd, check=check)

    def update(self) -> bool:
        try:
            result = self._run(["source", "update"], capture=False, check=True)
            return result.returncode == 0
        except Exception as e:
            print(f"winget update failed: {e}")
            return False

    def install(self, packages: List[str], **kwargs) -> bool:
        args = ["install"]
        if kwargs.get("yes"):
            args.append("--accept-source-agreements")
            args.append("--accept-package-agreements")
        if kwargs.get("simulate"):
            print(f"[SIMULATE] Would install via winget: {packages}")
            return True

        for pkg in packages:
            try:
                cmd = args + [pkg]
                result = self._run(cmd, capture=False, check=False)
                if result.returncode != 0:
                    return False
            except Exception as e:
                print(f"Failed to install {pkg} via winget: {e}")
                return False
        return True

    def remove(self, packages: List[str], purge: bool = False, **kwargs) -> bool:
        args = ["uninstall"]
        if kwargs.get("yes"):
            args.append("--accept-source-agreements")
        if kwargs.get("simulate"):
            print(f"[SIMULATE] Would remove via winget: {packages}")
            return True

        for pkg in packages:
            try:
                cmd = args + [pkg]
                result = self._run(cmd, capture=False, check=False)
                if result.returncode != 0:
                    return False
            except Exception as e:
                print(f"Failed to remove {pkg} via winget: {e}")
                return False
        return True

    def upgrade(self, packages: Optional[List[str]] = None, **kwargs) -> bool:
        args = ["upgrade"]
        if kwargs.get("yes"):
            args.append("--accept-source-agreements")
            args.append("--accept-package-agreements")
        if kwargs.get("simulate"):
            print(f"[SIMULATE] Would upgrade via winget: {packages or 'all'}")
            return True

        if packages:
            for pkg in packages:
                try:
                    cmd = args + [pkg]
                    result = self._run(cmd, capture=False, check=False)
                    if result.returncode != 0:
                        return False
                except Exception as e:
                    print(f"Failed to upgrade {pkg} via winget: {e}")
                    return False
        else:
            # Upgrade all
            try:
                args.append("--all")
                result = self._run(args, capture=False, check=False)
                return result.returncode == 0
            except Exception as e:
                print(f"Failed to upgrade all via winget: {e}")
                return False
        return True

    def search(self, keyword: str, **kwargs) -> List[Package]:
        packages = []
        try:
            result = self._run(["search", keyword], capture=True, check=False)
            if result.returncode != 0:
                return packages

            lines = result.stdout.strip().split("\n")
            # Skip header lines
            data_started = False
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line.startswith("Name") and "Id" in line:
                    data_started = True
                    continue
                if data_started:
                    # Parse: Name    Id    Version    Match    Source
                    parts = [p.strip() for p in line.split("  ") if p.strip()]
                    if len(parts) >= 2:
                        pkg = Package(
                            name=parts[0],
                            version=parts[2] if len(parts) > 2 else "unknown",
                            source="winget",
                            description="",
                            publisher=""
                        )
                        packages.append(pkg)
        except Exception as e:
            print(f"winget search failed: {e}")
        return packages

    def show(self, package: str, **kwargs) -> Optional[Package]:
        try:
            result = self._run(["show", package], capture=True, check=False)
            if result.returncode != 0:
                return None

            info = {"name": package, "version": "unknown", "description": "", "publisher": ""}
            for line in result.stdout.split("\n"):
                line = line.strip()
                if line.startswith("Found"):
                    continue
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip().lower()
                    value = value.strip()
                    if key in ["package name", "name"]:
                        info["name"] = value
                    elif key == "version":
                        info["version"] = value
                    elif key in ["description", "short description"]:
                        info["description"] = value
                    elif key in ["publisher", "author"]:
                        info["publisher"] = value
                    elif key == "homepage":
                        info["homepage"] = value
                    elif key == "license":
                        info["license"] = value

            return Package(
                name=info["name"],
                version=info["version"],
                source="winget",
                description=info["description"],
                publisher=info["publisher"],
                homepage=info.get("homepage"),
                license=info.get("license")
            )
        except Exception as e:
            print(f"winget show failed: {e}")
            return None

    def list_installed(self, pattern: Optional[str] = None, **kwargs) -> List[Package]:
        packages = []
        try:
            args = ["list"]
            if pattern:
                args.append(pattern)
            result = self._run(args, capture=True, check=False)
            if result.returncode != 0:
                return packages

            lines = result.stdout.strip().split("\n")
            data_started = False
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line.startswith("Name") and "Id" in line:
                    data_started = True
                    continue
                if data_started:
                    parts = [p.strip() for p in line.split("  ") if p.strip()]
                    if len(parts) >= 2:
                        version = parts[2] if len(parts) > 2 else "unknown"
                        available = parts[3] if len(parts) > 3 else None
                        pkg = Package(
                            name=parts[0],
                            version=version,
                            source="winget",
                            description="",
                            publisher="",
                            installed=True,
                            upgradable=available is not None and available != version and available != "",
                            latest_version=available if available != version else None
                        )
                        packages.append(pkg)
        except Exception as e:
            print(f"winget list failed: {e}")
        return packages

    def list_upgradable(self, **kwargs) -> List[Package]:
        packages = []
        try:
            result = self._run(["upgrade"], capture=True, check=False)
            if result.returncode != 0:
                return packages

            lines = result.stdout.strip().split("\n")
            data_started = False
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line.startswith("Name") and "Id" in line:
                    data_started = True
                    continue
                if data_started:
                    parts = [p.strip() for p in line.split("  ") if p.strip()]
                    if len(parts) >= 3:
                        pkg = Package(
                            name=parts[0],
                            version=parts[2] if len(parts) > 2 else "unknown",
                            source="winget",
                            description="",
                            publisher="",
                            installed=True,
                            upgradable=True,
                            latest_version=parts[3] if len(parts) > 3 else None
                        )
                        packages.append(pkg)
        except Exception as e:
            print(f"winget upgrade list failed: {e}")
        return packages

    def autoremove(self, purge: bool = False, **kwargs) -> bool:
        print("winget does not support autoremove. Skipping.")
        return True

    def download(self, package: str, **kwargs) -> bool:
        print("winget download not fully supported in this version.")
        return False
