"""Command line argument parser for apt/apt-get"""
import argparse
import sys

class AptParser:
    def __init__(self, prog_name="apt"):
        self.prog_name = prog_name
        self.parser = self._create_parser()

    def _create_parser(self):
        parser = argparse.ArgumentParser(
            prog=self.prog_name,
            description=f"WinApt - apt-like package manager for Windows (via winget/choco)",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Most used commands:
  update      - Update package index
  upgrade     - Upgrade installed packages
  install     - Install packages
  remove      - Remove packages
  autoremove  - Remove automatically installed packages
  purge       - Remove packages and config files
  search      - Search for packages
  show        - Show package details
  list        - List packages
  full-upgrade- Full system upgrade
  edit-sources- Edit source list
  moo         - Have you mooed today?

See '{self.prog_name} <command> --help' for more info.
            """.strip()
        )

        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # Common arguments
        common = argparse.ArgumentParser(add_help=False)
        common.add_argument("-y", "--yes", action="store_true", help="Assume yes")
        common.add_argument("--simulate", "-s", action="store_true", help="Simulate only")
        common.add_argument("--no-color", action="store_true", help="Disable colored output")
        common.add_argument("-q", "--quiet", action="store_true", help="Quiet mode")
        common.add_argument("-v", "--verbose", action="count", default=0, help="Verbose mode")

        # update
        p_update = subparsers.add_parser("update", parents=[common], help="Update package index")
        p_update.add_argument("sources", nargs="*", help="Specific sources to update")

        # upgrade
        p_upgrade = subparsers.add_parser("upgrade", parents=[common], help="Upgrade packages")
        p_upgrade.add_argument("packages", nargs="*", help="Packages to upgrade")
        p_upgrade.add_argument("--with-new-pkgs", action="store_true", help="Allow installing new packages")

        # full-upgrade / dist-upgrade
        p_full = subparsers.add_parser("full-upgrade", parents=[common], help="Full system upgrade")
        p_full.add_argument("--with-new-pkgs", action="store_true", help="Allow installing new packages")

        p_dist = subparsers.add_parser("dist-upgrade", parents=[common], help="Same as full-upgrade")
        p_dist.add_argument("--with-new-pkgs", action="store_true", help="Allow installing new packages")

        # install
        p_install = subparsers.add_parser("install", parents=[common], help="Install packages")
        p_install.add_argument("packages", nargs="+", help="Packages to install")
        p_install.add_argument("--no-install-recommends", action="store_true", help="Skip recommended packages")
        p_install.add_argument("--install-suggests", action="store_true", help="Install suggested packages")
        p_install.add_argument("--reinstall", action="store_true", help="Reinstall packages")
        p_install.add_argument("--download-only", "-d", action="store_true", help="Download only")

        # remove
        p_remove = subparsers.add_parser("remove", parents=[common], help="Remove packages")
        p_remove.add_argument("packages", nargs="+", help="Packages to remove")
        p_remove.add_argument("--purge", action="store_true", help="Purge configuration files")

        # purge
        p_purge = subparsers.add_parser("purge", parents=[common], help="Purge packages")
        p_purge.add_argument("packages", nargs="+", help="Packages to purge")

        # autoremove
        p_auto = subparsers.add_parser("autoremove", parents=[common], help="Remove automatically installed packages")
        p_auto.add_argument("--purge", action="store_true", help="Purge configuration files")

        # search
        p_search = subparsers.add_parser("search", parents=[common], help="Search for packages")
        p_search.add_argument("keyword", help="Search keyword")
        p_search.add_argument("--names-only", action="store_true", help="Search names only")
        p_search.add_argument("--full", action="store_true", help="Full text search")

        # show
        p_show = subparsers.add_parser("show", parents=[common], help="Show package details")
        p_show.add_argument("package", help="Package name")
        p_show.add_argument("--all-versions", action="store_true", help="Show all versions")

        # list
        p_list = subparsers.add_parser("list", parents=[common], help="List packages")
        p_list.add_argument("pattern", nargs="?", help="Package pattern")
        p_list.add_argument("--installed", action="store_true", help="List installed packages")
        p_list.add_argument("--upgradable", action="store_true", help="List upgradable packages")
        p_list.add_argument("--all-versions", action="store_true", help="Show all versions")

        # depends / rdepends
        p_dep = subparsers.add_parser("depends", parents=[common], help="Show dependencies")
        p_dep.add_argument("package", help="Package name")

        p_rdep = subparsers.add_parser("rdepends", parents=[common], help="Show reverse dependencies")
        p_rdep.add_argument("package", help="Package name")

        # policy
        p_policy = subparsers.add_parser("policy", parents=[common], help="Show policy")
        p_policy.add_argument("package", nargs="?", help="Package name")

        # download
        p_download = subparsers.add_parser("download", parents=[common], help="Download package")
        p_download.add_argument("package", help="Package name")

        # source
        p_source = subparsers.add_parser("source", parents=[common], help="Download source")
        p_source.add_argument("package", help="Package name")

        # edit-sources
        p_edit = subparsers.add_parser("edit-sources", parents=[common], help="Edit sources list")

        # moo
        p_moo = subparsers.add_parser("moo", help="Have you mooed today?")
        p_moo.add_argument("-v", "--verbose", action="count", default=0, help="More verbosity = more cow power")

        # cache
        p_cache = subparsers.add_parser("cache", help="Cache management")
        cache_sub = p_cache.add_subparsers(dest="cache_command")
        cache_sub.add_parser("clean", help="Clean cache")
        cache_sub.add_parser("stats", help="Cache statistics")
        cache_sub.add_parser("dump", help="Dump cache")

        # mark
        p_mark = subparsers.add_parser("mark", help="Mark packages")
        mark_sub = p_mark.add_subparsers(dest="mark_command")
        p_hold = mark_sub.add_parser("hold", help="Hold package")
        p_hold.add_argument("package", help="Package name")
        p_unhold = mark_sub.add_parser("unhold", help="Unhold package")
        p_unhold.add_argument("package", help="Package name")
        p_manual = mark_sub.add_parser("manual", help="Mark as manually installed")
        p_manual.add_argument("package", help="Package name")
        p_auto_mark = mark_sub.add_parser("auto", help="Mark as automatically installed")
        p_auto_mark.add_argument("package", help="Package name")

        # satisfy
        p_satisfy = subparsers.add_parser("satisfy", parents=[common], help="Satisfy dependencies")
        p_satisfy.add_argument("packages", nargs="+", help="Packages to satisfy")

        # changelog
        p_changelog = subparsers.add_parser("changelog", parents=[common], help="Show changelog")
        p_changelog.add_argument("package", help="Package name")

        # build-dep
        p_builddep = subparsers.add_parser("build-dep", parents=[common], help="Install build dependencies")
        p_builddep.add_argument("package", help="Package name")

        # clean / autoclean
        p_clean = subparsers.add_parser("clean", parents=[common], help="Clean downloaded packages")
        p_autoclean = subparsers.add_parser("autoclean", parents=[common], help="Clean old downloaded packages")

        # check
        p_check = subparsers.add_parser("check", parents=[common], help="Check for broken dependencies")

        # fix-broken
        p_fix = subparsers.add_parser("fix-broken", parents=[common], help="Fix broken dependencies")

        # dselect-upgrade
        p_dselect = subparsers.add_parser("dselect-upgrade", parents=[common], help="Follow dselect selections")

        return parser

    def parse(self, args=None):
        if args is None:
            args = sys.argv[1:]

        # Handle --version
        if "--version" in args or "-v" in args and len(args) == 1 and args[0] == "-v":
            if "--version" in args:
                return argparse.Namespace(command="version")

        return self.parser.parse_args(args)

    def print_help(self):
        self.parser.print_help()


class AptGetParser(AptParser):
    """apt-get parser with additional options"""
    def __init__(self):
        super().__init__(prog_name="apt-get")

    def _create_parser(self):
        parser = super()._create_parser()

        # Add apt-get specific options to the main parser
        # We need to recreate since argparse doesn't support easy modification
        # For simplicity, we just use the same parser but note it's apt-get
        return parser
