%define version 2.22.0
%define release %mkrel 1

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
License: 	LGPL
Group:   	System/Libraries
URL:     	http://gtkmm.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

Source:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2

BuildRequires:	gtkmm2.4-devel >= %{gtkmm_version}
BuildRequires:	libgnomecanvas2-devel >= %{libgnomecanvas_version}
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
rm -rf %{buildroot}
%makeinstall_std
find %buildroot -name \*.la|xargs chmod 644

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc COPYING README
%{_libdir}/libgnomecanvasmm-%{api_version}.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/%{pkgname}-%{api_version}
%{_libdir}/pkgconfig/*.pc

%files doc
%defattr(-, root, root)
%doc docs/reference/html


