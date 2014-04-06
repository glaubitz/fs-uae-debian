from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import sys
import traceback
import fsbc.queue
from fsui.res import gettext


import_order = ["PySide", "PyQT5", "PyQT4"]
if "--pyqt5" in sys.argv:
    import_order = ["PyQT5"]
elif "--pyqt4" in sys.argv:
    import_order = ["PyQT4"]
elif "--pyside" in sys.argv:
    import_order = ["PySide"]
for name in import_order:
    if name == "PyQT5":
        try:
            import PyQt5
        except ImportError:
            continue
        else:
            from PyQt5.QtCore import *
            from PyQt5.QtGui import *
            from PyQt5.QtWidgets import *
            from PyQt5.QtCore import pyqtSignal as Signal
            from PyQt5.QtCore import pyqtSignal as QSignal
    elif name == "PyQT4":
        try:
            import PyQt4
        except ImportError:
            continue
        else:
            import sip
            sip.setapi("QString", 2)
            from PyQt4.QtCore import *
            from PyQt4.QtGui import *
            from PyQt4.QtCore import pyqtSignal as Signal
            from PyQt4.QtCore import pyqtSignal as QSignal
    elif name == "PySide":
        try:
            import PySide
        except ImportError:
            continue
        else:
            from PySide.QtCore import *
            from PySide.QtCore import Signal as QSignal
            from PySide.QtGui import *
    else:
        raise Exception("unknown QT python bindings specified")
    break
else:
    raise Exception("no QT python bindings found")


def get_screen_size():
    print("FIXME: get_screen_size")
    return 1920, 1080


class CustomEvent(QEvent):
    
    def __init__(self):
        QEvent.__init__(self, QEvent.User)


class EventHandler(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.queue = fsbc.queue.Queue()

    def customEvent(self, event):
        while True:
            try:
                function, args, kwargs = self.queue.get_nowait()
            except fsbc.queue.Empty:
                break
            try:
                function(*args, **kwargs)
            except Exception:
                #log.warn("callback event failed: %r %r",
                #        self.callback, self.args, exc_info=True)
                print("-- callback exception --")
                traceback.print_exc()

    def post_callback(self, function, *args, **kwargs):
        self.queue.put((function, args, kwargs))
        QCoreApplication.instance().postEvent(self, CustomEvent())

event_handler = EventHandler()


def call_after(function, *args, **kwargs):
    event_handler.post_callback(function, *args, **kwargs)


def call_later(duration, function, *args, **kwargs):
    # print("FIXME: call_later", duration, function)
    # raise NotImplementedError()
    # QApplication.instance().
    def timer_callback():
        function(*args, **kwargs)
    QTimer.singleShot(duration, timer_callback)


def show_error(message, title=None, parent=None):
    if not title:
        title = gettext("An Error Occurred")
    #QErrorMessage().showMessage(message)
    # message_box = QMessageBox()
    # message_box.setIcon(QMessageBox.Critical)
    # message_box.setText(message)
    # message_box.exec_()
    QMessageBox.critical(parent, title, message)


def error_function(title):
    def error_function_2(message):
        show_error(message, title)
    return error_function_2
