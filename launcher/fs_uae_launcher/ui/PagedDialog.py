from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import fsui as fsui
from fsui.qt import Signal


class PagedDialog(fsui.Dialog):

    page_changed = Signal()

    def __init__(self, parent, title):
        fsui.Dialog.__init__(self, parent, title)
        self.layout = fsui.VerticalLayout()

        hor_layout = fsui.HorizontalLayout()
        self.layout.add(hor_layout, fill=True, expand=True)

        layout = fsui.VerticalLayout()
        layout.padding_top = 20
        layout.padding_bottom = 20
        layout.padding_left = 20
        #layout.padding_right = 20

        self.list_view = fsui.ListView(self)
        self.list_view.set_min_width(200)
        self.list_view.item_selected.connect(self.on_select_item)
        layout.add(self.list_view, fill=True, expand=True)
        hor_layout.add(layout, fill=True)

        #hor_layout.add_spacer(20)

        self.page_container = fsui.Panel(self)
        self.page_container.layout = fsui.VerticalLayout()
        hor_layout.add(self.page_container, fill=True, expand=True)

        #self.layout.add_spacer(20)

        hor_layout = fsui.HorizontalLayout()
        self.layout.add(hor_layout, fill=True)

        #hor_layout.add_spacer(20, expand=True)
        #self.close_button = fsui.Button(self, _("Close"))
        #self.close_button.on_activate = self.on_close_button
        #hor_layout.add(self.close_button)
        #hor_layout.add_spacer(20)
        #self.layout.add_spacer(20)

        self.page_titles = []
        self.pages = []

        #self.add_page(_("Hardware"), HardwarePage)
        #self.add_page(_("Hard Drives"), HardDrivesPage)
        #elf.add_page(_("Custom Options"), CustomOptionsPage)

        self.current_page = None
        self.set_size((800, 540))
        self.center_on_parent()

    # def on_close_button(self):
    #     self.end_modal(0)

    def on_select_item(self, index):
        self.set_page(index)

    def get_index(self):
        return self.list_view.get_index()

    def get_page_title(self, index):
        return self.page_titles[index][0]

    def get_page_index_by_title(self, title):
        for index, t in enumerate(self.page_titles):
            if t[0] == title:
                return index
        return None

    def add_page(self, title, function, icon=None):
        self.page_titles.append((title, icon))
        self.pages.append(function)
        self.list_view.set_items(self.page_titles)

    def set_page(self, index):
        if self.current_page:
            self.current_page.hide()
            self.page_container.layout.remove(self.current_page)
        if callable(self.pages[index]):
            page = self.pages[index](self.page_container)
            self.pages[index] = page
        else:
            page = self.pages[index]
        self.page_container.layout.add(page, fill=True, expand=True)
        self.current_page = page
        page.show()
        #print("calling self.layout.update")
        self.page_container.layout.update()
        self.layout.update()

        self.page_changed.emit()
