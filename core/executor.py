"""Command executor for WinApt"""
import sys
import os
import shutil
from typing import List, Optional
from core.config import load_config
from core.package import Package
from backends.winget import WingetBackend
from backends.choco import ChocoBackend
from easter_eggs import apt_moo, apt_get_moo, apt_sl, apt_random_easter_egg, apt_holiday

class AptExecutor:
    def __init__(self, prog_name="apt"):
        self.prog_name = prog_name
        self.config = load_config()
        self.backends = []
        self._init_backends()

    def _init_backends(self):
        winget = WingetBackend()
        choco = ChocoBackend()

        if winget.is_available():
            self.backends.append(winget)
        if choco.is_available():
            self.backends.append(choco)

        if not self.backends:
            print("ERROR: No package backend available!")
            print("Please install winget (Windows Package Manager) or Chocolatey.")
            print()
            print("To install winget: https://aka.ms/getwinget")
            print("To install Chocolatey: https://chocolatey.org/install")
            sys.exit(1)

    def _get_backend(self, name: str = None):
        if name:
            for b in self.backends:
                if b.name == name:
                    return b
        priority = self.config.get("priority", "winget")
        for b in self.backends:
            if b.name == priority:
                return b
        return self.backends[0] if self.backends else None

    def _get_all_backends(self):
        return self.backends

    def _print_header(self, text: str):
        sep = "=" * 60
        print("\n" + sep)
        print("  " + text)
        print(sep + "\n")

    def _print_success(self, text: str):
        print("  [OK] " + text)

    def _print_error(self, text: str):
        print("  [ERROR] " + text, file=sys.stderr)

    def _print_info(self, text: str):
        print("  [INFO] " + text)

    def execute(self, args):
        command = args.command

        if command is None:
            print(self.prog_name + ": no command specified")
            print("Try '" + self.prog_name + " --help' for more information.")
            return 1

        kwargs = {
            "yes": getattr(args, "yes", False),
            "simulate": getattr(args, "simulate", False),
            "quiet": getattr(args, "quiet", False),
            "verbose": getattr(args, "verbose", 0),
        }

        if command == "update":
            return self._cmd_update(kwargs)
        elif command == "upgrade":
            return self._cmd_upgrade(args, kwargs)
        elif command in ("full-upgrade", "dist-upgrade"):
            return self._cmd_full_upgrade(kwargs)
        elif command == "install":
            return self._cmd_install(args, kwargs)
        elif command == "remove":
            return self._cmd_remove(args, kwargs)
        elif command == "purge":
            return self._cmd_purge(args, kwargs)
        elif command == "autoremove":
            return self._cmd_autoremove(args, kwargs)
        elif command == "search":
            return self._cmd_search(args, kwargs)
        elif command == "show":
            return self._cmd_show(args, kwargs)
        elif command == "list":
            return self._cmd_list(args, kwargs)
        elif command == "depends":
            return self._cmd_depends(args, kwargs)
        elif command == "rdepends":
            return self._cmd_rdepends(args, kwargs)
        elif command == "policy":
            return self._cmd_policy(args, kwargs)
        elif command == "download":
            return self._cmd_download(args, kwargs)
        elif command == "source":
            return self._cmd_source(args, kwargs)
        elif command == "edit-sources":
            return self._cmd_edit_sources(kwargs)
        elif command == "moo":
            return self._cmd_moo(args)
        elif command == "cache":
            return self._cmd_cache(args, kwargs)
        elif command == "mark":
            return self._cmd_mark(args, kwargs)
        elif command == "satisfy":
            return self._cmd_satisfy(args, kwargs)
        elif command == "changelog":
            return self._cmd_changelog(args, kwargs)
        elif command == "build-dep":
            return self._cmd_build_dep(args, kwargs)
        elif command == "clean":
            return self._cmd_clean(kwargs)
        elif command == "autoclean":
            return self._cmd_autoclean(kwargs)
        elif command == "check":
            return self._cmd_check(kwargs)
        elif command == "fix-broken":
            return self._cmd_fix_broken(kwargs)
        elif command == "dselect-upgrade":
            return self._cmd_dselect_upgrade(kwargs)
        elif command == "version":
            return self._cmd_version()
        else:
            print(self.prog_name + ": unknown command '" + command + "'")
            print("Try '" + self.prog_name + " --help' for more information.")
            return 1

    def _cmd_update(self, kwargs):
        self._print_header("Updating Package Index")
        success = True
        for backend in self._get_all_backends():
            print("  -> Updating " + backend.name + "...")
            if not backend.update():
                self._print_error("Failed to update " + backend.name)
                success = False
            else:
                self._print_success(backend.name + " updated")
        if success:
            self._print_success("Package index updated successfully")
            return 0
        return 1

    def _cmd_upgrade(self, args, kwargs):
        self._print_header("Upgrading Packages")
        packages = getattr(args, "packages", None)

        success = True
        for backend in self._get_all_backends():
            print("  -> Upgrading via " + backend.name + "...")
            if not backend.upgrade(packages, **kwargs):
                self._print_error("Failed to upgrade via " + backend.name)
                success = False
            else:
                self._print_success("Upgrade completed via " + backend.name)
        return 0 if success else 1

    def _cmd_full_upgrade(self, kwargs):
        self._print_header("Performing Full System Upgrade")
        success = True
        for backend in self._get_all_backends():
            print("  -> Full upgrade via " + backend.name + "...")
            if not backend.upgrade(None, **kwargs):
                self._print_error("Failed to full-upgrade via " + backend.name)
                success = False
            else:
                self._print_success("Full upgrade completed via " + backend.name)
        return 0 if success else 1

    def _cmd_install(self, args, kwargs):
        self._print_header("Installing Packages: " + ", ".join(args.packages))
        success = True
        for backend in self._get_all_backends():
            print("  -> Installing via " + backend.name + "...")
            if not backend.install(args.packages, **kwargs):
                self._print_error("Failed to install via " + backend.name)
                success = False
            else:
                self._print_success("Installation completed via " + backend.name)
        return 0 if success else 1

    def _cmd_remove(self, args, kwargs):
        self._print_header("Removing Packages: " + ", ".join(args.packages))
        purge = getattr(args, "purge", False)
        success = True
        for backend in self._get_all_backends():
            print("  -> Removing via " + backend.name + "...")
            if not backend.remove(args.packages, purge=purge, **kwargs):
                self._print_error("Failed to remove via " + backend.name)
                success = False
            else:
                self._print_success("Removal completed via " + backend.name)
        return 0 if success else 1

    def _cmd_purge(self, args, kwargs):
        self._print_header("Purging Packages: " + ", ".join(args.packages))
        success = True
        for backend in self._get_all_backends():
            print("  -> Purging via " + backend.name + "...")
            if not backend.remove(args.packages, purge=True, **kwargs):
                self._print_error("Failed to purge via " + backend.name)
                success = False
            else:
                self._print_success("Purge completed via " + backend.name)
        return 0 if success else 1

    def _cmd_autoremove(self, args, kwargs):
        self._print_header("Removing Automatically Installed Packages")
        purge = getattr(args, "purge", False)
        success = True
        for backend in self._get_all_backends():
            print("  -> Autoremove via " + backend.name + "...")
            if not backend.autoremove(purge=purge, **kwargs):
                self._print_error("Failed to autoremove via " + backend.name)
                success = False
            else:
                self._print_success("Autoremove completed via " + backend.name)
        return 0 if success else 1

    def _cmd_search(self, args, kwargs):
        self._print_header("Searching for: " + args.keyword)
        all_results = []
        for backend in self._get_all_backends():
            print("  -> Searching " + backend.name + "...")
            results = backend.search(args.keyword, **kwargs)
            for pkg in results:
                pkg.source = backend.name
            all_results.extend(results)

        if not all_results:
            print("  No packages found.")
            return 0

        print("\n  Found " + str(len(all_results)) + " package(s):\n")
        for pkg in all_results:
            print("  " + pkg.name + "/" + pkg.version + " [" + pkg.source + "]")
            if pkg.description:
                print("    " + pkg.description[:80] + "...")
        return 0

    def _cmd_show(self, args, kwargs):
        self._print_header("Package Details: " + args.package)
        found = False
        for backend in self._get_all_backends():
            pkg = backend.show(args.package, **kwargs)
            if pkg:
                found = True
                print("  Package: " + pkg.name)
                print("  Version: " + pkg.version)
                print("  Source:  " + pkg.source)
                if pkg.publisher:
                    print("  Publisher: " + pkg.publisher)
                if pkg.description:
                    print("  Description: " + pkg.description)
                if pkg.homepage:
                    print("  Homepage: " + pkg.homepage)
                if pkg.license:
                    print("  License: " + pkg.license)
                print()

        if not found:
            self._print_error("Package '" + args.package + "' not found")
            return 1
        return 0

    def _cmd_list(self, args, kwargs):
        pattern = getattr(args, "pattern", None)
        installed = getattr(args, "installed", False)
        upgradable = getattr(args, "upgradable", False)

        if upgradable:
            self._print_header("Listing Upgradable Packages")
            all_pkgs = []
            for backend in self._get_all_backends():
                pkgs = backend.list_upgradable(**kwargs)
                all_pkgs.extend(pkgs)
        elif installed or pattern:
            header_text = "Listing Installed Packages"
            if pattern:
                header_text += " matching '" + pattern + "'"
            self._print_header(header_text)
            all_pkgs = []
            for backend in self._get_all_backends():
                pkgs = backend.list_installed(pattern, **kwargs)
                all_pkgs.extend(pkgs)
        else:
            self._print_header("Listing Packages")
            all_pkgs = []
            for backend in self._get_all_backends():
                pkgs = backend.list_installed(pattern, **kwargs)
                all_pkgs.extend(pkgs)

        if not all_pkgs:
            print("  No packages found.")
            return 0

        print("\n  " + str(len(all_pkgs)) + " package(s) found:\n")
        for pkg in all_pkgs:
            status = ""
            if pkg.upgradable:
                status = " [upgradable from: " + pkg.version + " -> " + str(pkg.latest_version) + "]"
            elif pkg.installed:
                status = " [installed]"
            print("  " + pkg.name + "/" + pkg.version + status + " [" + pkg.source + "]")
        return 0

    def _cmd_depends(self, args, kwargs):
        self._print_header("Dependencies for: " + args.package)
        print("  (Dependency resolution not fully implemented for Windows backends)")
        print("  Showing package info instead:")
        return self._cmd_show(args, kwargs)

    def _cmd_rdepends(self, args, kwargs):
        self._print_header("Reverse Dependencies for: " + args.package)
        print("  (Reverse dependency resolution not fully implemented for Windows backends)")
        return 0

    def _cmd_policy(self, args, kwargs):
        self._print_header("Package Policy")
        if args.package:
            print("  Package: " + args.package)
            for backend in self._get_all_backends():
                pkg = backend.show(args.package, **kwargs)
                if pkg:
                    print("  " + backend.name + ": " + pkg.version)
        else:
            print("  Installed backends:")
            for backend in self._get_all_backends():
                print("    - " + backend.name)
            print("\n  Priority: " + self.config.get("priority", "winget"))
        return 0

    def _cmd_download(self, args, kwargs):
        self._print_header("Downloading: " + args.package)
        success = False
        for backend in self._get_all_backends():
            if backend.download(args.package, **kwargs):
                success = True
                break
        return 0 if success else 1

    def _cmd_source(self, args, kwargs):
        self._print_header("Downloading Source: " + args.package)
        print("  (Source download not supported on Windows)")
        return 1

    def _cmd_edit_sources(self, kwargs):
        self._print_header("Editing Sources")
        config_file = os.path.expanduser("~/.winapt/config.json")
        print("  Opening " + config_file + "...")
        if sys.platform == "win32":
            os.startfile(config_file)
        else:
            editors = ["notepad", "nano", "vim", "code"]
            for editor in editors:
                if shutil.which(editor):
                    os.system(editor + ' "' + config_file + '"')
                    break
        return 0

    def _cmd_moo(self, args):
        if self.prog_name == "apt-get":
            apt_get_moo(args.verbose)
        else:
            apt_moo(args.verbose)
        return 0

    def _cmd_cache(self, args, kwargs):
        cache_cmd = getattr(args, "cache_command", None)
        if cache_cmd == "clean":
            self._print_header("Cleaning Cache")
            for backend in self._get_all_backends():
                backend.clean()
            return 0
        elif cache_cmd == "stats":
            self._print_header("Cache Statistics")
            print("  (Cache statistics not available)")
            return 0
        elif cache_cmd == "dump":
            self._print_header("Dumping Cache")
            print("  (Cache dump not available)")
            return 0
        else:
            print("Usage: apt cache {clean|stats|dump}")
            return 1

    def _cmd_mark(self, args, kwargs):
        mark_cmd = getattr(args, "mark_command", None)
        pkg = getattr(args, "package", None)
        if mark_cmd and pkg:
            self._print_header("Marking " + pkg + " as " + mark_cmd)
            print("  (Marking not implemented for Windows backends)")
            return 0
        print("Usage: apt mark {hold|unhold|manual|auto} <package>")
        return 1

    def _cmd_satisfy(self, args, kwargs):
        self._print_header("Satisfying: " + ", ".join(args.packages))
        return self._cmd_install(args, kwargs)

    def _cmd_changelog(self, args, kwargs):
        self._print_header("Changelog for: " + args.package)
        print("  (Changelogs not available via winget/choco)")
        return 0

    def _cmd_build_dep(self, args, kwargs):
        self._print_header("Build Dependencies for: " + args.package)
        print("  (Build dependencies not applicable on Windows)")
        return 0

    def _cmd_clean(self, kwargs):
        self._print_header("Cleaning Downloaded Packages")
        for backend in self._get_all_backends():
            backend.clean()
        self._print_success("Clean completed")
        return 0

    def _cmd_autoclean(self, kwargs):
        self._print_header("Cleaning Old Downloaded Packages")
        for backend in self._get_all_backends():
            backend.clean()
        self._print_success("Autoclean completed")
        return 0

    def _cmd_check(self, kwargs):
        self._print_header("Checking for Broken Dependencies")
        print("  (Dependency check not fully implemented for Windows)")
        print("  All backends operational.")
        return 0

    def _cmd_fix_broken(self, kwargs):
        self._print_header("Fixing Broken Dependencies")
        print("  (Fix-broken not applicable on Windows)")
        return 0

    def _cmd_dselect_upgrade(self, kwargs):
        self._print_header("dselect Upgrade")
        print("  (dselect not available on Windows)")
        return 0

    def _cmd_version(self):
        print("WinApt 1.0.0")
        print("apt-like package manager for Windows")
        print("Backends: winget, Chocolatey")
        return 0
