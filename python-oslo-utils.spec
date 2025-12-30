Name: python-oslo-utils
Version: 9.2.0
Release: 1
Source0: https://files.pythonhosted.org/packages/source/o/oslo_utils/oslo_utils-%{version}.tar.gz
Summary: Python utility library
URL: https://pypi.org/project/oslo_utils/
License: Apache
Group: System/Libraries
BuildArch: noarch
BuildSystem: python
BuildRequires: python%{pyver}dist(pbr)

%description
The oslo.utils library provides support for common utility type functions,
such as encoding, exception handling, string manipulation, and time
handling.

%files
%{py_puresitedir}/oslo_utils
%{py_puresitedir}/oslo_utils-%{version}.dist-info
