'''OpenGL extension OES.matrix_palette

This module customises the behaviour of the 
OpenGL.raw.GLES1.OES.matrix_palette to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/matrix_palette.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.OES.matrix_palette import *
from OpenGL.raw.GLES1.OES.matrix_palette import _EXTENSION_NAME

def glInitMatrixPaletteOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glMatrixIndexPointerOES.pointer size not checked against 'size,type,stride'
glMatrixIndexPointerOES=wrapper.wrapper(glMatrixIndexPointerOES).setInputArraySize(
    'pointer', None
)
# INPUT glWeightPointerOES.pointer size not checked against 'type,stride'
glWeightPointerOES=wrapper.wrapper(glWeightPointerOES).setInputArraySize(
    'pointer', None
)
### END AUTOGENERATED SECTION