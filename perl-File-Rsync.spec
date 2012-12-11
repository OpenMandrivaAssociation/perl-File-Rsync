%define	upstream_name	 File-Rsync
%define	upstream_version 0.43

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl module interface to rsync
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		%{name}-0.42.build.patch

BuildRequires:	perl-devel
BuildRequires:	rsync
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changelog
%{perl_vendorarch}/File
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.430.0-5
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-4mdv2011.0
+ Revision: 555836
- rebuild for perl 5.12

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.430.0-3mdv2011.0
+ Revision: 555464
- rebuild

* Mon Aug 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-2mdv2010.0
+ Revision: 420434
- force submit
- update to 0.42

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.420.0-1mdv2010.0
+ Revision: 403178
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.42-6mdv2009.0
+ Revision: 256995
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.42-4mdv2008.1
+ Revision: 152079
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-3mdv2008.0
+ Revision: 86402
- rebuild


* Sat Sep 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-2mdv2007.0
- buildrequires rsync

* Thu Dec 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-1mdk
- first mdk release

