#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pkginfo
Version  : 1.5.0.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/6c/04/fd6683d24581894be8b25bc8c68ac7a0a73bf0c4d74b888ac5fe9a28e77f/pkginfo-1.5.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/6c/04/fd6683d24581894be8b25bc8c68ac7a0a73bf0c4d74b888ac5fe9a28e77f/pkginfo-1.5.0.1.tar.gz
Summary  : Query metadatdata from sdists / bdists / installed packages.
Group    : Development/Tools
License  : MIT
Requires: pkginfo-bin = %{version}-%{release}
Requires: pkginfo-license = %{version}-%{release}
Requires: pkginfo-python = %{version}-%{release}
Requires: pkginfo-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
==================
        
        This package provides an API for querying the distutils metadata written in
        the ``PKG-INFO`` file inside a source distriubtion (an ``sdist``) or a
        binary distribution (e.g., created by running ``bdist_egg``).  It can
        also query the ``EGG-INFO`` directory of an installed distribution, and
        the ``*.egg-info`` stored in a "development checkout"
        (e.g, created by running ``setup.py develop``).

%package bin
Summary: bin components for the pkginfo package.
Group: Binaries
Requires: pkginfo-license = %{version}-%{release}

%description bin
bin components for the pkginfo package.


%package license
Summary: license components for the pkginfo package.
Group: Default

%description license
license components for the pkginfo package.


%package python
Summary: python components for the pkginfo package.
Group: Default
Requires: pkginfo-python3 = %{version}-%{release}

%description python
python components for the pkginfo package.


%package python3
Summary: python3 components for the pkginfo package.
Group: Default
Requires: python3-core
Provides: pypi(pkginfo)

%description python3
python3 components for the pkginfo package.


%prep
%setup -q -n pkginfo-1.5.0.1
cd %{_builddir}/pkginfo-1.5.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603398708
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pkginfo
cp %{_builddir}/pkginfo-1.5.0.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/pkginfo/03162d5b27cb1ca3f768d50b3ea24877f6543dbd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pkginfo

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pkginfo/03162d5b27cb1ca3f768d50b3ea24877f6543dbd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
