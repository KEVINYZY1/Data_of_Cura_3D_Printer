'''OpenGL extension ARB.shading_language_100

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.shading_language_100 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension string indicates that the OpenGL Shading Language is
	supported. The Shading Language is defined by a separate specification
	document which can be downloaded from
	
	    http://www.opengl.org/documentation/oglsl.html

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/shading_language_100.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.shading_language_100 import *
### END AUTOGENERATED SECTION