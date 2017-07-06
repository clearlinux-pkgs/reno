#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : reno
Version  : 2.4.1
Release  : 20
URL      : http://pypi.debian.net/reno/reno-2.4.1.tar.gz
Source0  : http://pypi.debian.net/reno/reno-2.4.1.tar.gz
Summary  : RElease NOtes manager
Group    : Development/Tools
License  : Apache-2.0
Requires: reno-bin
Requires: reno-python
Requires: Babel
Requires: PyYAML
Requires: Sphinx
Requires: docutils
Requires: pbr
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=========================================
reno: A New Way to Manage Release Notes
=========================================

%package bin
Summary: bin components for the reno package.
Group: Binaries

%description bin
bin components for the reno package.


%package python
Summary: python components for the reno package.
Group: Default

%description python
python components for the reno package.


%prep
%setup -q -n reno-2.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1499362260
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1499362260
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/reno

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
