%define git_repo prestapyt

#define distsuffix xrg

%{?!py_sitedir: %global py_sitedir %(python -c 'import distutils.sysconfig; print distutils.sysconfig.get_python_lib()' 2>/dev/null || echo PYTHON-LIBDIR-NOT-FOUND)}

Name:       prestapyt
Summary:    Prestashop Python Client Library
Version:    %git_get_ver
Release:    %mkrel %git_get_rel
URL:        https://github.com/guewen/prestapyt
Source0:    %git_bs_source %{name}-%{version}.tar.gz
License:    AGPLv3
BuildArch:  noarch
Group:      Libraries
BuildRequires:  python
Requires:   python-httplib2

%description
A library to access Prestashop Web Service from Python.

%prep
%git_get_source
%setup -q

%build
python setup.py build
# TODO docs

%install
python setup.py install --root=%{buildroot} --compile
# --optimize=2

%files
%defattr(-,root,root)
%doc README.md CREDITS LICENSE
%{py_sitedir}/*

%changelog -f %{_sourcedir}/%{name}-changelog.gitrpm.txt

