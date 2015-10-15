'''OpenGL extension ARB.texture_compression_bptc

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_compression_bptc to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides additional texture compression functionality
	specific to the BPTC and BPTC_FLOAT compressed texture formats (called BC7
	and BC6H respectively in Microsoft's DirectX API), subject to all the
	requirements and limitations described by the extension
	GL_ARB_texture_compression.
	
	Traditional block compression methods as typified by s3tc and latc
	compress a block of pixels into indicies along a gradient. This works well
	for smooth images, but can have quality issues along sharp edges and
	strong chrominance transitions. To improve quality in these problematic
	cases, the BPTC formats can divide each block into multiple partitions,
	each of which are compressed using an independent gradient.
	
	In addition, it is desirable to directly support high dynamic range
	imagery in compressed formats, which is accomplished by the BPTC_FLOAT
	formats.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/texture_compression_bptc.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.texture_compression_bptc import *
from OpenGL.raw.GL.ARB.texture_compression_bptc import _EXTENSION_NAME

def glInitTextureCompressionBptcARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION