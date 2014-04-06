from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

# import sys
from .common.element import Element, LightElement
from .common.group import Group
from .common.layout import VerticalLayout, HorizontalLayout
from .common.spacer import Spacer
# from .common.signal import Signal

use_qt = True
use_wx = False
toolkit = 'qt'

#if "--wx" in sys.argv:
#    use_wx = True
#    use_qt = False
#    toolkit = 'wx'
#
#if use_qt:

from .qt import *
from .qt.Application import Application
from .qt.Button import Button
from .qt.CheckBox import CheckBox, HeadingCheckBox
from .qt.Color import Color
from .qt.Choice import Choice
from .qt.ComboBox import ComboBox
from .qt.Dialog import Dialog
from .qt.DirDialog import DirDialog
from .qt.FileDialog import FileDialog, pick_directory, pick_file, pick_files
from .qt.HeadingLabel import HeadingLabel
from .qt.Icon import Icon
from .qt.Image import Image
from .qt.ImageButton import ImageButton
from .qt.ImageView import ImageView
from .qt.Label import Label, URLLabel
from .qt.MultilineLabel import MultilineLabel
from .qt.ListView import ListView
from .qt.Menu import Menu
from .qt.Panel import Panel
from .qt.SpinCtrl import SpinCtrl
from .qt.System import System
from .qt.TextArea import TextArea
from .qt.TextField import TextField, PasswordField
from .qt.VerticalItemView import VerticalItemView
from .qt.Window import Window

#if use_wx:
#    # import functions
#    from .wx import *
#
#    # import classes
#    from .wx.Application import Application
#    from .wx.button import Button
#    from .wx.choice import Choice
#    from .wx.CheckBox import CheckBox
#    from .wx.Color import Color
#    from .wx.control import Control
#    from .wx.combobox import ComboBox
#    from .wx.dialog import Dialog
#    from .wx.DirDialog import DirDialog
#    from .wx.filedialog import FileDialog
#    from .wx.itemview import VerticalItemView
#    from .wx.ImageButton import ImageButton
#    from .wx.label import Label, BoldLabel, HeadingLabel
#    from .wx.listview import ListView
#    from .wx.Menu import Menu
#    from .wx.panel import Panel
#    from .wx.separator import Separator
#    from .wx.SpinCtrl import SpinCtrl
#    from .wx.textarea import TextArea
#    from .wx.textfield import TextField
#    from .wx.window import Window
#
#    from .wx.image import Image
#    from .wx.imageview import ImageView
#
#    from .wx.System import System
