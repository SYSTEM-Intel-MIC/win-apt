"""Package data models"""
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Package:
    name: str
    version: str
    source: str  # winget or choco
    description: str = ""
    publisher: str = ""
    installed: bool = False
    upgradable: bool = False
    latest_version: Optional[str] = None
    size: Optional[str] = None
    architecture: Optional[str] = None
    homepage: Optional[str] = None
    license: Optional[str] = None
    dependencies: List[str] = None

    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []

    def __str__(self):
        status = "[installed]" if self.installed else ""
        if self.upgradable:
            status = f"[installed, upgradable: {self.latest_version}]"
        return f"{self.name}/{self.version} {status} - {self.description}"
