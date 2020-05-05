#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : user-manager
Version  : 5.18.5
Release  : 34
URL      : https://download.kde.org/stable/plasma/5.18.5/user-manager-5.18.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.18.5/user-manager-5.18.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.18.5/user-manager-5.18.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: user-manager-data = %{version}-%{release}
Requires: user-manager-lib = %{version}-%{release}
Requires: user-manager-license = %{version}-%{release}
Requires: user-manager-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : ki18n-dev
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
%setup -q -n user-manager-5.18.5
cd %{_builddir}/user-manager-5.18.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588707927
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1588707927
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/user-manager
cp %{_builddir}/user-manager-5.18.5/COPYING %{buildroot}/usr/share/package-licenses/user-manager/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd clr-build
%make_install
popd
%find_lang user_manager

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/user_manager.desktop
/usr/share/qlogging-categories5/user-manager.categories
/usr/share/user-manager/avatars/circles/Cat.png
/usr/share/user-manager/avatars/circles/Female.png
/usr/share/user-manager/avatars/circles/Konqi.png
/usr/share/user-manager/avatars/circles/Male.png
/usr/share/user-manager/avatars/circles/Penguin.png
/usr/share/user-manager/avatars/circles/Zebra.png
"/usr/share/user-manager/avatars/konqui/Artist Konqi.png"
"/usr/share/user-manager/avatars/konqui/Bookworm Konqi.png"
"/usr/share/user-manager/avatars/konqui/Boss Konqi.png"
"/usr/share/user-manager/avatars/konqui/Bug Catcher Konqi.png"
"/usr/share/user-manager/avatars/konqui/Card Shark Konqi.png"
"/usr/share/user-manager/avatars/konqui/Hacker Konqi.png"
"/usr/share/user-manager/avatars/konqui/Journalist Konqi.png"
/usr/share/user-manager/avatars/konqui/Katie.png
/usr/share/user-manager/avatars/konqui/Konqi.png
"/usr/share/user-manager/avatars/konqui/Mechanic Konqi.png"
"/usr/share/user-manager/avatars/konqui/Messenger Konqi.png"
"/usr/share/user-manager/avatars/konqui/Musician Konqi.png"
"/usr/share/user-manager/avatars/konqui/Office Worker Konqi.png"
"/usr/share/user-manager/avatars/konqui/PC Builder Konqi.png"
"/usr/share/user-manager/avatars/konqui/Scientist Konqi.png"
"/usr/share/user-manager/avatars/konqui/Teacher Konqi.png"
"/usr/share/user-manager/avatars/konqui/Virtual Reality Konqi.png"

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/user_manager.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/user-manager/4cc77b90af91e615a64ae04893fdffa7939db84c

%files locales -f user_manager.lang
%defattr(-,root,root,-)

