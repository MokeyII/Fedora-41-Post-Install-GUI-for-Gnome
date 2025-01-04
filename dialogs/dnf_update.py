import subprocess
from gi.repository import Gtk

def dnf_update():
    dialog = Gtk.MessageDialog(
        transient_for=None,
        flags=0,
        message_type=Gtk.MessageType.INFO,
        buttons=Gtk.ButtonsType.OK,
        text="Updating DNF Packages",
    )
    dialog.format_secondary_text("Running: sudo dnf update -y")
    dialog.show_all()
    subprocess.run(["sudo", "dnf", "update", "-y"])
    dialog.destroy()
