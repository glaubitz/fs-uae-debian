version = $(strip $(shell cat ../../VERSION))
macos = fs-uae-arcade_$(version)_macosx/"FS-UAE Arcade.app"/Contents/MacOS/
frameworks = fs-uae-arcade_$(version)_macosx/"FS-UAE Arcade.app"/Contents/Frameworks/
resources = fs-uae-arcade_$(version)_macosx/"FS-UAE Arcade.app"/Contents/Resources/

all: bindist-arcade

clean:
	rm -Rf ../macosx/fs-uae-arcade*

arcade:
	make -C ../..
	rm -Rf fs-uae-arcade_$(version)_macosx	
	mkdir -p fs-uae-arcade_$(version)_macosx
	cd ../.. && python3 setup.py build_exe

	#mv ../dist/"FS-UAE Arcade.app" fs-uae-arcade_$(version)_macosx/
	#cp -pPR ../share $(resources)/
	# cp -pPR fs-uae_$(version)_macosx/FS-UAE.app fs-uae-arcade_$(version)_macosx/"FS-UAE Arcade.app"/Contents/Resources/

	mkdir -p $(macos)
	mkdir -p $(resources)
	mv ../../build/*/* $(macos)
	find fs-uae-arcade_$(version)_macosx/ -name *_debug.dylib -delete
	mv fs-uae-arcade_$(version)_macosx/"FS-UAE Arcade.app" fs-uae-arcade_$(version)_macosx/temp.app
	python3 fs-make-standalone-app.py fs-uae-arcade_$(version)_macosx/temp.app
	mv fs-uae-arcade_$(version)_macosx/temp.app fs-uae-arcade_$(version)_macosx/"FS-UAE Arcade.app"
	cp Info.plist fs-uae-arcade_$(version)_macosx/"FS-UAE Arcade.app"/Contents/
	cp ../../icon/fs-uae-arcade.icns $(resources)/fs-uae-arcade.icns
	# python3 sign.py fs-uae-arcade_$(version)_macosx/"FS-UAE Arcade.app"

bindist-arcade: arcade
	cd fs-uae-arcade_$(version)_macosx && GZIP=-9 tar zcfv ../../../fs-uae-arcade_$(version)_macosx.tar.gz *
