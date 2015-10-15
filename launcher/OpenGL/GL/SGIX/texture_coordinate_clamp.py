'''OpenGL extension SGIX.texture_coordinate_clamp

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.texture_coordinate_clamp to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a mechanism to specify the maximum texture coordinate
	clamping values. Standard OpenGL always clamps the upper bound to 1.0 when
	the wrap mode is set to CLAMP. This mechanism can be used to  guarantee 
	that non-existent texel data will not be accessed when the texture image has 
	dimensions that are not a power of 2.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIX/texture_coordinate_clamp.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.SGIX.texture_coordinate_clamp import *
from OpenGL.raw.GL.SGIX.texture_coordinate_clamp import _EXTENSION_NAME

def glInitTextureCoordinateClampSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION