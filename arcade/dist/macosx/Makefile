version = $(strip $(shell cat ../../VERSION))
arch = $(strip $(shell python3 ../arch.py))

ver_os_arch = $(version)_macosx_$(arch)
dname = fs-uae-arcade_$(ver_os_arch)
app = $(dname)/"FS-UAE Arcade.app"
macos =  $(app)/Contents/MacOS/
frameworks = $(app)/Contents/Frameworks/
resources = $(app)/Contents/Resources/

all: bindist-arcade

clean:
	rm -Rf ../macosx/fs-uae-arcade*

arcade:
	make -C ../..
	rm -Rf $(dname)
	mkdir -p $(dname)
	cd ../.. && python3 setup.py build_exe

	#mv ../dist/"FS-UAE Arcade.app" $(dname)/
	#cp -pPR ../share $(resources)/
	# cp -pPR fs-uae_$(version)_macosx/FS-UAE.app $(dname)/"FS-UAE Arcade.app"/Contents/Resources/

	mkdir -p $(macos)
	mkdir -p $(resources)
	mv ../../build/*/* $(macos)
	find $(dname)/ -name *_debug.dylib -delete
	mv $(dname)/"FS-UAE Arcade.app" $(dname)/temp.app
	python3 fs-make-standalone-app.py $(dname)/temp.app
	mv $(dname)/temp.app $(dname)/"FS-UAE Arcade.app"
	cp Info.plist $(dname)/"FS-UAE Arcade.app"/Contents/
	cp ../../icon/fs-uae-arcade.icns $(resources)/fs-uae-arcade.icns
	# python3 sign.py $(dname)/"FS-UAE Arcade.app"

bindist-arcade: arcade
	cd $(dname) && GZIP=-9 tar zcfv ../../../$(dname).tar.gz *
