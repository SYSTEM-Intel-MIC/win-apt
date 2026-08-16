"""Base backend interface"""
from abc import ABC, abstractmethod
from typing import List, Optional
from core.package import Package

class PackageBackend(ABC):
    name: str = "base"
    available: bool = False

    def __init__(self):
        self._check_available()

    @abstractmethod
    def _check_available(self):
        """Check if the backend tool is available"""
        pass

    @abstractmethod
    def update(self) -> bool:
        """Update package index"""
        pass

    @abstractmethod
    def install(self, packages: List[str], **kwargs) -> bool:
        """Install packages"""
        pass

    @abstractmethod
    def remove(self, packages: List[str], purge: bool = False, **kwargs) -> bool:
        """Remove packages"""
        pass

    @abstractmethod
    def upgrade(self, packages: Optional[List[str]] = None, **kwargs) -> bool:
        """Upgrade packages"""
        pass

    @abstractmethod
    def search(self, keyword: str, **kwargs) -> List[Package]:
        """Search for packages"""
        pass

    @abstractmethod
    def show(self, package: str, **kwargs) -> Optional[Package]:
        """Show package details"""
        pass

    @abstractmethod
    def list_installed(self, pattern: Optional[str] = None, **kwargs) -> List[Package]:
        """List installed packages"""
        pass

    @abstractmethod
    def list_upgradable(self, **kwargs) -> List[Package]:
        """List upgradable packages"""
        pass

    @abstractmethod
    def autoremove(self, purge: bool = False, **kwargs) -> bool:
        """Remove automatically installed packages"""
        pass

    @abstractmethod
    def download(self, package: str, **kwargs) -> bool:
        """Download package"""
        pass

    def clean(self) -> bool:
        """Clean cache"""
        return True

    def is_available(self) -> bool:
        return self.available
