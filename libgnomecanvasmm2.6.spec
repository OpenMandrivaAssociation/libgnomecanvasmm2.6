%define version 2.26.0
%define release %mkrel 6

%define libgnomecanvas_version 2.6.0
%define gtkmm_version 2.4.0

%define major	1
%define api_version 2.6

%define pkgname	libgnomecanvasmm
%define libname_orig	%mklibname gnomecanvasmm %api_version
%define libname		%mklibname gnomecanvasmm %api_version %{major}
%define develname %mklibname -d gnomecanvasmm %api_version

Name:	 	%{pkgname}%{api_version}
Summary: 	A C++ interface for GNOME 2 canvas library
Version: 	%{version}
Release: 	%{release}
License: 	LGPLv2+
Group:   	System/Libraries
URL:     	http://gtkmm.sourceforge.net/

Source:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2

BuildRequires:	gtkmm2.4-devel >= %{gtkmm_version}
BuildRequires:	pkgconfig(libgnomecanvas-2.0) >= %{libgnomecanvas_version}
BuildRequires:	doxygen

%description
This package provides a C++ interface for GNOME canvas library.  It is a
subpackage of the gnomemm project.  The interface provides a convenient
interface for C++ programmers to create GNOME GUIs with GTK+'s flexible
object-oriented framework.

%package	-n %{libname}
Summary:	A C++ interface for GNOME 2 canvas library
Group:		System/Libraries
Provides:	%{libname_orig} = %{version}-%{release}
Provides:	%{pkgname} = %{version}-%{release}

%description	-n %{libname}
This package provides a C++ interface for GNOME canvas library.  It is a
subpackage of the gnomemm project.  The interface provides a convenient
interface for C++ programmers to create GNOME GUIs with GTK+'s flexible
object-oriented framework.

%package	-n %develname
Summary:	Headers and development files of GNOME 2 canvas library
Group:		Development/GNOME and GTK+
Provides:	%name-devel = %{version}-%{release}
Provides:	%{pkgname}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes: %mklibname -d gnomecanvasmm %api_version 1

%description	-n %develname
This package contains the headers and various development files needed
for compiling or development of applications that wants C++ interface
of GNOME 2 canvas library.

%package	doc
Summary:	Documentation of %{pkgname} library
Group:		Books/Other

%description	doc
This package provides API documentation of %{pkgname} library.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x --enable-static
%make 

### Build doc
pushd docs/reference
  perl -pi -e 's/^(HAVE_DOT.*=) YES$/$1 NO/' Doxyfile
  make all
popd

%install
%makeinstall_std
find %buildroot -name \*.la|xargs chmod 644

%files -n %{libname}
%doc COPYING README
%{_libdir}/libgnomecanvasmm-%{api_version}.so.%{major}*

%files -n %develname
%doc AUTHORS COPYING ChangeLog NEWS
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/%{pkgname}-%{api_version}
%{_libdir}/pkgconfig/*.pc

%files doc
%doc docs/reference/html


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.26.0-5mdv2011.0
+ Revision: 661466
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 2.26.0-4mdv2011.0
+ Revision: 602553
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.26.0-3mdv2010.1
+ Revision: 520841
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.26.0-2mdv2010.0
+ Revision: 425553
- rebuild

* Mon Mar 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355974
- update to new version 2.26.0

* Mon Aug 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.1-1mdv2009.0
+ Revision: 263294
- new version
- update license

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.22.0-2mdv2009.0
+ Revision: 222656
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Mar 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 182998
- new version

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 2.20.0-2mdv2008.1
+ Revision: 150609
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 85542
- new version
- new devel name

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 2.16.0-3mdv2008.0
+ Revision: 64756
- rebuild


* Tue Jan 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-2mdv2007.0
+ Revision: 103076
- Import libgnomecanvasmm2.6

* Tue Jan 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-2mdv2007.1
- Rebuild

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New release 2.16.0

* Tue Apr 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.0-1mdk
- New release 2.14.0
- use mkrel

* Sun Oct 09 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.0-1mdk
- New release 2.12.0

* Tue May 10 2005 Götz Waschk <waschk@mandriva.org> 2.10.0-2mdk
- fix devel provides

* Mon Mar 07 2005 Götz Waschk <waschk@linux-mandrake.com> 2.10.0-1mdk
- reenable libtoolize
- source URL
- New release 2.10.0

* Wed Nov 10 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.0-1mdk
- fix source URL
- New release 2.8.0

* Fri Jun 18 2004 Abel Cheung <deaddog@mandrakesoft.com> 2.6.1-1mdk
- New release 2.6.1

* Thu Apr 29 2004 Abel Cheung <deaddog@deaddog.org> 2.6.0-1mdk
- New major release

* Thu Apr 29 2004 Abel Cheung <deaddog@deaddog.org> 2.0.1-5mdk
- Rebuild
- Split documentation

* Mon Feb 09 2004 Abel Cheung <deaddog@deaddog.org> 2.0.1-4mdk
- Fix BuildRequires

