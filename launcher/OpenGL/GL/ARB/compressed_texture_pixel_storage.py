'''OpenGL extension ARB.compressed_texture_pixel_storage

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.compressed_texture_pixel_storage to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension expands the functionality of the PixelStore modes
	to allow UNPACK_ROW_LENGTH, UNPACK_SKIP_ROWS, UNPACK_SKIP_PIXELS,
	UNPACK_IMAGE_HEIGHT and UNPACK_SKIP_IMAGES to affect the operation of
	CompressedTexImage*D and CompressedTexSubImage*D. Similarly, it 
	also allows PACK_ROW_LENGTH, PACK_SKIP_ROWS, PACK_SKIP_PIXELS, 
	PACK_IMAGE_HEIGHT and PACK_SKIP_IMAGES to affect the operation of 
	GetCompressedTexImage*D. This allows data to be transferred
	to or from a specified sub-rectangle of a larger compressed image.
	
	This extension is designed primarily to support compressed image
	formats with fixed-size blocks. To use this new mechanism, an 
	application should program new parameters UNPACK_COMPRESSED_BLOCK_
	{WIDTH,HEIGHT,DEPTH,SIZE} to indicate the number of texels in each
	dimension of the fixed-size block as well as the number of bytes
	consumed by each block. These parameters, in addition to the 
	existing PixelStore parameters, are used to identify a collection 
	of bytes in client memory or a buffer object's data store to use
	as compressed texture data. This operation is unlikely to have 
	the desired results if the client programs a block size inconsistent
	with the underlying compressed image format, or if the compressed
	image format has variable-sized blocks.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/compressed_texture_pixel_storage.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.compressed_texture_pixel_storage import *
from OpenGL.raw.GL.ARB.compressed_texture_pixel_storage import _EXTENSION_NAME

def glInitCompressedTexturePixelStorageARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION