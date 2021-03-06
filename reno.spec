#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : reno
Version  : 3.2.0
Release  : 48
URL      : https://files.pythonhosted.org/packages/b3/8c/a0c4b6596c6e7f232dcba1e6f97532b3e139b9f5b3c76284ae8e755dad4f/reno-3.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b3/8c/a0c4b6596c6e7f232dcba1e6f97532b3e139b9f5b3c76284ae8e755dad4f/reno-3.2.0.tar.gz
Summary  : RElease NOtes manager
Group    : Development/Tools
License  : Apache-2.0
Requires: reno-bin = %{version}-%{release}
Requires: reno-license = %{version}-%{release}
Requires: reno-python = %{version}-%{release}
Requires: reno-python3 = %{version}-%{release}
Requires: PyYAML
Requires: docutils
Requires: dulwich
Requires: packaging
Requires: pbr
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : docutils
BuildRequires : dulwich
BuildRequires : packaging
BuildRequires : pbr

%description
=========================================
reno: A New Way to Manage Release Notes
=========================================

%package bin
Summary: bin components for the reno package.
Group: Binaries
Requires: reno-license = %{version}-%{release}

%description bin
bin components for the reno package.


%package license
Summary: license components for the reno package.
Group: Default

%description license
license components for the reno package.


%package python
Summary: python components for the reno package.
Group: Default
Requires: reno-python3 = %{version}-%{release}

%description python
python components for the reno package.


%package python3
Summary: python3 components for the reno package.
Group: Default
Requires: python3-core
Provides: pypi(reno)
Requires: pypi(dulwich)
Requires: pypi(packaging)
Requires: pypi(pbr)
Requires: pypi(pyyaml)

%description python3
python3 components for the reno package.


%prep
%setup -q -n reno-3.2.0
cd %{_builddir}/reno-3.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598982214
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/reno
cp %{_builddir}/reno-3.2.0/LICENSE %{buildroot}/usr/share/package-licenses/reno/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/reno

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/reno/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
