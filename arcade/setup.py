import os
import sys
if sys.platform == "darwin":
    from setuptools import setup
else:
    from distutils.core import setup


name = "fs-uae-arcade"
title = "FS-UAE Arcade"
py_name = "fs_uae_arcade"
tar_name = "fs-uae-arcade"
version = "2.4.1"
author = "Frode Solheim"
author_email = "frode@fs-uae.net"
package_map = {
    "fsbc": "../python",
    "fsgs": "../python",
    "fsui": "../python",
    "game_center": "../python",
    "lhafile": "../python-lhafile",
    "six": "../python",
}
packages = list(package_map.keys())
scripts = ["fs-uae-arcade"]


setup_packages = set()
package_dir = {}
package_data = {}
setup_options = {}
setup_cmdclass = {}


def add_package(package_name, package_dir_name):
    setup_packages.add(package_name)
    local_name = package_name.replace(".", "/")
    if os.path.exists(local_name):
        package_dir_path = local_name
    else:
        package_dir_path = package_dir_name + "/" + local_name
    package_dir[package_name] = package_dir_path
    package_data[package_name] = []
    for dir_path, dir_names, file_names in os.walk(package_dir_path):
        for name in file_names:
            n, ext = os.path.splitext(name)
            if ext in [".py", ".pyc", ".pyo", ".swp", "*.swo"]:
                continue
            path = os.path.join(dir_path[len(package_dir_path) + 1:], name)
            package_data[package_name].append(path)
            setup_packages.add(package_name)


def add_packages():
    for name in sorted(packages):
        dir_name = package_map[name]
        add_package(name, dir_name)
        for dir_path, dir_names, file_names in os.walk(
                package_dir[name]):
            for n in file_names:
                if n != "__init__.py":
                    continue
                pname_rev = []
                path = dir_path
                while os.path.exists(os.path.join(path, "__init__.py")):
                    pname_rev.append(os.path.basename(path))
                    path = os.path.dirname(path)
                sub_name = ".".join(reversed(pname_rev))
                package_dir[sub_name] = (package_dir[name] + "/" +
                                         sub_name.replace(".", "/"))
                add_package(sub_name, dir_name)


if sys.platform == "win32":
    import py2exe

    try:
        # py2exe 0.6.4 introduced a replacement modulefinder.
        # This means we have to add package paths there, not to the built-in
        # one.  If this new modulefinder gets integrated into Python, then
        # we might be able to revert this some day.
        # if this doesn't work, try import modulefinder
        try:
            import py2exe.mf as modulefinder
        except ImportError:
            import modulefinder
        import win32com, sys
        for p in win32com.__path__[1:]:
            modulefinder.AddPackagePath("win32com", p)
        for extra in ["win32com.shell"]:  # ,"win32com.mapi"
            __import__(extra)
            m = sys.modules[extra]
            for p in m.__path__[1:]:
                modulefinder.AddPackagePath(extra, p)
    except ImportError:
        # no build path setup, no worries.
        pass

    origIsSystemDLL = py2exe.build_exe.isSystemDLL

    def isSystemDLL(pathname):
        # checks if the freetype and ogg dll files are being included
        if os.path.basename(pathname).lower() in [
                "libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll"]:
            return 0
        return origIsSystemDLL(pathname)

    py2exe.build_exe.isSystemDLL = isSystemDLL

    py2exe_options = {
        "dll_excludes": ["MSVCP90.dll"],
        "includes": [
            "ctypes",
            "logging",
        ],
        "excludes": [
            "Tkconstants",
            "Tkinter",
            "tcl",
        ],
    }

    from py2exe.build_exe import py2exe as build_exe

    class BuildExe(build_exe):

        def copy_extensions(self, extensions):
            build_exe.copy_extensions(self, extensions)

            res_dirs = []
            res_dirs.append('fsbc/res')
            res_dirs.append('fsgs/res')
            res_dirs.append('fsui/res')
            res_dirs.append('game_center/res')
            res_dirs.append('lhafile/res')
            res_dirs.append('six/res')

            for res_dir in res_dirs:
                full = os.path.join(self.collect_dir, res_dir)
                if not os.path.exists(full):
                    self.mkpath(full)
                for dir_path, dir_names, file_names in os.walk(res_dir):
                    for name in file_names:
                        src = os.path.join(dir_path, name)
                        dst = os.path.join(full, src[len(res_dir) + 1:])
                        print(src, dst)
                        if not os.path.exists(os.path.dirname(dst)):
                            os.makedirs(os.path.dirname(dst))
                        self.copy_file(src, dst)
                        self.compiled_files.append(src)

    setup_options["py2exe"] = py2exe_options
    setup_cmdclass["py2exe"] = BuildExe

if sys.platform == "darwin":
    py2app_options = {
        "argv_emulation": True,
    }

    setup_options["py2app"] = py2app_options

add_packages()

setup_kwargs = {
    "name": py_name,
    "version": version,
    "author": author,
    "author_email": author_email,
    "packages": setup_packages,
    "package_dir": package_dir,
    "package_data": package_data,
    "options": setup_options,
    "cmdclass": setup_cmdclass,
}

if sys.platform == "win32":
    setup_kwargs["windows"] = scripts

if sys.platform == "darwin":
    # faking version right now because a simpler version format is needed,
    # FIXME: retrieve major.minor.revision from actual version number
    setup_kwargs["name"] = title
    setup_kwargs["version"] = "2.4.1"
    setup_kwargs["app"] = [name]
    py2app_options["packages"] = ",".join(packages)
else:
    setup_kwargs["scripts"] = scripts

setup(**setup_kwargs)
