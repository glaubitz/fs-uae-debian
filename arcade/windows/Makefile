version = $(strip $(shell cat ../VERSION))
program_dir = fs-uae-arcade_$(version)_windows

all: progdir zipfile setup

clean:
	rm -Rf fs-uae-arcade-*_windows*
	rm -Rf fs-uae-arcade_*_windows*

progdir:
	rm -Rf $(program_dir)

	# make -C ..

	rm -Rf ../build ../dist
	cd .. && python setup.py py2exe
	mv ../dist $(program_dir)

	cp -a ../share $(program_dir)/share

	python replace-icon.py $(program_dir)/fs-uae-arcade.exe ../icon/fs-uae-arcade.ico
	python /c/signtool.py $(program_dir)/fs-uae-arcade.exe
	cp -a /c/Microsoft.VC90.CRT $(program_dir)/
	# cp -a $(emulator_dir) $(program_dir)/FS-UAE

zipfile:
	cd $(program_dir) && zip -9 -r ../../$(program_dir).zip *

setup:
	sed s/9.8.7/${version}/g fs-uae-arcade.iss > fs-uae-arcade.iss.tmp
	iscc fs-uae-arcade.iss.tmp
	python /c/signtool.py ../fs-uae-arcade_$(version)_windows.exe
	rm fs-uae-arcade.iss.tmp
