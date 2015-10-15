'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_APPLE_element_array'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_APPLE_element_array',error_checker=_errors._error_checker)
GL_ELEMENT_ARRAY_APPLE=_C('GL_ELEMENT_ARRAY_APPLE',0x8A0C)
GL_ELEMENT_ARRAY_POINTER_APPLE=_C('GL_ELEMENT_ARRAY_POINTER_APPLE',0x8A0E)
GL_ELEMENT_ARRAY_TYPE_APPLE=_C('GL_ELEMENT_ARRAY_TYPE_APPLE',0x8A0D)
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLsizei)
def glDrawElementArrayAPPLE(mode,first,count):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLint,_cs.GLsizei)
def glDrawRangeElementArrayAPPLE(mode,start,end,first,count):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.c_void_p)
def glElementPointerAPPLE(type,pointer):pass
# Calculate length of pointer from type:ElementPointerTypeATI
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray,arrays.GLsizeiArray,_cs.GLsizei)
def glMultiDrawElementArrayAPPLE(mode,first,count,primcount):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,arrays.GLintArray,arrays.GLsizeiArray,_cs.GLsizei)
def glMultiDrawRangeElementArrayAPPLE(mode,start,end,first,count,primcount):pass
