'''OpenGL extension ARB.texture_non_power_of_two

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_non_power_of_two to provide a more 
Python-friendly API

Overview (from the spec)
	
	Conventional OpenGL texturing is limited to images with
	power-of-two dimensions and an optional 1-texel border.
	ARB_texture_non_power_of_two extension relaxes the size restrictions
	for the 1D, 2D, cube map, and 3D texture targets.
	
	There is no additional procedural or enumerant api introduced by this
	extension except that an implementation which exports the extension
	string will allow an application to pass in texture dimensions for
	the 1D, 2D, cube map, and 3D targets that may or may not be a power
	of two.
	
	An implementation which supports relaxing traditional GL's
	power-of-two size restrictions across all texture targets will export
	the extension string: "ARB_texture_non_power_of_two".
	
	When this extension is supported, mipmapping, automatic mipmap
	generation, and all the conventional wrap modes are supported for
	non-power-of-two textures

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/texture_non_power_of_two.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.texture_non_power_of_two import *
from OpenGL.raw.GL.ARB.texture_non_power_of_two import _EXTENSION_NAME

def glInitTextureNonPowerOfTwoARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION