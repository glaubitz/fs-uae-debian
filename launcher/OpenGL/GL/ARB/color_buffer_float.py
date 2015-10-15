'''OpenGL extension ARB.color_buffer_float

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.color_buffer_float to provide a more 
Python-friendly API

Overview (from the spec)
	
	The standard OpenGL pipeline is based on a fixed-point pipeline.
	While color components are nominally floating-point values in the
	pipeline, components are frequently clamped to the range [0,1] to
	accomodate the fixed-point color buffer representation and allow
	for fixed-point computational hardware.
	
	This extension adds pixel formats or visuals with floating-point
	RGBA color components and controls for clamping of color
	components within the pipeline.
	
	For a floating-point RGBA pixel format, the size of each float
	components is specified using the same attributes that are used
	for defining the size of fixed-point components.  32-bit
	floating-point components are in the standard IEEE float format.
	16-bit floating-point components have 1 sign bit, 5 exponent bits,
	and 10 mantissa bits.
	
	Clamping control provides a way to disable certain color clamps
	and allow programs, and the fixed-function pipeline, to deal in
	unclamped colors.  There are controls to modify clamping of vertex
	colors, clamping of fragment colors throughout the pipeline, and
	for pixel return data.
	
	The default state for fragment clamping is "FIXED_ONLY", which
	has the behavior of clamping colors for fixed-point color buffers
	and not clamping colors for floating-pont color buffers.
	
	Vertex colors are clamped by default.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/color_buffer_float.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ARB.color_buffer_float import *
from OpenGL.raw.GL.ARB.color_buffer_float import _EXTENSION_NAME

def glInitColorBufferFloatARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION
from OpenGL.GL import glget
glget.addGLGetConstant( GL_RGBA_FLOAT_MODE_ARB, (1,) )