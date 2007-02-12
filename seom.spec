Summary:	seom video capturing library
Summary(pl.UTF-8):   Biblioteka przechwytywania video seom
Name:		seom
Version:	20070203
Release:	1
License:	GPL (?)
Group:		Libraries
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	84b07eb7ccfbc3628d6c23fe11d17d32
Source1:	%{name}-backup
URL:		http://neopsis.com/projects/seom/
BuildRequires:	OpenGL-devel
BuildRequires:	xorg-lib-libXv-devel
%ifarch %{ix86} %{x8664}
BuildRequires:	yasm
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
seom video capturing library.

%description -l pl.UTF-8
Biblioteka przechwytywania video seom.

%package devel
Summary:	Header files for seom
Summary(pl.UTF-8):   Pliki nałówkowe seom
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The header files are only needed for development of programs using the
seom library.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe, przeznaczone dla
programistów używających biblioteki seom.

%package utils
Summary:	seom utilities
Summary(pl.UTF-8):   Narzędzia seom
Group:		Applications
Suggests:	mencoder

%description utils
seom utilities.

%description utils -l pl.UTF-8
Narzędzia seom.

%prep
%setup -q

%build
./configure --prefix="%{_prefix}"

%{__make} \
	CC="%{__cc}" \
	CFLAGS="-Iinclude -std=c99 -W -Wall %{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	LIBDIR="%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	LIBDIR="%{_lib}"

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/seom-backup

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libseom.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libseom.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libseom.so
%{_pkgconfigdir}/seom.pc
%{_includedir}/seom

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
