version = $(strip $(shell cat ../../VERSION))
arch = $(strip $(shell python3 ../arch.py))
ver_os_arch = $(version)_macos_$(arch)

dname = fs-uae-arcade_$(ver_os_arch)
macos =  Launcher.app/Contents/MacOS
frameworks = Launcher.app/Contents/Frameworks
resources = Launcher.app/Contents/Resources
locale = Launcher.app/Contents/Locale
pylib = /Library/Frameworks/Python.framework/Versions/3.6/lib
qtdir = $(pylib)/python3.6/site-packages/PyQt5/Qt

all: bindist-launcher

clean:
	rm -Rf Launcher.app "FS-UAE Arcade.app"

cxfreeze: clean
	make -C ../..
	rm -Rf ../../build
	ln -fs $(qtdir)/lib/Qt*.framework $(pylib)
	cd ../.. && PYTHONHASHSEED=1 python3 setup.py build_exe
	rm  $(pylib)/Qt*.framework

	mkdir -p $(macos)
	mkdir -p $(resources)
	cp ../../cacert.pem $(macos) || \
		cp ../../../fs-uae-launcher/cacert.pem $(macos)
	rm -Rf $(resources)/applications
	rm -Rf $(resources)/icons
	mv ../../build/*/* $(macos)

	rm -Rf $(macos)/Qt*

addqt:
	mkdir -p Launcher.app/Contents/PlugIns/platforms
	cp $(qtdir)/plugins/platforms/libqcocoa.dylib Launcher.app/Contents/PlugIns/platforms/

	mkdir -p Launcher.app/Contents/PlugIns/imageformats
	cp $(qtdir)/plugins/imageformats/libqgif.dylib Launcher.app/Contents/PlugIns/imageformats/
	cp $(qtdir)/plugins/imageformats/libqicns.dylib Launcher.app/Contents/PlugIns/imageformats/
	cp $(qtdir)/plugins/imageformats/libqjpeg.dylib Launcher.app/Contents/PlugIns/imageformats/

	mkdir -p $(frameworks)
	cp -r $(qtdir)/lib/QtCore.framework $(frameworks)/
	cp -r $(qtdir)/lib/QtGui.framework $(frameworks)/
	cp -r $(qtdir)/lib/QtWidgets.framework $(frameworks)/
	cp -r $(qtdir)/lib/QtOpenGL.framework $(frameworks)/
	cp -r $(qtdir)/lib/QtDBus.framework $(frameworks)/
	cp -r $(qtdir)/lib/QtPrintSupport.framework $(frameworks)/

launcher: cxfreeze addqt
	find Launcher.app -name *_debug.dylib -delete

	rm -Rf $(macos)/imageformats
	rm -Rf $(macos)/platforms

	rm -f $(macos)/PyQt5.QtNetwork.so
	rm -f $(macos)/PyQt5.QtQml.so
	rm -f $(macos)/PyQt5.QtQuick.so

	python3 standalone.py Launcher.app

	# rm -f $(macos)/libncursesw.5.dylib

	cp Info.plist Launcher.app/Contents/
	cp ../../icon/fs-uae-arcade.icns $(resources)/fs-uae-arcade.icns

	make -C ../python

	rm -Rf $(macos)/arcade
	rm -Rf $(macos)/fsbc
	rm -Rf $(macos)/fsgs
	rm -Rf $(macos)/fspy
	rm -Rf $(macos)/fstd
	rm -Rf $(macos)/fsui
	rm -Rf $(macos)/launcher
	rm -Rf $(macos)/OpenGL
	rm -Rf $(macos)/oyoyo
	rm -Rf $(macos)/workspace

	zip -d $(macos)/library.zip arcade/\*
	zip -d $(macos)/library.zip fsbc/\*
	zip -d $(macos)/library.zip fsgs/\*
	zip -d $(macos)/library.zip fspy/\*
	zip -d $(macos)/library.zip fstd/\*
	zip -d $(macos)/library.zip fsui/\*
	zip -d $(macos)/library.zip launcher/\*
	zip -d $(macos)/library.zip OpenGL/\*
	zip -d $(macos)/library.zip oyoyo/\*
	zip -d $(macos)/library.zip workspace/\*

	# This file differs between each build
	zip -d $(macos)/library.zip BUILD_CONSTANTS.pyc
	# Remove wrong-cased members from the archive
	zip -d $(macos)/library.zip ConfigParser.pyc || true
	zip -d $(macos)/library.zip Queue.pyc || true
	PYTHONPATH=../..:../../../fs-uae-launcher \
		python3 -m fspy.zipfile deterministic \
		--fix-pyc-timestamps $(macos)/library.zip

	mkdir -p Launcher.app/Contents/Python
	cp -a ../python/*.zip Launcher.app/Contents/Python/

bindist-launcher: launcher
	rm -Rf "FS-UAE Arcade.app"
	mv Launcher.app "FS-UAE Arcade.app"
	# python3 sign.py "FS-UAE Arcade.app"
	GZIP=-9 tar Jcfv ../../$(dname).tar.xz "FS-UAE Arcade.app"
