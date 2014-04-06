from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals


from .helper import DeviceHelper


class DeviceManager(object):

    __instance = None

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = cls("NO_INSTANCES")
        return cls.__instance

    def __init__(self, sentinel="NO_INSTANCES"):
        assert sentinel == "NO_INSTANCES"
        self.helper = DeviceHelper()

    def get_devices(self):
        self.helper.init()
        return self.helper.devices
