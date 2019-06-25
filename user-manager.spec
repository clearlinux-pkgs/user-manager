#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : user-manager
Version  : 5.16.2
Release  : 19
URL      : https://download.kde.org/stable/plasma/5.16.2/user-manager-5.16.2.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.16.2/user-manager-5.16.2.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.16.2/user-manager-5.16.2.tar.xz.sig
Summary  : A simple system settings module to manage the users of your system
Group    : Development/Tools
License  : GPL-2.0
Requires: user-manager-data = %{version}-%{release}
Requires: user-manager-lib = %{version}-%{release}
Requires: user-manager-license = %{version}-%{release}
Requires: user-manager-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : pkg-config
BuildRequires : pkgconfig(pwquality)
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package data
Summary: data components for the user-manager package.
Group: Data

%description data
data components for the user-manager package.


%package lib
Summary: lib components for the user-manager package.
Group: Libraries
Requires: user-manager-data = %{version}-%{release}
Requires: user-manager-license = %{version}-%{release}

%description lib
lib components for the user-manager package.


%package license
Summary: license components for the user-manager package.
Group: Default

%description license
license components for the user-manager package.


%package locales
Summary: locales components for the user-manager package.
Group: Default

%description locales
locales components for the user-manager package.


%prep
%setup -q -n user-manager-5.16.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561485671
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1561485671
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/user-manager
cp COPYING %{buildroot}/usr/share/package-licenses/user-manager/COPYING
pushd clr-build
%make_install
popd
%find_lang user_manager

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/user_manager.desktop
"/usr/share/user-manager/avatars/bluesstyle/Ada Lovelace.png"
"/usr/share/user-manager/avatars/bluesstyle/Alice in Wonderland.png"
"/usr/share/user-manager/avatars/bluesstyle/Grace Hopper.png"
"/usr/share/user-manager/avatars/bluesstyle/Leonardo da Vinci.png"
"/usr/share/user-manager/avatars/bluesstyle/Mahatma Gandhi.png"
/usr/share/user-manager/avatars/bluesstyle/Man.png
"/usr/share/user-manager/avatars/bluesstyle/Mowgli jungle book.png"
/usr/share/user-manager/avatars/circles/Cat.png
/usr/share/user-manager/avatars/circles/Female.png
/usr/share/user-manager/avatars/circles/Konqui.png
/usr/share/user-manager/avatars/circles/Male.png
/usr/share/user-manager/avatars/circles/Penguin.png
/usr/share/user-manager/avatars/circles/Zebra.png
/usr/share/user-manager/avatars/classic/Blackbox.png
/usr/share/user-manager/avatars/classic/Bomb.png
/usr/share/user-manager/avatars/classic/Dragon.png
/usr/share/user-manager/avatars/classic/Green.png
/usr/share/user-manager/avatars/classic/Happy.png
/usr/share/user-manager/avatars/classic/Listening.png
/usr/share/user-manager/avatars/classic/Notme.png
/usr/share/user-manager/avatars/classic/TV.png
/usr/share/user-manager/avatars/konqui/Kati.png
/usr/share/user-manager/avatars/konqui/Konqui.png
/usr/share/user-manager/avatars/konqui/Logger.png
/usr/share/user-manager/avatars/konqui/Parley.png
/usr/share/user-manager/avatars/konqui/Rekonqui.png
/usr/share/xdg/user-manager.categories

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/user_manager.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/user-manager/COPYING

%files locales -f user_manager.lang
%defattr(-,root,root,-)

