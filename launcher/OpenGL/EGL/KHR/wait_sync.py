'''OpenGL extension KHR.wait_sync

This module customises the behaviour of the 
OpenGL.raw.EGL.KHR.wait_sync to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/KHR/wait_sync.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.EGL import _types
from OpenGL.raw.EGL.KHR.wait_sync import *
from OpenGL.raw.EGL.KHR.wait_sync import _EXTENSION_NAME

def glInitWaitSyncKHR():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION