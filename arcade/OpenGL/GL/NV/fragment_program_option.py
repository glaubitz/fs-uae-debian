'''OpenGL extension NV.fragment_program_option

This module customises the behaviour of the 
OpenGL.raw.GL.NV.fragment_program_option to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides additional fragment program functionality
	to extend the standard ARB_fragment_program language and execution
	environment.  ARB programs wishing to use this added functionality
	need only add:
	
	    OPTION NV_fragment_program;
	
	to the beginning of their fragment programs.
	
	The functionality provided by this extension, which is roughly
	equivalent to that provided by the NV_fragment_program extension,
	includes:
	
	  * increased control over precision in arithmetic computations and
	    storage,
	
	  * data-dependent conditional writemasks,
	
	  * an absolute value operator on scalar and swizzled operand loads,
	
	  * instructions to compute partial derivatives, and perform texture
	    lookups using specified partial derivatives,
	
	  * fully orthogonal "set on" instructions,
	
	  * instructions to compute reflection vector and perform a 2D
	    coordinate transform, and
	
	  * instructions to pack and unpack multiple quantities into a single
	    component.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/fragment_program_option.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.NV.fragment_program_option import *
from OpenGL.raw.GL.NV.fragment_program_option import _EXTENSION_NAME

def glInitFragmentProgramOptionNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION