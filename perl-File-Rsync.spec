%define	module	File-Rsync
%define	name	perl-%{module}
%define	version	0.42
%define	release	%mkrel 4

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Perl module interface to rsync
License:	    GPL or Artistic
Group:		    Development/Perl
Url:		    http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.bz2
Patch0:		    %{name}-0.42.build.patch
BuildRequires:	perl-devel
BuildRequires:	rsync
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Perl Convenience wrapper for the rsync(1) program. Written for rsync-2.3.2 and
updated for rsync-2.6.0 but should perform properly with most recent versions.

%prep
%setup -n %{module}-%{version}
%patch

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changelog
%{perl_vendorarch}/File
%{_mandir}/*/*

