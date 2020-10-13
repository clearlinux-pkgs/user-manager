#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : user-manager
Version  : 5.19.5
Release  : 39
URL      : https://download.kde.org/stable/plasma/5.19.5/user-manager-5.19.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.19.5/user-manager-5.19.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.19.5/user-manager-5.19.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0
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
%setup -q -n user-manager-5.19.5
cd %{_builddir}/user-manager-5.19.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602621200
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
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1602621200
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/user-manager
cp %{_builddir}/'user-manager-5.19.5/src/pics_sources/Air Balloon.png.license' %{buildroot}/usr/share/package-licenses/user-manager/adabd116af64401b76dd0583f403226df139a955
cp %{_builddir}/user-manager-5.19.5/COPYING %{buildroot}/usr/share/package-licenses/user-manager/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/user-manager-5.19.5/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/user-manager/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Astronaut.png.license %{buildroot}/usr/share/package-licenses/user-manager/cf03e23da9870281180ea4163b13a7bcf38a7a82
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Books.png.license %{buildroot}/usr/share/package-licenses/user-manager/cfbb9bcb7e1389c251a0ba3df2b0880cb6620ffb
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Brushes.png.license %{buildroot}/usr/share/package-licenses/user-manager/72d8e0f71a54fd570e1e5264d6e5fb7b29406ad4
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Bulb.png.license %{buildroot}/usr/share/package-licenses/user-manager/be0b3c0900b90dd09df479fad56b1229ad516d3a
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Car.png.license %{buildroot}/usr/share/package-licenses/user-manager/0a9b728823a71ad489b7e1f072590fa00f3aa5bc
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Cat.png.license %{buildroot}/usr/share/package-licenses/user-manager/129c1e09a68be9de6cef412b2a6e93559a87ea26
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Chamelon.png.license %{buildroot}/usr/share/package-licenses/user-manager/c1d70c75552ee593940f393a518534e72587338f
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Cocktail.png.license %{buildroot}/usr/share/package-licenses/user-manager/25b13534deaa992a714f25f14efeaa5eae4de592
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Dog.png.license %{buildroot}/usr/share/package-licenses/user-manager/6220b049f6ae68dbc5a495f05afca9adead61ff6
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Fish.png.license %{buildroot}/usr/share/package-licenses/user-manager/53c07475f67932feacd6188d906188a8dbd6991a
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Gamepad.png.license %{buildroot}/usr/share/package-licenses/user-manager/32946f0e0836c590cc36b8b3206eef0349aa13dd
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Owl.png.license %{buildroot}/usr/share/package-licenses/user-manager/f1bbe3025f15ecddbed6d4510fc2a1794ebf6009
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Pancakes.png.license %{buildroot}/usr/share/package-licenses/user-manager/7cd170c61cf35ee527ce0ffa4abf416bf29038a7
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Parrot.png.license %{buildroot}/usr/share/package-licenses/user-manager/a8b6c38c66a63e54df39a7a2394a61c386dcc323
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Pencils.png.license %{buildroot}/usr/share/package-licenses/user-manager/545c254aaacc416b6d7d7881d4ad9fe94c1cbf1e
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Shuttle.png.license %{buildroot}/usr/share/package-licenses/user-manager/3846b0d0a1072ef0698c1383f6aa5fa88e617a0d
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Soccer.png.license %{buildroot}/usr/share/package-licenses/user-manager/2363d6a59f5770f0340ae0e616d48b000ed85041
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Sunflower.png.license %{buildroot}/usr/share/package-licenses/user-manager/a8a48fc3a258971b868e37643efbabf5ca42ae95
cp %{_builddir}/user-manager-5.19.5/src/pics_sources/Sushi.png.license %{buildroot}/usr/share/package-licenses/user-manager/e6059edbfaf63e2ad3822f2c09b7ee4c9b6f2aad
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
/usr/share/user-manager/avatars/circles/Konqi.png
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
"/usr/share/user-manager/avatars/photos/Air Balloon.png"
/usr/share/user-manager/avatars/photos/Astronaut.png
/usr/share/user-manager/avatars/photos/Books.png
/usr/share/user-manager/avatars/photos/Brushes.png
/usr/share/user-manager/avatars/photos/Bulb.png
/usr/share/user-manager/avatars/photos/Car.png
/usr/share/user-manager/avatars/photos/Cat.png
/usr/share/user-manager/avatars/photos/Chameleon.png
/usr/share/user-manager/avatars/photos/Cocktail.png
/usr/share/user-manager/avatars/photos/Dog.png
/usr/share/user-manager/avatars/photos/Fish.png
/usr/share/user-manager/avatars/photos/Gamepad.png
/usr/share/user-manager/avatars/photos/Owl.png
/usr/share/user-manager/avatars/photos/Pancakes.png
/usr/share/user-manager/avatars/photos/Parrot.png
/usr/share/user-manager/avatars/photos/Pencils.png
/usr/share/user-manager/avatars/photos/Shuttle.png
/usr/share/user-manager/avatars/photos/Soccer.png
/usr/share/user-manager/avatars/photos/Sunflower.png
/usr/share/user-manager/avatars/photos/Sushi.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/user_manager.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/user-manager/0a9b728823a71ad489b7e1f072590fa00f3aa5bc
/usr/share/package-licenses/user-manager/129c1e09a68be9de6cef412b2a6e93559a87ea26
/usr/share/package-licenses/user-manager/2363d6a59f5770f0340ae0e616d48b000ed85041
/usr/share/package-licenses/user-manager/25b13534deaa992a714f25f14efeaa5eae4de592
/usr/share/package-licenses/user-manager/32946f0e0836c590cc36b8b3206eef0349aa13dd
/usr/share/package-licenses/user-manager/3846b0d0a1072ef0698c1383f6aa5fa88e617a0d
/usr/share/package-licenses/user-manager/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/user-manager/53c07475f67932feacd6188d906188a8dbd6991a
/usr/share/package-licenses/user-manager/545c254aaacc416b6d7d7881d4ad9fe94c1cbf1e
/usr/share/package-licenses/user-manager/6220b049f6ae68dbc5a495f05afca9adead61ff6
/usr/share/package-licenses/user-manager/72d8e0f71a54fd570e1e5264d6e5fb7b29406ad4
/usr/share/package-licenses/user-manager/7cd170c61cf35ee527ce0ffa4abf416bf29038a7
/usr/share/package-licenses/user-manager/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/user-manager/a8a48fc3a258971b868e37643efbabf5ca42ae95
/usr/share/package-licenses/user-manager/a8b6c38c66a63e54df39a7a2394a61c386dcc323
/usr/share/package-licenses/user-manager/adabd116af64401b76dd0583f403226df139a955
/usr/share/package-licenses/user-manager/be0b3c0900b90dd09df479fad56b1229ad516d3a
/usr/share/package-licenses/user-manager/c1d70c75552ee593940f393a518534e72587338f
/usr/share/package-licenses/user-manager/cf03e23da9870281180ea4163b13a7bcf38a7a82
/usr/share/package-licenses/user-manager/cfbb9bcb7e1389c251a0ba3df2b0880cb6620ffb
/usr/share/package-licenses/user-manager/e6059edbfaf63e2ad3822f2c09b7ee4c9b6f2aad
/usr/share/package-licenses/user-manager/f1bbe3025f15ecddbed6d4510fc2a1794ebf6009

%files locales -f user_manager.lang
%defattr(-,root,root,-)

