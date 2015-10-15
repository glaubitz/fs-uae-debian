'''OpenGL extension NVX.gpu_memory_info

This module customises the behaviour of the 
OpenGL.raw.GL.NVX.gpu_memory_info to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NVX/gpu_memory_info.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.NVX.gpu_memory_info import *
from OpenGL.raw.GL.NVX.gpu_memory_info import _EXTENSION_NAME

def glInitGpuMemoryInfoNVX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION