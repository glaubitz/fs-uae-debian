'''OpenGL extension ARB.fragment_shader

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.fragment_shader to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds functionality to define fragment shader objects. A
	fragment shader object is a shader object (see the ARB_shader_objects
	extension) that, when attached to a program object, can be compiled and
	linked to produce an executable that runs on the fragment processor in
	OpenGL. The fragment processor is a programmable unit that replaces the
	OpenGL 1.4 fixed-function texturing, color sum and fog stages. This
	extension also defines how such an executable interacts with the fixed
	functionality fragment processing of OpenGL 1.4. The language used to
	write fragment shaders is not discussed here. That language is defined
	in the OpenGL Shading Language specification as the Fragment Shading
	Language.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/fragment_shader.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.fragment_shader import *
from OpenGL.raw.GL.ARB.fragment_shader import _EXTENSION_NAME

def glInitFragmentShaderARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION