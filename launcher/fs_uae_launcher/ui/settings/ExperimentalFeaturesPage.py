import fsui as fsui
from fsui.extra.iconheader import NewIconHeader
from ...I18N import gettext
from .OptionUI import OptionUI


class ExperimentalFeaturesPage(fsui.Panel):

    def __init__(self, parent):
        fsui.Panel.__init__(self, parent)
        self.layout = fsui.VerticalLayout()
        # self.layout.set_padding(20, 20, 20, 20)

        self.icon_header = NewIconHeader(
            self, fsui.Icon("settings", "pkg:fs_uae_workspace"),
            gettext("Experimental Features"),
            "")
        self.layout.add(self.icon_header, fill=True, margin_bottom=20)

        # label = fsui.HeadingLabel(self, _("Experimental Features"))
        # self.layout.add(label, margin=10, margin_bottom=20)

        def add_option(name):
            self.layout.add(OptionUI.create_group(self, name), fill=True,
                            margin_top=10, margin_bottom=10)

        add_option("netplay_feature")
        add_option("config_feature")