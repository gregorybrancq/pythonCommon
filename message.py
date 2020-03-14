#!/usr/bin/env python
# -*- coding: utf-8 -*-

# basic import
import sys

# use for graphical interface
try:
    import pygtk
    pygtk.require('2.0')
except ImportError as e:
    sys.exit("Issue with PyGTK.\n" + str(e))
try:
    import gtk
except (RuntimeError, ImportError) as e:
    sys.exit("Issue with GTK.\n" + str(e))


###############################################
## Message Dialog Class
###############################################

"""Shows a message. The message type, title and the message to be
displayed can be passed when initializing the class."""


class MessageDialog(object):
    """Shows a message. The message type, title and the message to be
    displayed can be passed when initializing the class."""

    def __init__(self, type_, title, message):
        self.type = type_
        if self.type == 'error':
            self.dialog = gtk.MessageDialog(
                type=gtk.MESSAGE_ERROR, buttons=gtk.BUTTONS_CLOSE)
        elif self.type == 'info':
            self.dialog = gtk.MessageDialog(
                type=gtk.MESSAGE_INFO, buttons=gtk.BUTTONS_CLOSE)
        elif self.type == 'question':
            self.dialog = gtk.MessageDialog(
                type=gtk.MESSAGE_QUESTION, buttons=gtk.BUTTONS_YES_NO)
        elif self.type == 'entry':
            self.dialog = gtk.MessageDialog(
                type=gtk.MESSAGE_QUESTION, buttons=gtk.BUTTONS_YES_NO)
            dialogBox = self.dialog.get_content_area()
            self.userEntry = gtk.Entry()
            self.userEntry.show()
            # the following will trigger OK response when enter is hit in the entry
            self.userEntry.connect("activate", lambda w: self.dialog.response(gtk.RESPONSE_YES))
            dialogBox.pack_end(self.userEntry, False, False, 0)
        self.dialog.set_title(title)
        self.dialog.set_markup(message)
        self.dialog.show_all()

    def run(self):
        """Runs the dialog and closes it afterwards."""
        response = self.dialog.run()
        self.dialog.hide()
        if (response == gtk.RESPONSE_YES) and (self.type == 'entry'):
            return self.userEntry.get_text()
        else:
            return response


## End dialog
def MessageDialogEnd(warnC, errC, logFile, title, msg):
    if (errC != 0):
        msg += "\nError = " + str(errC)
        msg += "\nLog file = " + str(logFile)
        MessageDialog(type_='error', title=title, message=msg).run()
    else:
        if (warnC != 0):
            msg += "\nWarning = " + str(warnC)
        msg += "\n\nLog file = " + str(logFile)
        MessageDialog(type_='info', title=title, message=msg).run()

###############################################
