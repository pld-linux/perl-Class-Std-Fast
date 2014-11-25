#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Class
%define	pnam	Std-Fast
%include	/usr/lib/rpm/macros.perl
Summary:	Class::Std::Fast - faster but less secure than Class::Std
Name:		perl-Class-Std-Fast
Version:	0.0.8
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-v%{version}.tar.gz
# Source0-md5:	d06d084cb84f295b0aabf2eee78ef746
URL:		http://search.cpan.org/dist/Class-Std-Fast/
BuildRequires:	perl-Class-Std >= 0.0.9
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Std::Fast allows you to use the beautiful API of Class::Std in
a faster way than Class::Std does. You can get the object's ident via
scalarifiyng your object. Getting the objects ident is still possible
via the ident method, but it's faster to scalarify your object.

%prep
%setup -q -n %{pdir}-%{pnam}-v%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Class/Std
%{perl_vendorlib}/Class/Std/*.pm
%dir %{perl_vendorlib}/Class/Std/Fast
%{perl_vendorlib}/Class/Std/Fast/*.pm
%{_mandir}/man3/*
