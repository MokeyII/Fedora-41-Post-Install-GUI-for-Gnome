import subprocess
from gi.repository import Gtk

def flatpak_update():
    dialog = Gtk.MessageDialog(
        transient_for=None,
        flags=0,
        message_type=Gtk.MessageType.INFO,
        buttons=Gtk.ButtonsType.OK,
        text="Updating Flatpaks",
    )
    dialog.format_secondary_text("Running: flatpak update -y")
    dialog.show_all()
    subprocess.run(["flatpak", "update", "-y"])
    dialog.destroy()
