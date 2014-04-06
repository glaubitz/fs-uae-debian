from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import subprocess
from fsbc.system import windows, macosx
from fsbc.Application import Application

try:
    getcwd = os.getcwdu
except AttributeError:
    getcwd = os.getcwd


class FSUAEDeviceHelper(object):

    @classmethod
    def start_with_args(cls, args, **kwargs):
        print("FSUAE.start_with_args:", args)
        exe = cls.find_executable()
        print("current dir (cwd): ", getcwd())
        print("using fs-uae executable:", exe)
        args = [exe] + args
        print(args)

        proc = subprocess.Popen(args, **kwargs)
        return proc

    @classmethod
    def find_executable(cls):
        application = Application.instance()

        if os.path.isdir("../fs-uae/src"):
            # running FS-UAE Launcher from source directory, we
            # then want to run the locally compiled fs-uae binary
            path = "../fs-uae/fs-uae-device-helper"
            if windows:
                path += ".exe"
            if os.path.isfile(path):
                return path
            raise Exception("Could not find development FS-UAE "
                            "device helper executable")

        if windows:
            exe = os.path.join(
                application.executable_dir(),
                "fs-uae/fs-uae-device-helper.exe")
            if not os.path.exists(exe):
                exe = os.path.join(
                    application.executable_dir(),
                    "../fs-uae-device-helper.exe")
        elif macosx:
            exe = os.path.join(
                application.executable_dir(),
                "../FS-UAE.app/Contents/MacOS/fs-uae-device-helper")
            if not os.path.exists(exe):
                exe = os.path.join(
                    application.executable_dir(),
                    "../../../FS-UAE.app/Contents/MacOS/fs-uae-device-helper")
            if not os.path.exists(exe):
                exe = os.path.join(
                    application.executable_dir(),
                    "../../../Programs/Mac OS X/FS-UAE"
                    ".app/Contents/MacOS/fs-uae-device-helper")
            if not os.path.exists(exe):
                exe = os.path.join(
                    application.executable_dir(),
                    "../../../FS-UAE Launcher.app/Contents/Resources/"
                    "FS-UAE.app/Contents/MacOS/fs-uae-device-helper")
        else:
            return "fs-uae-device-helper"

        if not os.path.exists(exe):
            raise Exception("Could not find fs-uae-device-helper executable")
        return exe
