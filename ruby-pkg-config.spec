#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	pkg-config
Summary:	pkg-config module for Ruby
Summary(pl.UTF-8):	Moduł pkg-config dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.4.1
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages
# tarballs: https://github.com/ruby-gnome/pkg-config/releases
# gems: https://rubygems.org/gems/pkg-config
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	1622d8b28b115e997cc5c4ffd20c0bd7
URL:		https://github.com/ruby-gnome2/pkg-config
BuildRequires:	pkgconfig
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-modules >= 1:1.8
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
