from gi.repository import Gtk

def show_selection_dialog(title, items, disable_on_select_all=False):
    dialog = Gtk.Dialog(title=title, transient_for=None, flags=0)
    dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK)
    box = dialog.get_content_area()
    label = Gtk.Label(label=f"Select {title.lower()}:")
    box.add(label)

    check_buttons = []

    if disable_on_select_all:
        select_all_button = Gtk.CheckButton(label="Install All Gaming Flatpaks")
        box.add(select_all_button)

        def toggle_all_check_buttons(widget):
            for check_button in check_buttons:
                if check_button != widget:
                    check_button.set_sensitive(not widget.get_active())

        select_all_button.connect("toggled", toggle_all_check_buttons)
        check_buttons.append(select_all_button)

    for name, command in items.items():
        check_button = Gtk.CheckButton(label=name)
        check_button.command = command
        box.add(check_button)
        check_buttons.append(check_button)

    dialog.show_all()
    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        if disable_on_select_all and select_all_button.get_active():
            selected_items = list(items.values())  # Install all
        else:
            selected_items = [btn.command for btn in check_buttons if btn.get_active() and hasattr(btn, 'command')]
    else:
        selected_items = []
    dialog.destroy()
    return selected_items
