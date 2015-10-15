'''OpenGL extension OES.depth_texture

This module customises the behaviour of the 
OpenGL.raw.GLES2.OES.depth_texture to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/depth_texture.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLES2 import _types
from OpenGL.raw.GLES2.OES.depth_texture import *
from OpenGL.raw.GLES2.OES.depth_texture import _EXTENSION_NAME

def glInitDepthTextureOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION