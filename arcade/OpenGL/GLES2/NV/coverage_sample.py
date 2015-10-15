'''OpenGL extension NV.coverage_sample

This module customises the behaviour of the 
OpenGL.raw.GLES2.NV.coverage_sample to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/coverage_sample.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLES2 import _types
from OpenGL.raw.GLES2.NV.coverage_sample import *
from OpenGL.raw.GLES2.NV.coverage_sample import _EXTENSION_NAME

def glInitCoverageSampleNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION