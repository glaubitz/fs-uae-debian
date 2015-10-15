'''OpenGL extension EXT.coordinate_frame

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.coordinate_frame to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows specifying a per-vertex tangent and binormal
	vector in addition to the normal vector, defining a coordinate frame.
	The coordinate frame is used in additional extensions which also build
	on fragment lighting to achieve bump mapping.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/coordinate_frame.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.EXT.coordinate_frame import *
from OpenGL.raw.GL.EXT.coordinate_frame import _EXTENSION_NAME

def glInitCoordinateFrameEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION