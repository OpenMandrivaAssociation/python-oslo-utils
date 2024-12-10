Name: python-oslo-utils
Version: 8.0.0
Release: 1
Source0: https://files.pythonhosted.org/packages/source/o/oslo.utils/oslo.utils-%{version}.tar.gz
Summary: Python utility library
URL: https://pypi.org/project/oslo.i18n/
License: Apache
Group: System/Libraries
BuildArch: noarch
BuildRequires: python python-setuptools
BuildRequires: python-pip python-wheel

%description
The oslo.utils library provides support for common utility type functions,
such as encoding, exception handling, string manipulation, and time
handling.

%prep
%autosetup -p1 -n oslo.utils-%{version}

%build
python setup.py build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}

%files
%{py_puresitedir}/oslo_utils
%{py_puresitedir}/*.egg-info
