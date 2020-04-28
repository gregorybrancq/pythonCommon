#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Open a window to print the status of the program
"""

# use for graphical interface
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

##############################################
# Message Dialog Class
##############################################

"""Shows a message. The message type, title and the message to be
displayed can be passed when initializing the class."""


class MessageDialog(object):
    """Shows a message. The message type, title and the message to be
    displayed can be passed when initializing the class."""

    def __init__(self, dialog_type, title, message1, message2=None):
        self.type = dialog_type

        if self.type == 'error':
            self.dialog = Gtk.MessageDialog(Gtk.Window(),
                                            Gtk.DialogFlags.MODAL,
                                            Gtk.MessageType.ERROR,
                                            Gtk.ButtonsType.CLOSE,
                                            message1,
                                            )
            if message2 is not None:
                self.dialog.format_secondary_text(message2)

        elif self.type == 'info':
            self.dialog = Gtk.MessageDialog(Gtk.Window(),
                                            Gtk.DialogFlags.MODAL,
                                            Gtk.MessageType.INFO,
                                            Gtk.ButtonsType.CLOSE,
                                            message1,
                                            )
            if message2 is not None:
                self.dialog.format_secondary_text(message2)

        elif self.type == 'question':
            self.dialog = Gtk.MessageDialog(Gtk.Window(),
                                            Gtk.DialogFlags.MODAL,
                                            Gtk.MessageType.QUESTION,
                                            Gtk.ButtonsType.YES_NO,
                                            message1,
                                            )
            if message2 is not None:
                self.dialog.format_secondary_text(message2)

        elif self.type == 'entry':
            self.dialog = Gtk.MessageDialog(Gtk.Window(),
                                            Gtk.DialogFlags.MODAL,
                                            Gtk.MessageType.QUESTION,
                                            Gtk.ButtonsType.YES_NO,
                                            message1,
                                            )
            if message2 is not None:
                self.dialog.format_secondary_text(message2)

            dialog_box = self.dialog.get_content_area()
            self.userEntry = Gtk.Entry()
            self.userEntry.show()
            # the following will trigger OK response when enter is hit in the entry
            self.userEntry.connect("activate", lambda w: self.dialog.response(Gtk.ResponseType.YES))
            dialog_box.pack_end(self.userEntry, False, False, 0)

        self.dialog.set_title(title)
        self.dialog.show_all()

    def run(self):
        """Runs the dialog and closes it afterwards."""
        response = self.dialog.run()
        if (response == Gtk.ResponseType.YES) and (self.type == 'entry'):
            user_text = self.userEntry.get_text()
            self.dialog.destroy()
            return user_text
        else:
            self.dialog.destroy()
            return response


# End dialog
def MessageDialogEnd(error, log_file, title, msg1, msg2):
    if error:
        msg2 += "\nLog file = " + str(log_file)
        MessageDialog(dialog_type='error', title=title, message1=msg1, message2=msg2).run()
    else:
        msg2 += "\nLog file = " + str(log_file)
        MessageDialog(dialog_type='info', title=title, message1=msg1, message2=msg2).run()

# 'application' code
# print(MessageDialog('error', "Error !", "Le programme a planté", "comme une grosse ...").run())
# print(MessageDialog('info', "Info", "C'est une information importante").run())
# print(MessageDialog('question', "Question ?", "Irais-tu sur la lune si tu le pouvais ?", "une petite aide : pourquoi pas...").run())
# print(MessageDialog('entry', "Entry", "Question importante", "Donne moi un chiffre").run())
