'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_vertex_program4'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_vertex_program4',error_checker=_errors._error_checker)
GL_VERTEX_ATTRIB_ARRAY_INTEGER_NV=_C('GL_VERTEX_ATTRIB_ARRAY_INTEGER_NV',0x88FD)
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVertexAttribIivEXT(index,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetVertexAttribIuivEXT(index,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint)
def glVertexAttribI1iEXT(index,x):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttribI1ivEXT(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glVertexAttribI1uiEXT(index,x):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttribI1uivEXT(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint)
def glVertexAttribI2iEXT(index,x,y):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttribI2ivEXT(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glVertexAttribI2uiEXT(index,x,y):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttribI2uivEXT(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint)
def glVertexAttribI3iEXT(index,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttribI3ivEXT(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glVertexAttribI3uiEXT(index,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttribI3uivEXT(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLbyteArray)
def glVertexAttribI4bvEXT(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glVertexAttribI4iEXT(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttribI4ivEXT(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLshortArray)
def glVertexAttribI4svEXT(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLubyteArray)
def glVertexAttribI4ubvEXT(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glVertexAttribI4uiEXT(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttribI4uivEXT(index,v):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLushortArray)
def glVertexAttribI4usvEXT(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glVertexAttribIPointerEXT(index,size,type,stride,pointer):pass
# Calculate length of pointer from type:VertexAttribEnum
