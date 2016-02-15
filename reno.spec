#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : reno
Version  : 1.1.0
Release  : 4
URL      : https://pypi.python.org/packages/source/r/reno/reno-1.1.0.tar.gz
Source0  : https://pypi.python.org/packages/source/r/reno/reno-1.1.0.tar.gz
Summary  : RElease NOtes manager
Group    : Development/Tools
License  : Apache-2.0
Requires: reno-bin
Requires: reno-python
BuildRequires : Babel-python
BuildRequires : PyYAML-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : hacking
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : setuptools
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

%description
===============================
reno -- Release Notes Manager
===============================

%package bin
Summary: bin components for the reno package.
Group: Binaries

%description bin
bin components for the reno package.


%package python
Summary: python components for the reno package.
Group: Default
Requires: Babel-python
Requires: PyYAML-python

%description python
python components for the reno package.


%prep
%setup -q -n reno-1.1.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/reno

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
