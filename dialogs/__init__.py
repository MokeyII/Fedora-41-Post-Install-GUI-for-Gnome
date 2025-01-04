# dialogs/__init__.py

from .dnf_update import dnf_update
from .flatpak_update import flatpak_update
from .install_dnf import install_dnf_packages
from .install_nvidia import install_nvidia_packages
from .install_flatpak import install_flatpak_packages
from .install_gaming_flatpak import install_gaming_flatpak_packages
from.install_codecs import install_media_codecs
from .add_repos import add_repositories

__all__ = [
    "dnf_update",
    "flatpak_update",
    "install_dnf_packages",
    "install_nvidia_packages",
    "install_flatpak_packages",
    "install_gaming_flatpak_packages",
    "install_media_codecs",
    "add_repositories",
]
