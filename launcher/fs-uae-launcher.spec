%define name fs-uae-launcher
%define version 2.4.1
%define unmangled_version 2.4.1
%define release 1%{?dist}

Summary: Graphical configuration frontend and launcher for FS-UAE
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
Requires: python-qt4 fs-uae python-setuptools
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
FS-UAE Launcher is a graphical configuration program and
launcher for FS-UAE.

%prep
%setup -n %{name}-%{unmangled_version}

%build
%{__python} setup.py build
make

%install
#%{__python} install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES \
#--prefix=/usr

%{__python} setup.py install \
--prefix=%{_prefix} \
--root=%{buildroot} \
--install-lib=%{_prefix}/share/fs-uae-launcher \
--install-scripts=%{_prefix}/share/fs-uae-launcher
make install DESTDIR=$RPM_BUILD_ROOT
mkdir %{buildroot}/%{_prefix}/bin
ln -s %{_prefix}/share/fs-uae-launcher/fs-uae-launcher \
%{buildroot}/%{_prefix}/bin/fs-uae-launcher

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%_bindir/*
%_datadir/%{name}/
%_datadir/doc/%{name}/
%_datadir/applications/*.desktop
%_datadir/icons/*/*/*/*.png
%_datadir/locale/*/*/*.mo

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
