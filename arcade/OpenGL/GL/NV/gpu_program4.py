'''OpenGL extension NV.gpu_program4

This module customises the behaviour of the 
OpenGL.raw.GL.NV.gpu_program4 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This specification documents the common instruction set and basic
	functionality provided by NVIDIA's 4th generation of assembly instruction
	sets supporting programmable graphics pipeline stages.  
	
	The instruction set builds upon the basic framework provided by the
	ARB_vertex_program and ARB_fragment_program extensions to expose
	considerably more capable hardware.  In addition to new capabilities for
	vertex and fragment programs, this extension provides a new program type
	(geometry programs) further described in the NV_geometry_program4
	specification.
	
	NV_gpu_program4 provides a unified instruction set -- all instruction set
	features are available for all program types, except for a small number of
	features that make sense only for a specific program type.  It provides
	fully capable signed and unsigned integer data types, along with a set of
	arithmetic, logical, and data type conversion instructions capable of
	operating on integers.  It also provides a uniform set of structured
	branching constructs (if tests, loops, and subroutines) that fully support
	run-time condition testing.
	
	This extension provides several new texture mapping capabilities.  Shadow
	cube maps are supported, where cube map faces can encode depth values.
	Texture lookup instructions can include an immediate texel offset, which
	can assist in advanced filtering.  New instructions are provided to fetch
	a single texel by address in a texture map (TXF) and query the size of a
	specified texture level (TXQ).
	
	By and large, vertex and fragment programs written to ARB_vertex_program
	and ARB_fragment_program can be ported directly by simply changing the
	program header from "!!ARBvp1.0" or "!!ARBfp1.0" to "!!NVvp4.0" or
	"!!NVfp4.0", and then modifying the code to take advantage of the expanded
	feature set.  There are a small number of areas where this extension is
	not a functional superset of previous vertex program extensions, which are
	documented in this specification.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/gpu_program4.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.NV.gpu_program4 import *
from OpenGL.raw.GL.NV.gpu_program4 import _EXTENSION_NAME

def glInitGpuProgram4NV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION