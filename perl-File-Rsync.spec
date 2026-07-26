%define	upstream_name	 File-Rsync
%define debug_package %{nil}

Name:       perl-%{upstream_name}
Version:    0.49
Release:	2

Summary:	Perl module interface to rsync
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/File-Rsync
Source0:    https://cpan.metacpan.org/authors/id/L/LE/LEAKIN/File-Rsync-%{version}.tar.gz
Patch0:		%{name}-0.42.build.patch

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	rsync

%description
Perl Convenience wrapper for the rsync(1) program. Written for rsync-2.3.2 and
updated for rsync-2.6.0 but should perform properly with most recent versions.

%prep
%setup -q -n %{upstream_name}-%{version}
%patch0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
%makeinstall_std

%files 
%doc README Changelog
%{perl_vendorarch}/File
%{_mandir}/*/*
