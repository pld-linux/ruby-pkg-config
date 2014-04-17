Summary:	pkg-config module for Ruby
Summary(pl.UTF-8):	Moduł pkg-config dla języka Ruby
Name:		ruby-pkg-config
Version:	1.1.5
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages
#Source0Download: http://rubyforge.org/frs/?group_id=3443
Source0:	https://github.com/ruby-gnome2/pkg-config/archive/%{version}/pkg-config-%{version}.tar.gz
# Source0-md5:	c9e4f92576a8ed08d26807059dbef862
URL:		https://github.com/ruby-gnome2/pkg-config
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.8
Requires:	ruby >= 1:1.8
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pkg-config module for Ruby.

%description -l pl.UTF-8
Moduł pkg-config dla języka Ruby.

%prep
%setup -q -n pkg-config-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

cp -pr lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.rdoc
%{ruby_rubylibdir}/pkg-config.rb
%{ruby_rubylibdir}/pkg-config
