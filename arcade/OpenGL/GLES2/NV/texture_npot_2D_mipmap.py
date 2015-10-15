'''OpenGL extension NV.texture_npot_2D_mipmap

This module customises the behaviour of the 
OpenGL.raw.GLES2.NV.texture_npot_2D_mipmap to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/texture_npot_2D_mipmap.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLES2 import _types
from OpenGL.raw.GLES2.NV.texture_npot_2D_mipmap import *
from OpenGL.raw.GLES2.NV.texture_npot_2D_mipmap import _EXTENSION_NAME

def glInitTextureNpot2DMipmapNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION