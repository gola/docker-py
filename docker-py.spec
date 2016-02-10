%define name docker-py
%define version 1.6.0
%define release 2

Summary: docker-py tar pacekage from douban pip.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: MarsGu <gukai@syswin.com>
Url: http://www.openstack.org/

# The context of requirements.txt, But it works in well test env:
#     python-requests-2.2.1, 
#     python-six-1.7.3-1.el6.noarch
#     whithout websocket-client。
#
#requests==2.5.3
#six>=1.4.0
#websocket-client==0.32.0
Requires: 	docker-io
#Requires: 	python-requests == 2.5.3
#Requires: 	python-websocket-client == 0.32.0
#Requires:	python-six >= 1.4.0

%description
===============================
docker-py
===============================
docker-py tar pacekage from douban pip.

%prep
%setup -n %{name}-%{version} -n %{name}-%{version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
