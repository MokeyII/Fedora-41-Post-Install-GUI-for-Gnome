import subprocess
from utils.dialog_helper import show_selection_dialog

def install_media_codecs():
    codecs = {
        "FFmpeg": "ffmpeg",
        "Fedora Cisco OpenH264": "fedora-cisco-openh264",
        "GStreamer OpenH264 Plugin": "gstreamer1-plugin-openh264 mozilla-openh264",
        "x265 Libraries": "x265-libs",
    }
    selected_codecs = show_selection_dialog("Media Codecs", codecs)
    if selected_codecs:
        for codec in selected_codecs:
            if codec == "fedora-cisco-openh264":
                subprocess.run(["sudo", "dnf", "config-manager", "--set-enabled", codec])
            else:
                subprocess.run(["sudo", "dnf", "install", "-y", codec])
        subprocess.run(["sudo", "dnf", "update", "-y"])