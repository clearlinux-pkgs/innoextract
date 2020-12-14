#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x28555A66D7E1DEC9 (daniel@constexpr.org)
#
Name     : innoextract
Version  : 1.8
Release  : 7
URL      : https://github.com/dscharrer/innoextract/releases/download/1.8/innoextract-1.8.tar.gz
Source0  : https://github.com/dscharrer/innoextract/releases/download/1.8/innoextract-1.8.tar.gz
Source1  : https://github.com/dscharrer/innoextract/releases/download/1.8/innoextract-1.8.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : Zlib
Requires: innoextract-bin = %{version}-%{release}
Requires: innoextract-license = %{version}-%{release}
Requires: innoextract-man = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : pkg-config
BuildRequires : pkgconfig(liblzma)
BuildRequires : python3

%description
# innoextract - A tool to unpack installers created by Inno Setup
[Inno Setup](http://www.jrsoftware.org/isinfo.php) is a tool to create installers for Microsoft Windows applications. innoextract allows to extract such installers under non-Windows systems without running the actual installer using wine. innoextract currently supports installers created by Inno Setup 1.2.10 to 5.6.0.

%package bin
Summary: bin components for the innoextract package.
Group: Binaries
Requires: innoextract-license = %{version}-%{release}

%description bin
bin components for the innoextract package.


%package license
Summary: license components for the innoextract package.
Group: Default

%description license
license components for the innoextract package.


%package man
Summary: man components for the innoextract package.
Group: Default

%description man
man components for the innoextract package.


%prep
%setup -q -n innoextract-1.8
cd %{_builddir}/innoextract-1.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592454274
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1592454274
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/innoextract
cp %{_builddir}/innoextract-1.8/LICENSE %{buildroot}/usr/share/package-licenses/innoextract/f40c216cd654f955c27946064fced5a5d41e47fb
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/innoextract

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/innoextract/f40c216cd654f955c27946064fced5a5d41e47fb

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/innoextract.1
