version := $(strip $(shell cat VERSION))
build_dir := "."
dist_name = fs-uae-arcade-$(version)
dist_dir := $(build_dir)/$(dist_name)

DESTDIR :=
prefix := /usr/local

ifeq ($(wildcard OpenGL),)
	OpenGL_dir := "../fs-uae-launcher"
else
	OpenGL_dir := "."
endif

ifeq ($(wildcard arcade),)
	arcade_dir := "../fs-uae-launcher"
else
	arcade_dir := "."
endif

ifeq ($(wildcard fsbc),)
	fsbc_dir := "../fs-uae-launcher"
else
	fsbc_dir := "."
endif

ifeq ($(wildcard fsboot),)
	fsboot_dir := "../fs-uae-launcher"
else
	fsboot_dir := "."
endif

ifeq ($(wildcard fsgs),)
	fsgs_dir := "../fs-uae-launcher"
else
	fsgs_dir := "."
endif

ifeq ($(wildcard fspy),)
	fspy_dir := "../fs-uae-launcher"
else
	fspy_dir := "."
endif

ifeq ($(wildcard fstd),)
	fstd_dir := "../fs-uae-launcher"
else
	fstd_dir := "."
endif

ifeq ($(wildcard fsui),)
	fsui_dir := "../fs-uae-launcher"
else
	fsui_dir := "."
endif

ifeq ($(wildcard launcher),)
	launcher_dir := "../fs-uae-launcher"
else
	launcher_dir := "."
endif

ifeq ($(wildcard oyoyo),)
	oyoyo_dir := "../fs-uae-launcher"
else
	oyoyo_dir := "."
endif

ifeq ($(wildcard workspace),)
	workspace_dir := "../fs-uae-launcher"
else
	workspace_dir := "."
endif

all: mo

share/locale/%/LC_MESSAGES/fs-uae-arcade.mo: po/%.po
	mkdir -p share/locale/$*/LC_MESSAGES
	msgfmt --verbose $< -o $@

catalogs = \


mo: $(catalogs)


install-program:
ifeq ($(DESTDIR),)
	python3 setup.py install	 --install-lib=$(prefix)/share/fs-uae-arcade	 --install-scripts=$(prefix)/share/fs-uae-arcade
	install -d $(DESTDIR)$(prefix)/bin
	rm -f $(DESTDIR)$(prefix)/bin/fs-uae-arcade
	ln -s ../share/fs-uae-arcade/fs-uae-arcade	 $(DESTDIR)$(prefix)/bin/fs-uae-arcade
else
	python3 setup.py install	 --root=$(DESTDIR)	 --install-lib=$(prefix)/share/fs-uae-arcade	 --install-scripts=$(prefix)/share/fs-uae-arcade
	install -d $(DESTDIR)$(prefix)/bin
	rm -f $(DESTDIR)$(prefix)/bin/fs-uae-arcade
	ln -s ../share/fs-uae-arcade/fs-uae-arcade	 $(DESTDIR)$(prefix)/bin/fs-uae-arcade
endif

install-data: mo
	mkdir -p $(DESTDIR)$(prefix)/share
	cp -a share/* $(DESTDIR)$(prefix)/share

	mkdir -p $(DESTDIR)$(prefix)/share/doc/fs-uae-arcade
	cp -a README COPYING $(DESTDIR)$(prefix)/share/doc/fs-uae-arcade

install: install-data install-program

dist_dir := fs-uae-arcade-$(version)

distdir:
	rm -Rf $(dist_dir)/*
	mkdir -p $(dist_dir)

	cp -a $(OpenGL_dir)/OpenGL $(dist_dir)/
	cp -a $(arcade_dir)/arcade $(dist_dir)/
	cp -a $(fsbc_dir)/fsbc $(dist_dir)/
	cp -a $(fsboot_dir)/fsboot $(dist_dir)/
	cp -a $(fsgs_dir)/fsgs $(dist_dir)/
	cp -a $(fspy_dir)/fspy $(dist_dir)/
	cp -a $(fstd_dir)/fstd $(dist_dir)/
	cp -a $(fsui_dir)/fsui $(dist_dir)/
	cp -a $(launcher_dir)/launcher $(dist_dir)/
	cp -a $(oyoyo_dir)/oyoyo $(dist_dir)/
	cp -a $(workspace_dir)/workspace $(dist_dir)/
	cp -a share $(dist_dir)/
	mkdir $(dist_dir)/po/

	find $(dist_dir) -name "*.mo" -delete
	find $(dist_dir) -name "*.pyc" -delete
	find $(dist_dir) -name "*.pyo" -delete
	find $(dist_dir) -name __pycache__ -delete

	cp COPYING $(dist_dir)/
	cp INSTALL $(dist_dir)/
	cp Makefile $(dist_dir)/
	cp README $(dist_dir)/
	cp VERSION $(dist_dir)/
	cp cacert.pem $(dist_dir)/
	mkdir -p $(dist_dir)/debian
	cp debian/changelog $(dist_dir)/debian
	cp debian/compat $(dist_dir)/debian
	cp debian/control $(dist_dir)/debian
	cp debian/copyright $(dist_dir)/debian
	cp debian/links $(dist_dir)/debian
	cp debian/rules $(dist_dir)/debian
	mkdir -p $(dist_dir)/debian/source
	cp debian/source/format $(dist_dir)/debian/source
	mkdir -p $(dist_dir)/dist
	cp dist/arch.py $(dist_dir)/dist
	mkdir -p $(dist_dir)/dist/macos
	cp dist/macos/Info.plist $(dist_dir)/dist/macos
	cp dist/macos/Makefile $(dist_dir)/dist/macos
	cp dist/macos/sign.py $(dist_dir)/dist/macos
	cp dist/macos/standalone.py $(dist_dir)/dist/macos
	mkdir -p $(dist_dir)/dist/python
	cp dist/python/Makefile $(dist_dir)/dist/python
	cp fs-uae-arcade $(dist_dir)/
	cp fs-uae-arcade.spec $(dist_dir)/
	mkdir -p $(dist_dir)/icon
	cp icon/fs-uae-arcade.icns $(dist_dir)/icon
	cp icon/fs-uae-arcade.ico $(dist_dir)/icon
	cp po-update.py $(dist_dir)/
	cp setup.py $(dist_dir)/
	cp update-version $(dist_dir)/
	cd $(dist_dir) && ./update-version setup.py --strict
	cd $(dist_dir) && ./update-version debian/changelog --deb
	cd $(dist_dir) && ./update-version dist/macos/Info.plist --strict
	cd $(dist_dir) && ./update-version launcher/version.py
	cd $(dist_dir) && ./update-version fs-uae-arcade
	cd $(dist_dir) && ./update-version fs-uae-arcade.spec --rpm

dist: distdir
	find $(dist_dir) -exec touch \{\} \;
	cd "$(build_dir)" && tar zcfv $(dist_name).tar.gz $(dist_name)

windows-dist: distdir
	cd $(dist_dir)/dist/windows && make
	mv $(dist_dir)/fs-uae-arcade_*windows* .
	rm -Rf $(dist_dir)

macos-dist: distdir
	cd $(dist_dir)/dist/macos && make
	mv $(dist_dir)/fs-uae-arcade_*macos* .
	rm -Rf $(dist_dir)

clean-dist:
	rm -Rf fs-uae-arcade-* fs-uae-arcade_*
	rm -Rf debian/fs-uae-arcade*

clean:
	rm -Rf build
	find share -name "*.mo" -delete
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name __pycache__ -delete

distclean: clean clean-dist
	rm -f Makefile
	rm -f setup.py

bindist: distdir
	cd $(dist_dir)/dist/linux && fs-sdk-linux-x86-64 make
	mv $(dist_dir)/fs-uae-launcher_*linux* .
	rm -Rf $(dist_dir)

bindist-x86: distdir
	cd $(dist_dir)/dist/linux && fs-sdk-linux-x86 make
	mv $(dist_dir)/fs-uae-launcher_*linux* .
	rm -Rf $(dist_dir)

