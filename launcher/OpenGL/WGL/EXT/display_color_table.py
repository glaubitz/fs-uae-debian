'''OpenGL extension EXT.display_color_table

This module customises the behaviour of the 
OpenGL.raw.WGL.EXT.display_color_table to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/display_color_table.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.WGL import _types
from OpenGL.raw.WGL.EXT.display_color_table import *
from OpenGL.raw.WGL.EXT.display_color_table import _EXTENSION_NAME

def glInitDisplayColorTableEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION