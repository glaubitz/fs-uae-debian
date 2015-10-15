'''OpenGL extension SGIS.texture_edge_clamp

This module customises the behaviour of the 
OpenGL.raw.GL.SGIS.texture_edge_clamp to provide a more 
Python-friendly API

Overview (from the spec)
	
	The base OpenGL provides clamping such that the texture coordinates are
	limited to exactly the range [0,1].  When a texture coordinate is
	clamped using this algorithm, the texture sampling filter straddles the
	edge of the texture image, taking 1/2 its sample values from within the
	texture image, and the other 1/2 from the texture border.  It is
	sometimes desirable to clamp a texture without requiring a border, and
	without using the constant border color.
	
	This extension defines a new texture clamping algorithm.
	CLAMP_TO_EDGE_SGIS clamps texture coordinates at all mipmap levels such
	that the texture filter never samples a border texel.  When used with a
	NEAREST or a LINEAR filter, the color returned when clamping is derived
	only from texels at the edge of the texture image.  When used with
	FILTER4 filters, the filter operations of CLAMP_TO_EDGE_SGIS are defined
	but don't result in a nice clamp-to-edge color.
	
	CLAMP_TO_EDGE_SGIS is supported by 1, 2, and 3-dimensional textures
	only.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIS/texture_edge_clamp.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.SGIS.texture_edge_clamp import *
from OpenGL.raw.GL.SGIS.texture_edge_clamp import _EXTENSION_NAME

def glInitTextureEdgeClampSGIS():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION