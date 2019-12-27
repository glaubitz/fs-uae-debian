lib = ../../build/lib
zip=zip -r
#copy=python3 ../../fspy/zipfile.py deterministic
cp=python3 -m fspy.zipfile deterministic
PYTHONPATH=../..:../../../fs-uae-launcher

all: build

build:
	# cd ../../fs-uae-arcade && ./bootstrap
	cd ../.. && rm -Rf build/lib
	cd ../.. && python3 setup.py build

	cd $(lib) && rm -f *.zip

	cd $(lib) && $(zip) arcade.zip arcade
	PYTHONPATH=$(PYTHONPATH) $(cp) $(lib)/arcade.zip arcade.zip

	cd $(lib) && $(zip) fsbc.zip fsbc
	PYTHONPATH=$(PYTHONPATH) $(cp) $(lib)/fsbc.zip fsbc.zip

	# cd $(lib) && $(zip) fsboot.zip fsboot
	# PYTHONPATH=$(PYTHONPATH) $(cp) $(lib)/fsboot.zip .

	cd $(lib) && $(zip) fsgs.zip fsgs
	PYTHONPATH=$(PYTHONPATH) $(cp) $(lib)/fsgs.zip fsgs.zip

	cd $(lib) && $(zip) fspy.zip fspy
	PYTHONPATH=$(PYTHONPATH) $(cp) $(lib)/fspy.zip fspy.zip

	cd $(lib) && $(zip) fstd.zip fstd
	PYTHONPATH=$(PYTHONPATH) $(cp) $(lib)/fstd.zip fstd.zip

	cd $(lib) && $(zip) fsui.zip fsui
	PYTHONPATH=$(PYTHONPATH) $(cp) $(lib)/fsui.zip fsui.zip

	cd $(lib) && $(zip) launcher.zip launcher
	PYTHONPATH=$(PYTHONPATH) $(cp) $(lib)/launcher.zip launcher.zip

	cd $(lib) && $(zip) OpenGL.zip OpenGL
	PYTHONPATH=$(PYTHONPATH) $(cp) $(lib)/OpenGL.zip OpenGL.zip

	cd $(lib) && $(zip) oyoyo.zip oyoyo
	PYTHONPATH=$(PYTHONPATH) $(cp) $(lib)/oyoyo.zip oyoyo.zip

	cd $(lib) && $(zip) workspace.zip workspace
	PYTHONPATH=$(PYTHONPATH) $(cp) $(lib)/workspace.zip workspace.zip

	cd ../.. && rm -Rf build/lib
