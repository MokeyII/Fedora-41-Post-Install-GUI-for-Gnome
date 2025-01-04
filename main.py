import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from dialogs import (
    dnf_update,
    flatpak_update,
    install_dnf_packages,
    install_nvidia_packages,
    install_flatpak_packages,
    install_gaming_flatpak_packages,
    add_repositories,
    install_media_codecs,
)

class InstallerWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Mokey's Fedora 41 Post Installer GUI for Gnome")
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        buttons = [
            ("Add Repositories", add_repositories),
            ("Update DNF Packages", dnf_update),
            ("Update Flatpaks", flatpak_update),
            ("Install DNF Packages", install_dnf_packages),
            ("Install NVIDIA Packages", install_nvidia_packages),
            ("Install Media Codec Packages", install_media_codecs),
            ("Install Flatpaks", install_flatpak_packages),
            ("Install Gaming Flatpaks", install_gaming_flatpak_packages),
        ]

        for label, callback in buttons:
            button = Gtk.Button(label=label)
            button.connect("clicked", lambda _, cb=callback: cb())
            vbox.pack_start(button, True, True, 0)

if __name__ == "__main__":
    win = InstallerWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
