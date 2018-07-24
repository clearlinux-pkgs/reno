#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : reno
Version  : 2.9.2
Release  : 26
URL      : https://files.pythonhosted.org/packages/83/cb/e76c5c678decc0cb28f3b8e29dea7c324ef67a2b69898dfb6fc16d2b41d3/reno-2.9.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/83/cb/e76c5c678decc0cb28f3b8e29dea7c324ef67a2b69898dfb6fc16d2b41d3/reno-2.9.2.tar.gz
Summary  : RElease NOtes manager
Group    : Development/Tools
License  : Apache-2.0
Requires: reno-bin
Requires: reno-python3
Requires: reno-license
Requires: reno-python
Requires: PyYAML
Requires: Sphinx
Requires: coverage
Requires: docutils
Requires: dulwich
Requires: hacking
Requires: openstackdocstheme
Requires: pbr
Requires: python-mock
Requires: python-subunit
Requires: six
Requires: testrepository
Requires: testscenarios
Requires: testtools
BuildRequires : buildreq-distutils3
BuildRequires : dulwich
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=========================================
reno: A New Way to Manage Release Notes
=========================================

%package bin
Summary: bin components for the reno package.
Group: Binaries
Requires: reno-license

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
Requires: reno-python3

%description python
python components for the reno package.


%package python3
Summary: python3 components for the reno package.
Group: Default
Requires: python3-core

%description python3
python3 components for the reno package.


%prep
%setup -q -n reno-2.9.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532452883
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/reno
cp LICENSE %{buildroot}/usr/share/doc/reno/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/reno

%files license
%defattr(-,root,root,-)
/usr/share/doc/reno/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
