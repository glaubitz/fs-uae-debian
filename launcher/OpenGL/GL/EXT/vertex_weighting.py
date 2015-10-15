'''OpenGL extension EXT.vertex_weighting

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.vertex_weighting to provide a more 
Python-friendly API

Overview (from the spec)
	
	The intent of this extension is to provide a means for blending
	geometry based on two slightly differing modelview matrices.
	The blending is based on a vertex weighting that can change on a
	per-vertex basis.  This provides a primitive form of skinning.
	
	A second modelview matrix transform is introduced.  When vertex
	weighting is enabled, the incoming vertex object coordinates are
	transformed by both the primary and secondary modelview matrices;
	likewise, the incoming normal coordinates are transformed by the
	inverses of both the primary and secondary modelview matrices.
	The resulting two position coordinates and two normal coordinates
	are blended based on the per-vertex vertex weight and then combined
	by addition.  The transformed, weighted, and combined vertex position
	and normal are then used by OpenGL as the eye-space position and
	normal for lighting, texture coordinate, generation, clipping,
	and further vertex transformation.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/vertex_weighting.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.EXT.vertex_weighting import *
from OpenGL.raw.GL.EXT.vertex_weighting import _EXTENSION_NAME

def glInitVertexWeightingEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION