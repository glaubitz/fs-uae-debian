from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import numpy
from PIL import Image
from fsbc.Application import app
# import .opengl first
from game_center.resources import resources
from game_center.glui.opengl import *


class Texture(object):

    shadow = None
    shadow2 = None
    gloss = None
    screen_gloss = None
    static = None
    default_item = None
    missing_screenshot = None
    missing_cover = None
    logo = None
    top = None
    top_logo = None
    top_logo_selected = None

    add = None
    add_selected = None
    home = None
    home_selected = None
    minimize = None
    minimize_selected = None
    close = None
    close_selected = None
    shutdown = None
    shutdown_selected = None

    bottom_bar = None
    screen_border_1 = None
    screen_border_2 = None
    top_background = None
    top_item = None
    top_item_selected = None
    top_item_left = None
    top_item_left_selected = None
    top_item_right = None
    top_item_arrow = None
    top_item_arrow_selected = None
    
    glow_top = None
    glow_top_left = None
    glow_left = None
    
    sidebar_background_shadow = None

    def __init__(self, name, target=GL_TEXTURE_2D, **kwargs):
        #print(repr(type(name)))
        if isinstance(name, (int, long)):
            self.size = kwargs["size"]
            self.texture = name
        else:
            self.size = [0, 0]
            #print(name, kwargs)
            out_data = {}
            self.texture = self.from_resource(
                name, target=target, size=self.size, out_data=out_data,
                **kwargs)
            self.data = out_data["im_data"]
            self.gl_type = out_data["type"]
        self.w, self.h = self.size
        self.target = target

    def bind(self):
        glBindTexture(self.target, self.texture)

    def render(self, x, y, w, h, z=0.0, opacity=1.0):
        self.bind()
        fs_emu_texturing(True)
        if self.gl_type == GL_RGBA or opacity < 1.0:
            fs_emu_blending(True)
        else:
            fs_emu_blending(False)
        glBegin(GL_QUADS)
        if opacity < 1.0:
            glColor4f(opacity, opacity, opacity, opacity)
        else:
            glColor3f(1.0, 1.0, 1.0)
        glTexCoord(0.0, 1.0)
        glVertex3f(x, y, z)
        glTexCoord(1.0, 1.0)
        glVertex3f(x + w, y, z)
        glTexCoord(1.0, 0.0)
        glVertex3f(x + w, y + h, z)
        glTexCoord(0.0, 0.0)
        glVertex3f(x, y + h, z)
        glEnd()

    @classmethod
    def load(cls, im, mipmap=False, min_filter=None,
             wrap_s=GL_CLAMP_TO_EDGE, wrap_t=GL_CLAMP_TO_EDGE,
             target=GL_TEXTURE_2D, size=None, out_data=None):
        if size is None:
            size = [0, 0]
        type = "RGB"
        gl_type = GL_RGB
        if im.mode == "RGBA":
            # convert to premultiplied alpha
            #pix = im.load()
            #for x in range(im.size[0]):
            #    for y in range(im.size[1]):
            #        r, g, b, a = pix[x, y]
            #        if a:
            #            pix[x, y] = r * 255 // a, g * 255 // a, b * 255 // a, a
            #        else:
            #            pix[x, y] = 0, 0, 0, 0
            a = numpy.fromstring(im.tostring(), dtype=numpy.uint8)
            alpha_layer = a[3::4] / 255.0
            a[0::4] *= alpha_layer
            a[1::4] *= alpha_layer
            a[2::4] *= alpha_layer
            #im = Image.fromstring("RGBA", im.size, a.tostring())
            im_data = a.tostring()
            type = "RGBA"
            gl_type = GL_RGBA
        else:
            im_data = im.tostring("raw", type)
        size[0] = im.size[0]
        size[1] = im.size[1]
        #texture = glGenTextures(1)
        from game_center.glui.render import Render
        texture = Render.create_texture()
        glBindTexture(target, texture)
        glTexImage2D(target, 0, gl_type, im.size[0], im.size[1], 0,
                gl_type, GL_UNSIGNED_BYTE, im_data)
        if mipmap:
            glGenerateMipmap(target)
            if min_filter is None:
                min_filter = GL_LINEAR_MIPMAP_LINEAR
        else:
            if min_filter is None:
                min_filter = GL_LINEAR
        glTexParameteri(target, GL_TEXTURE_MIN_FILTER, min_filter)
        glTexParameteri(target, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(target, GL_TEXTURE_WRAP_S, wrap_s)
        glTexParameteri(target, GL_TEXTURE_WRAP_T, wrap_t)
        if out_data is not None:
            out_data["im_data"] = im_data
            out_data["type"] = gl_type
        return texture

    @classmethod
    def from_resource(cls, name, size=None, **kwargs):
        if size is None:
            size = [0, 0]
        try:
            path = app.data_file(name)
        except LookupError:
            im = resources.resource_pil_image(name)
        else:
            im = Image.open(path)
        return cls.load(im, size=size, **kwargs)
