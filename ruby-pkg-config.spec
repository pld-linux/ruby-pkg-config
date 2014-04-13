Summary:	pkg-config module for Ruby
Summary(pl.UTF-8):	Moduł pkg-config dla języka Ruby
Name:		ruby-pkg-config
Version:	1.1.1
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages
#Source0Download: http://rubyforge.org/frs/?group_id=3443
Source0:	http://rubyforge.org/frs/download.php/74790/pkg-config-%{version}.tgz
# Source0-md5:	6f20e3ac87490556a56f0a057fbdab1a
URL:		http://rubyforge.org/projects/cairo/
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

%build
ruby extconf.rb

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	RUBYLIBDIR=$RPM_BUILD_ROOT%{ruby_rubylibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.rdoc
%{ruby_rubylibdir}/pkg-config.rb
