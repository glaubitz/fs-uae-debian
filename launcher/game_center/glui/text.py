from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import numpy
import pygame
import pygame.image


class TextRenderer(object):

    def __init__(self, font):
        self.font = font

    # @staticmethod
    # def BLUR(inarray):
    #     return convolution_filter(inarray, BLUR_FILTER[0], BLUR_FILTER[1])

    def render_text(self, text, color):
        #color = (255, 255, 255)
        rendered = self.font.render(text, True, color)
        # if filter:
        #     rendered = apply_filter(rendered, filter)
        txt_size = rendered.get_size()
        txt_data = pygame.image.tostring(rendered, "RGBA", 1)
        
        # convert to premultipled alpha
        a = numpy.fromstring(txt_data, dtype=numpy.uint8)
        alpha_layer = a[3::4] / 255.0
        a[0::4] *= alpha_layer
        a[1::4] *= alpha_layer
        a[2::4] *= alpha_layer
        #im = Image.fromstring("RGBA", im.size, a.tostring())
        
        #return txt_data, txt_size
        return a.tostring(), txt_size

    def get_size(self, text):
        return self.font.size(text)
