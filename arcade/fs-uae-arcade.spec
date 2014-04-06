%define name fs-uae-arcade
%define version 2.4.1
%define unmangled_version 2.4.1
%define release 1%{?dist}

Summary: Fullscreen game browser for FS-UAE
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://fs-uae.net/
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPL-2.0+
Group: Applications/Emulators
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Frode Solheim <frode@fs-uae.net>
Requires: fs-uae python-setuptools python-imaging pygame python-opengl
BuildRequires: python-devel python-setuptools

%define is_mandrake %(test -e /etc/mandrake-release && echo 1 || echo 0)
%define is_suse %(test -e /etc/SuSE-release && echo 1 || echo 0)
%define is_fedora %(test -e /etc/fedora-release && echo 1 || echo 0)

%if 0%{?suse_version}
%else
%if 0%{?mandriva_version}
%else
%endif
%endif

%description
FS-UAE Arcade is a fullscreen Amiga game browser for FS-UAE.

%prep
%setup -n %{name}-%{unmangled_version}

%build
%{__python} setup.py build
make

%install
%{__python} setup.py install \
--prefix=%{_prefix} \
--root=%{buildroot} \
--install-lib=%{_prefix}/share/fs-uae-arcade \
--install-scripts=%{_prefix}/share/fs-uae-arcade
make install DESTDIR=$RPM_BUILD_ROOT
mkdir %{buildroot}/%{_prefix}/bin
ln -s %{_prefix}/share/fs-uae-arcade/fs-uae-arcade \
%{buildroot}/%{_prefix}/bin/fs-uae-arcade

%if 0%{?suse_version}
# when building for openSUSE, a lint checker refuses to accept Game;Emulator;
sed -i "s/Categories=Game;Emulator;/Categories=System;Emulator;/g" \
%{buildroot}/%{_prefix}/share/applications/fs-uae-arcade.desktop
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%_bindir/*
%_datadir/%{name}/
%_datadir/doc/%{name}/
%_datadir/applications/*.desktop
%_datadir/icons/*/*/*/*.png
# %_datadir/locale/*/*/*.mo

%dir %_datadir/icons/hicolor
%dir %_datadir/icons/hicolor/128x128
%dir %_datadir/icons/hicolor/128x128/apps
%dir %_datadir/icons/hicolor/16x16
%dir %_datadir/icons/hicolor/16x16/apps
%dir %_datadir/icons/hicolor/256x256
%dir %_datadir/icons/hicolor/256x256/apps
%dir %_datadir/icons/hicolor/32x32
%dir %_datadir/icons/hicolor/32x32/apps
%dir %_datadir/icons/hicolor/48x48
%dir %_datadir/icons/hicolor/48x48/apps
%dir %_datadir/icons/hicolor/64x64
%dir %_datadir/icons/hicolor/64x64/apps

%doc

%changelog
