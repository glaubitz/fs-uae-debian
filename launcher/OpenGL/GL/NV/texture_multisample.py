'''OpenGL extension NV.texture_multisample

This module customises the behaviour of the 
OpenGL.raw.GL.NV.texture_multisample to provide a more 
Python-friendly API

Overview (from the spec)
	
	This specification extends NV_gpu_program4 to support per-sample fetching
	from multisample textures described in ARB_texture_multisample.
	Specifically, it adds:
	
	  * The TXFMS sample fetch instruction.
	
	  * Texture targets corresponding to the multisample textures added by
	    ARB_texture_multisample.
	
	  * A program option to enable these features.
	
	This specification also extends the ARB_texture_multisample extension
	by adding support for EXT_direct_state_access and VCAA multisample
	coverage with seperate <colorSamples> and <coverageSamples> parameters.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/texture_multisample.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.NV.texture_multisample import *
from OpenGL.raw.GL.NV.texture_multisample import _EXTENSION_NAME

def glInitTextureMultisampleNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION