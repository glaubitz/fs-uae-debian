from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import re
import traceback
import subprocess
# from .I18N import _
# from .Settings import Settings
# from .Signal import Signal
from fsgs.amiga.FSUAEDeviceHelper import FSUAEDeviceHelper
from .device import Device

# def create_cmp_id(id):
#     return id.lower().replace(" ", "")


class DeviceHelper(object):

    initialized = False
    devices = []
    #device_ids = []
    #device_names = []
    #device_types = []
    #device_name_count = {}

    #joystick_data = {}

    #@classmethod
    #def joystick_buttons(cls, device):
    #    return cls.joystick_data[device][0]
    #
    #    return cls.joystick_data[device][1]
    #
    #@classmethod
    #def joystick_hats(cls, device):
    #@classmethod
    #def joystick_axes(cls, device):
    #    return cls.joystick_data[device][2]
    #
    #@classmethod
    #def joystick_balls(cls, device):
    #    return cls.joystick_data[device][3]

    def __init__(self):
        self.devices = []
        self.joystick_devices = []
        self.keyboard_devices = []
        self.joystick_like_devices = []
        self.initialized = False

    def update(self):
        # if cls.initialized:
        #     return
        # init can be called more than once (by setting initialized to
        # false, used by refresh function, so we need to clear the lists...
        self.devices = []
        self.joystick_devices = []
        self.keyboard_devices = []
        self.joystick_like_devices = []
        self.init_fsuae()

    def init(self):
        if self.initialized:
            return
        self.init_fsuae()
        self.initialized = True

    #def refresh(self):
    #    self.initialized = False
    #    self.init()
    #    # Signal.broadcast("device_list_updated")

    def init_fsuae(self):
        print("finding connected joysticks")
        try:
            p = FSUAEDeviceHelper.start_with_args(
                ["list"], stdout=subprocess.PIPE)
            joysticks = p.stdout.read()
            p.wait()
        except Exception:
            print("exception while listing joysticks and devices")
            traceback.print_exc()
            return
        print(repr(joysticks))
        # If the character conversion failes, replace will ensure that
        # as much as possible succeeds. The joystick in question will
        # not be pre-selectable in the launcher, but the other ones will
        # work at least.
        joysticks = joysticks.decode("UTF-8", "replace")
        joysticks = [x.strip() for x in joysticks.split("\n") if x.strip()]

        # joysticks.append("J: controller xbox 360 for windows")
        # joysticks.append("Buttons: 10 Hats: 1 Axes: 5 Balls: 0")

        device_name_count = {}
        last_joystick = None

        for line in joysticks:
            if line.startswith("#"):
                continue
            if line.startswith("Buttons:"):
                parts = line.split(" ")
                last_joystick.buttons = int(parts[1])
                last_joystick.hats = int(parts[3])
                last_joystick.axes = int(parts[5])
                last_joystick.balls = int(parts[7])
                continue

            device = Device()
            device_type, name = line.split(" ", 1)

            name_count = device_name_count.get(name, 0) + 1
            device_name_count[name] = name_count
            if name_count > 1:
                name = name + " #" + str(name_count)
            device.id = name
            name = re.sub("[ ]+", " ", name)
            device.name = name
            if device_type == "J:":
                device.type = "joystick"
                last_joystick = device
                self.joystick_devices.append(device)
            elif device_type == "M:":
                device.type = "mouse"
            elif device_type == "K:":
                # works as an emulated joystick...
                # device_type = "joystick"
                device.type = "keyboard"
                self.keyboard_devices.append(device)
            #self.device_types.append(device_type)
            self.devices.append(device)
        for i, device in enumerate(self.joystick_devices):
            device.index = i
        for i, device in enumerate(self.keyboard_devices):
            device.index = i
        self.joystick_like_devices.extend(self.joystick_devices)
        self.joystick_like_devices.extend(self.keyboard_devices)

    def default_port_selection(self, ports):
        print("devices:")
        self.init()
        # for device in self.devices:
        #     print(" #", device.id)
        #     device.configure("megadrive")

        joystick_like_devices = self.joystick_like_devices[:]

        print("ports:")
        for port in ports:
            for i, device in enumerate(joystick_like_devices):
                # device.configure()
                if True:
                    joystick_like_devices.pop(i)
                    port.device = device
                    break

            #if len(joystick_like_devices) > 0:
            #    device = joystick_like_devices[0]
            #
            #
            #    if True:
            #    port.device = joystick_like_devices.pop(0)
            print(" /", port.name, port.device)

    #@classmethod
    #def get_joystick_names(cls):
    #    cls.init()
    #    return cls.device_names[:]
    #
    #@classmethod
    #def get_device_type(cls, device):
    #    cls.init()
    #    for i in range(len(cls.device_names)):
    #        if cls.device_names[i] == device:
    #            return cls.device_types[i]
    #    return ""
    #
    #@classmethod
    #def is_joystick(cls, device):
    #    return cls.get_device_type(device) == "joystick"
    #
    #@classmethod
    #def get_joystick_ids(cls):
    #    cls.init()
    #    return cls.device_ids[:]
