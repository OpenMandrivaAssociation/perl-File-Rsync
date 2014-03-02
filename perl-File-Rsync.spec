%define	upstream_name	 File-Rsync
%define	upstream_version 0.43

%define debug_package %{nil}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	6

Summary:	Perl module interface to rsync
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		%{name}-0.42.build.patch

BuildRequires:	perl-devel
BuildRequires:	rsync

%description
Perl Convenience wrapper for the rsync(1) program. Written for rsync-2.3.2 and
updated for rsync-2.6.0 but should perform properly with most recent versions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
