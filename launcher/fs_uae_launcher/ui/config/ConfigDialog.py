from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import fsui as fsui
from ...I18N import _, ngettext
from ..PagedDialog import PagedDialog
from .CustomOptionsPage import CustomOptionsPage
# from ..settings.CustomSettingsPage import CustomSettingsPage


class ConfigDialog(fsui.Dialog):

    CUSTOM_OPTIONS = 0

    def __init__(self, parent, index):
        fsui.Dialog.__init__(self, parent, _("Custom Configuration"))

        # self.add_page(_("Custom Options"), CustomOptionsPage)
        # self.add_page(_("Custom Settings"), CustomSettingsPage)
        self.layout = fsui.VerticalLayout()
        self.layout.add(CustomOptionsPage(self), fill=True, expand=True)

        # self.list_view.set_index(0)
        self.set_size((800, 540))
        self.center_on_parent()

    @classmethod
    def run(cls, parent, index):
        dialog = cls(parent, index)
        dialog.show_modal()
        # FIXME: shouldn't really be necessary, but right now still is to
        # ensure onclose handlers are run if the dialog is dismissed with
        # endmodal -- dialog class should be updated/improved.
        dialog.close()
        dialog.destroy()
