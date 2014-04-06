from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from fsbc.system import windows


if windows:
    #noinspection PyUnresolvedReferences
    from pygame.locals import *
    from ctypes import windll
    user32 = windll.user32
    ShowWindow = user32.ShowWindow
    IsZoomed = user32.IsZoomed
    IsIconic = user32.IsIconic
    SW_MAXIMIZE = 3
    SW_MINIMIZE = 6
    SW_RESTORE = 9

    #noinspection PyPep8Naming
    def getSDLWindow():
        import pygame
        return pygame.display.get_wm_info()["window"]

    #noinspection PyPep8Naming
    def SDL_Maximize():
        return ShowWindow(getSDLWindow(), SW_MAXIMIZE)

    #noinspection PyPep8Naming
    def SDL_Restore():
        return ShowWindow(getSDLWindow(), SW_RESTORE)

    #noinspection PyPep8Naming
    def SDL_Minimize():
        return ShowWindow(getSDLWindow(), SW_MINIMIZE)

    #noinspection PyPep8Naming
    def SDL_IsMaximized():
        return IsZoomed(getSDLWindow())

    #noinspection PyPep8Naming
    def SDL_IsMinimized():
        return IsIconic(getSDLWindow())
else:
    #noinspection PyPep8Naming
    def SDL_Maximize():
        pass

    #noinspection PyPep8Naming
    def SDL_Restore():
        pass

    #noinspection PyPep8Naming
    def SDL_Minimize():
        pass

    #noinspection PyPep8Naming
    def SDL_IsMaximized():
        return False

    #noinspection PyPep8Naming
    def SDL_IsMinimized():
        return False
