version = $(strip $(shell cat ../VERSION))

all: bindist-launcher

clean:
	rm -Rf ../macosx/fs-uae-launcher*

launcher:
	make -C ..
	rm -Rf fs-uae-launcher_$(version)_macosx	
	mkdir -p fs-uae-launcher_$(version)_macosx
	cd .. && python2.7 setup.py py2app --iconfile icon/fs-uae-launcher.icns
	mv ../dist/"FS-UAE Launcher.app" fs-uae-launcher_$(version)_macosx/
	cp -pPR ../share fs-uae-launcher_$(version)_macosx/"FS-UAE Launcher.app"/Contents/Resources/

	# cp -pPR fs-uae_$(version)_macosx/FS-UAE.app fs-uae-launcher_$(version)_macosx/"FS-UAE Launcher.app"/Contents/Resources/

bindist-launcher: launcher
	cd fs-uae-launcher_$(version)_macosx && GZIP=-9 tar zcfv ../../fs-uae-launcher_$(version)_macosx.tar.gz *
