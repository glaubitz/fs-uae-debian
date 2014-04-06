from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import sys
import weakref
from fsui.qt import Qt, QMainWindow, QDesktopWidget, Signal

_windows = set()


class Window(QMainWindow):

    closed = Signal()
    default_parent = None
    default_center = None

    def __init__(self, parent=None, title=""):
        if parent is None and Window.default_parent:
            parent = Window.default_parent
            print("using default parent", parent)
        QMainWindow.__init__(self, parent)

        self._window = weakref.ref(self)

        self.setWindowTitle(title)
        self.destroyed.connect(self.__destroyed)
        self.setAttribute(Qt.WA_DeleteOnClose, True)

        self._size_specified = False
        self.destroy_listeners = []
        self.close_listeners = []
        _windows.add(self)
        self.closed.connect(self.__on_closed)

        self.already_closed = False

    def __on_closed(self):
        print("__on_closed, removing", self)
        _windows.remove(self)

    def set_icon(self, icon):
        self.setWindowIcon(icon.qicon())

    def close(self):
        QMainWindow.close(self)

    def get_container(self):
        return self

    def get_parent(self):
        return None

    def add_destroy_listener(self, function):
        self.destroy_listeners.append(function)

    def add_close_listener(self, function):
        # self.close_listeners.append(function)
        self.closed.connect(function)

    def on_close(self):
        pass

    def closeEvent(self, event):
        print("Window.closeEvent")
        if self.already_closed:
            print("Looks like a duplicate event, ignoring this one")
            return

        self.closed.emit()
        self.on_close()
        # for function in self.close_listeners:
        #     function()
        event.accept()
        #self.destroy()
         #event.ignore()
        self.already_closed = True

    def get_window(self):
        return self
 
    def on_destroy(self):
        pass

    def __destroyed(self):
        print("__destroyed")
        for function in self.destroy_listeners:
            function()
        self.on_destroy()

    def showEvent(self, event):
        self.on_resize()

    def get_position(self):
        return self.pos().x(), self.pos().y()

    def set_position(self, position):
        self.move(position[0], position[1])

    def get_size(self):
        return self.width(), self.height()

    def set_size(self, size):
        self._size_specified = True
        #self.SetClientSize(size)
        #print("FIXME:\n\nDialog.set_size")
        self.resize(size[0], size[1])

    def is_maximized(self):
        #return self.isMaximized()
        print("FIXME: always returning False")
        return False

    def maximize(self):
        self.showMaximized()

    def get_window_center(self):
        return self.x() + self.width() // 2, self.y() + self.height() // 2

    def center_on_parent(self):
        real_parent = self.parent()
        if real_parent:
            pp = real_parent.x(), real_parent.y()
            ps = real_parent.width(), real_parent.height()
            ss = self.get_size()
            self.move(pp[0] + (ps[0] - ss[0]) // 2,
                      pp[1] + (ps[1] - ss[1]) // 2)
        elif self.default_center:
            x, y = self.default_center
            ss = self.get_size()
            self.move(x - ss[0] // 2, y - ss[1] // 2,)

    def center_on_screen(self):
        frect = self.frameGeometry()
        frect.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(frect.topLeft())

    def resizeEvent(self, event):
        print("resized..")
        self.on_resize()

    def on_resize(self):
        if self.layout:
            self.layout.set_size(self.get_size())
            self.layout.update()

    def set_background_color(self, color):
        p = self.palette()
        p.setColor(self.backgroundRole(), color)
        self.setPalette(p)

    def set_icon_from_path(self, path):
        print("FIXME: Window.set_icon_from_path")

    def show(self):
        if hasattr(self, "layout") and not self._size_specified:
            self.set_size(self.layout.get_min_size())
        QMainWindow.show(self)

    def is_shown(self):
        return self.isVisible()

    def raise_and_activate(self):
        self.raise_()
        self.activateWindow()


if "--workspace" in sys.argv:
    fs_uae_workspace = __import__("fs_uae_workspace.window")
    if not "--windows" in sys.argv:
        from fs_uae_workspace.window import Window

# else:
#     base_class = QMainWindow
