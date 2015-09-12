%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	2.6
%define major	1
%define pkgname	libgnomecanvasmm
%define libname	%mklibname gnomecanvasmm %{api} %{major}
%define devname %mklibname -d gnomecanvasmm %{api}

Summary: 	A C++ interface for GNOME 2 canvas library
Name:	 	%{pkgname}%{api}
Version: 	2.26.0
Release: 	16
License: 	LGPLv2+
Group:   	System/Libraries
Url:     	http://gtkmm.sourceforge.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnomecanvasmm/%{url_ver}/%{pkgname}-%{version}.tar.bz2

BuildRequires:	doxygen
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(libgnomecanvas-2.0)

%description
This package provides a C++ interface for GNOME canvas library.  It is a
subpackage of the gnomemm project.  The interface provides a convenient
interface for C++ programmers to create GNOME GUIs with GTK+'s flexible
object-oriented framework.

%package	-n %{libname}
Summary:	A C++ interface for GNOME 2 canvas library
Group:		System/Libraries
Provides:	%{pkgname} = %{version}-%{release}

%description	-n %{libname}
This package provides a C++ interface for GNOME canvas library.  It is a
subpackage of the gnomemm project.  The interface provides a convenient
interface for C++ programmers to create GNOME GUIs with GTK+'s flexible
object-oriented framework.

%package	-n %{devname}
Summary:	Headers and development files of GNOME 2 canvas library
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%mklibname -d gnomecanvasmm %{api} 1

%description	-n %{devname}
This package contains the headers and various development files needed
for compiling or development of applications that wants C++ interface
of GNOME 2 canvas library.

%package	doc
Summary:	Documentation of %{pkgname} library
Group:		Books/Other

%description	doc
This package provides API documentation of %{pkgname} library.

%prep
%setup -qn %{pkgname}-%{version}

%build
%configure2_5x --disable-static
%make 

### Build doc
pushd docs/reference
  sed -i -e 's/^(HAVE_DOT.*=) YES$/$1 NO/' Doxyfile
  make all
popd

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libgnomecanvasmm-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/%{pkgname}-%{api}
%{_libdir}/pkgconfig/*.pc

%files doc
%doc docs/reference/html

