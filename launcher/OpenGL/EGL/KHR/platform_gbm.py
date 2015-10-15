'''OpenGL extension KHR.platform_gbm

This module customises the behaviour of the 
OpenGL.raw.EGL.KHR.platform_gbm to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/KHR/platform_gbm.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.EGL import _types
from OpenGL.raw.EGL.KHR.platform_gbm import *
from OpenGL.raw.EGL.KHR.platform_gbm import _EXTENSION_NAME

def glInitPlatformGbmKHR():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION