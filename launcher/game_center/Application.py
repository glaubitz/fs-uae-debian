from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import os
from fsbc.Application import Application as BaseApplication
from fsgs.application import ApplicationMixin
from game_center import Paths


class Application(ApplicationMixin, BaseApplication):

    instance = None
    name = None

    @classmethod
    def init(cls, name):
        cls.name = name

    def __init__(self):
        BaseApplication.__init__(self)
        #assert name

    def get_config_dir(self):
        path = os.path.join(Paths.get_config_dir(), self.name)
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def get_data_dir(self):
        path = os.path.join(Paths.get_data_dir(), self.name)
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def get_cache_dir(self):
        path = os.path.join(Paths.get_cache_dir(), self.name)
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def get_config_path(self, name):
        return os.path.join(self.get_config_dir(), name)

    def get_data_path(self, name):
        return os.path.join(self.get_data_dir(), name)

    def get_cache_path(self, name):
        return os.path.join(self.get_cache_dir(), name)

    def is_stopping(self):
        return self.stop_flag
