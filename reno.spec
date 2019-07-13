#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : reno
Version  : 2.11.3
Release  : 39
URL      : https://files.pythonhosted.org/packages/a9/8f/134bb3a26dbe947db297dd2b16d71115d732fb8f4b17ef482601a5fa6a59/reno-2.11.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/a9/8f/134bb3a26dbe947db297dd2b16d71115d732fb8f4b17ef482601a5fa6a59/reno-2.11.3.tar.gz
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
Requires: pbr
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : dulwich
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

%description python3
python3 components for the reno package.


%prep
%setup -q -n reno-2.11.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554402141
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/reno
cp LICENSE %{buildroot}/usr/share/package-licenses/reno/LICENSE
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
/usr/share/package-licenses/reno/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
