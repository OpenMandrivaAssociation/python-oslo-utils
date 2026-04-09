%define module oslo_utils

Name:		python-oslo-utils
Summary:	Python utility library
Version:	10.0.1
Release:	1
License:	Apache-2.0
Group:		System/Libraries
URL:		https://pypi.org/project/oslo_utils/
Source0:	https://files.pythonhosted.org/packages/source/o/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem: python
BuildArch: noarch
BuildRequires:	python%{pyver}dist(pbr)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
The oslo.utils library provides support for common utility type functions,
such as encoding, exception handling, string manipulation, and time
handling.

%files
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info
