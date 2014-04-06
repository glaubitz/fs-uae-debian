from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from .wxpython import wx
from .Application import Application, require_wx_app


def call_after(function):
    #Application.get_instance().run_in_main(function)
    require_wx_app()
    wx.CallAfter(function)


def call_later(ms, function):
    require_wx_app()
    wx.CallLater(ms, function)


def show_error(message):
    require_wx_app()
    wx.MessageBox(message, "Error", wx.ICON_ERROR)


def get_screen_size():
    require_wx_app()
    return wx.GetDisplaySize()


def get_background_color():
    require_wx_app()
    c = wx.SystemSettings_GetColour(wx.SYS_COLOUR_BTNFACE)
    from .Color import Color
    return Color(c)
