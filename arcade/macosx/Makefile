version = $(strip $(shell cat ../VERSION))
arcade_app = fs-uae-arcade_$(version)_macosx/FS-UAE Arcade.app
arcade_resources = $(arcade_app)/Contents/Resources

all: bindist-arcade

clean:
	rm -Rf ../macosx/fs-uae*

arcade:
	# make -C ..
	rm -Rf fs-uae-arcade_$(version)_macosx	
	mkdir -p fs-uae-arcade_$(version)_macosx
	cd .. && python2.7 setup.py py2app --iconfile icon/fs-uae-arcade.icns
	mv ../dist/"FS-UAE Arcade.app" "$(arcade_app)"

	cp -pPR ../share "$(arcade_resources)"/
	# mkdir -p "$(arcade_resources)"/share/fs-uae-arcade/fengestad.input
	# cp -pPR ../fengestad/input/res "$(arcade_resources)"/share/fs-uae-arcade/fengestad.input
	# mkdir -p "$(arcade_resources)"/share/fs-uae-arcade/fengestad.gamecenter
	# cp -pPR ../fengestad/gamecenter/res "$(arcade_resources)"/share/fs-uae-arcade/fengestad.gamecenter
	# cp -pPR fs-uae_$(version)_macosx/FS-UAE.app "$(arcade_resources)"/

bindist-arcade: arcade
	cd fs-uae-arcade_$(version)_macosx && GZIP=-9 tar zcfv ../../fs-uae-arcade_$(version)_macosx.tar.gz *
