"""Chocolatey backend"""
import subprocess
import shutil
import re
from typing import List, Optional
from backends.base import PackageBackend
from core.package import Package

class ChocoBackend(PackageBackend):
    name = "choco"

    def _check_available(self):
        self.available = shutil.which("choco") is not None

    def _run(self, args: List[str], capture=True, check=True) -> subprocess.CompletedProcess:
        cmd = ["choco"] + args
        if capture:
            return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore", check=check)
        return subprocess.run(cmd, check=check)

    def update(self) -> bool:
        try:
            # choco doesn't have a direct update command for sources
            # We can use outdated to refresh
            result = self._run(["outdated"], capture=True, check=False)
            return True
        except Exception as e:
            print(f"choco update failed: {e}")
            return False

    def install(self, packages: List[str], **kwargs) -> bool:
        args = ["install"]
        if kwargs.get("yes"):
            args.append("-y")
        if kwargs.get("simulate"):
            print(f"[SIMULATE] Would install via choco: {packages}")
            return True

        for pkg in packages:
            try:
                cmd = args + [pkg]
                result = self._run(cmd, capture=False, check=False)
                if result.returncode != 0:
                    return False
            except Exception as e:
                print(f"Failed to install {pkg} via choco: {e}")
                return False
        return True

    def remove(self, packages: List[str], purge: bool = False, **kwargs) -> bool:
        args = ["uninstall"]
        if kwargs.get("yes"):
            args.append("-y")
        if kwargs.get("simulate"):
            print(f"[SIMULATE] Would remove via choco: {packages}")
            return True

        for pkg in packages:
            try:
                cmd = args + [pkg]
                result = self._run(cmd, capture=False, check=False)
                if result.returncode != 0:
                    return False
            except Exception as e:
                print(f"Failed to remove {pkg} via choco: {e}")
                return False
        return True

    def upgrade(self, packages: Optional[List[str]] = None, **kwargs) -> bool:
        args = ["upgrade"]
        if kwargs.get("yes"):
            args.append("-y")
        if kwargs.get("simulate"):
            print(f"[SIMULATE] Would upgrade via choco: {packages or 'all'}")
            return True

        if packages:
            for pkg in packages:
                try:
                    cmd = args + [pkg]
                    result = self._run(cmd, capture=False, check=False)
                    if result.returncode != 0:
                        return False
                except Exception as e:
                    print(f"Failed to upgrade {pkg} via choco: {e}")
                    return False
        else:
            try:
                args.append("all")
                result = self._run(args, capture=False, check=False)
                return result.returncode == 0
            except Exception as e:
                print(f"Failed to upgrade all via choco: {e}")
                return False
        return True

    def search(self, keyword: str, **kwargs) -> List[Package]:
        packages = []
        try:
            result = self._run(["search", keyword], capture=True, check=False)
            if result.returncode != 0:
                return packages

            lines = result.stdout.strip().split("\n")
            for line in lines:
                line = line.strip()
                if not line or line.startswith("Chocolatey") or line.startswith("["):
                    continue
                # Parse: name|version
                if "|" in line:
                    parts = line.split("|")
                    if len(parts) >= 2:
                        pkg = Package(
                            name=parts[0].strip(),
                            version=parts[1].strip(),
                            source="choco",
                            description=""
                        )
                        packages.append(pkg)
        except Exception as e:
            print(f"choco search failed: {e}")
        return packages

    def show(self, package: str, **kwargs) -> Optional[Package]:
        try:
            result = self._run(["info", package], capture=True, check=False)
            if result.returncode != 0:
                return None

            info = {"name": package, "version": "unknown", "description": "", "publisher": ""}
            for line in result.stdout.split("\n"):
                line = line.strip()
                if line.startswith("Package id:") or line.startswith("Title:"):
                    info["name"] = line.split(":", 1)[1].strip()
                elif line.startswith("Version:"):
                    info["version"] = line.split(":", 1)[1].strip()
                elif line.startswith("Summary:") or line.startswith("Description:"):
                    info["description"] = line.split(":", 1)[1].strip()
                elif line.startswith("Author:") or line.startswith("Owners:"):
                    info["publisher"] = line.split(":", 1)[1].strip()

            return Package(
                name=info["name"],
                version=info["version"],
                source="choco",
                description=info["description"],
                publisher=info["publisher"]
            )
        except Exception as e:
            print(f"choco show failed: {e}")
            return None

    def list_installed(self, pattern: Optional[str] = None, **kwargs) -> List[Package]:
        packages = []
        try:
            args = ["list", "--local-only"]
            result = self._run(args, capture=True, check=False)
            if result.returncode != 0:
                return packages

            lines = result.stdout.strip().split("\n")
            for line in lines:
                line = line.strip()
                if not line or line.startswith("Chocolatey"):
                    continue
                if "|" in line:
                    parts = line.split("|")
                    if len(parts) >= 2:
                        name = parts[0].strip()
                        if pattern and pattern.lower() not in name.lower():
                            continue
                        pkg = Package(
                            name=name,
                            version=parts[1].strip(),
                            source="choco",
                            description="",
                            installed=True
                        )
                        packages.append(pkg)
        except Exception as e:
            print(f"choco list failed: {e}")
        return packages

    def list_upgradable(self, **kwargs) -> List[Package]:
        packages = []
        try:
            result = self._run(["outdated"], capture=True, check=False)
            if result.returncode != 0:
                return packages

            lines = result.stdout.strip().split("\n")
            for line in lines:
                line = line.strip()
                if not line or line.startswith("Chocolatey") or line.startswith("["):
                    continue
                if "|" in line:
                    parts = line.split("|")
                    if len(parts) >= 3:
                        pkg = Package(
                            name=parts[0].strip(),
                            version=parts[1].strip(),
                            source="choco",
                            description="",
                            installed=True,
                            upgradable=True,
                            latest_version=parts[2].strip()
                        )
                        packages.append(pkg)
        except Exception as e:
            print(f"choco outdated failed: {e}")
        return packages

    def autoremove(self, purge: bool = False, **kwargs) -> bool:
        print("choco does not support autoremove. Skipping.")
        return True

    def download(self, package: str, **kwargs) -> bool:
        print("choco download not fully supported in this version.")
        return False
