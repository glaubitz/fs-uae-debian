from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals


class Config(object):
    
    @classmethod
    def get(cls, key, default=None):
        return default

    @classmethod
    def get_bool(cls, key, default):
        return default

    @classmethod
    def get_int(cls, key, default):
        return default
