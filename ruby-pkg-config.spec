#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	pkg-config
Summary:	pkg-config module for Ruby
Summary(pl.UTF-8):	Moduł pkg-config dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.1.5
Release:	3
License:	LGPL v2.1+
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	c32204c8d6f0d1cae84f6c67b3e0fd92
Patch0:		%{name}-avoid-cycle.patch
URL:		https://github.com/ruby-gnome2/pkg-config
BuildRequires:	pkgconfig
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-bundler
BuildRequires:	ruby-rake
BuildRequires:	ruby-test-unit
BuildRequires:	ruby-test-unit-notify
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pkg-config module for Ruby.

%description -l pl.UTF-8
Moduł pkg-config dla języka Ruby.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.rdoc
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
