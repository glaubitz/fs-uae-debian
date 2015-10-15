'''OpenGL extension NV.texgen_reflection

This module customises the behaviour of the 
OpenGL.raw.GL.NV.texgen_reflection to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides two new texture coordinate generation modes
	that are useful texture-based lighting and environment mapping.
	The reflection map mode generates texture coordinates (s,t,r)
	matching the vertex's eye-space reflection vector.  The reflection
	map mode is useful for environment mapping without the singularity
	inherent in sphere mapping.  The normal map mode generates texture
	coordinates (s,t,r) matching the vertex's transformed eye-space
	normal.  The normal map mode is useful for sophisticated cube map
	texturing-based diffuse lighting models.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/texgen_reflection.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.NV.texgen_reflection import *
from OpenGL.raw.GL.NV.texgen_reflection import _EXTENSION_NAME

def glInitTexgenReflectionNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION