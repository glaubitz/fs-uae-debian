version := $(strip $(shell cat VERSION))
series := $(strip $(shell cat SERIES))
prefix := /usr
build_dir := "."
dist_name = fs-uae-arcade-$(version)
dist_dir := $(build_dir)/$(dist_name)

ifeq ($(wildcard fsbc),)
	fsbc_dir := "../python"
else
	fsbc_dir := "."
endif

ifeq ($(wildcard fsgs),)
	fsgs_dir := "../python"
else
	fsgs_dir := "."
endif

ifeq ($(wildcard fsui),)
	fsui_dir := "../python"
else
	fsui_dir := "."
endif

ifeq ($(wildcard game_center),)
	game_center_dir := "../python"
else
	game_center_dir := "."
endif

ifeq ($(wildcard lhafile),)
	lhafile_dir := "../python-lhafile"
else
	lhafile_dir := "."
endif

ifeq ($(wildcard six),)
	six_dir := "../python"
else
	six_dir := "."
endif

all: mo

share/locale/%/LC_MESSAGES/fs-uae-arcade.mo: po/%.po
	mkdir -p share/locale/$*/LC_MESSAGES
	msgfmt --verbose $< -o $@

catalogs = \


mo: $(catalogs)

install: mo
	mkdir -p $(DESTDIR)$(prefix)/share
	cp -a share/* $(DESTDIR)$(prefix)/share

	mkdir -p $(DESTDIR)$(prefix)/share/doc/fs-uae-arcade
	cp -a README COPYING $(DESTDIR)$(prefix)/share/doc/fs-uae-arcade

dist_dir := fs-uae-arcade-$(version)

distdir:
	rm -Rf $(dist_dir)/*
	mkdir -p $(dist_dir)

	cp -a $(fsbc_dir)/fsbc $(dist_dir)/
	cp -a $(fsgs_dir)/fsgs $(dist_dir)/
	cp -a $(fsui_dir)/fsui $(dist_dir)/
	cp -a $(game_center_dir)/game_center $(dist_dir)/
	cp -a $(lhafile_dir)/lhafile $(dist_dir)/
	cp -a $(six_dir)/six $(dist_dir)/
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
	cp SERIES $(dist_dir)/
	cp VERSION $(dist_dir)/
	mkdir -p $(dist_dir)/debian
	cp debian/changelog $(dist_dir)/debian
	cp debian/compat $(dist_dir)/debian
	cp debian/control $(dist_dir)/debian
	cp debian/copyright $(dist_dir)/debian
	cp debian/links $(dist_dir)/debian
	cp debian/rules $(dist_dir)/debian
	mkdir -p $(dist_dir)/debian/source
	cp debian/source/format $(dist_dir)/debian/source
	cp fs-uae-arcade $(dist_dir)/
	cp fs-uae-arcade.spec $(dist_dir)/
	mkdir -p $(dist_dir)/icon
	cp icon/fs-uae-arcade.icns $(dist_dir)/icon
	cp icon/fs-uae-arcade.ico $(dist_dir)/icon
	mkdir -p $(dist_dir)/macosx
	cp macosx/Makefile $(dist_dir)/macosx
	cp po-update.py $(dist_dir)/
	cp setup.py $(dist_dir)/
	cp update-version.py $(dist_dir)/
	mkdir -p $(dist_dir)/windows
	cp windows/Makefile $(dist_dir)/windows
	cp windows/replace-icon.py $(dist_dir)/windows
	cd $(dist_dir) && python update-version.py setup.py
	cd $(dist_dir) && python update-version.py debian/changelog
	cd $(dist_dir) && python update-version.py fs-uae-arcade --update-series
	cd $(dist_dir) && python update-version.py fs-uae-arcade.spec

dist: distdir
	find $(dist_dir) -exec touch \{\} \;
	cd "$(build_dir)" && tar zcfv $(dist_name).tar.gz $(dist_name)

windows-dist: distdir
	cd $(dist_dir)/windows && make
	mv $(dist_dir)/fs-uae-arcade_*windows* .
	rm -Rf $(dist_dir)

macosx-dist: distdir
	cd $(dist_dir)/macosx && make
	mv $(dist_dir)/fs-uae-arcade_*macosx* .
	rm -Rf $(dist_dir)

clean-dist:
	rm -Rf build dist fs-uae-arcade-* fs-uae-arcade_*
	rm -Rf debian/fs-uae-arcade*

clean:
	find share -name "*.mo" -delete
	find . -name "*.pyc" -delete

distclean: clean clean-dist
