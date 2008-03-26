# TODO
# - kill: Requires: /bin/bash
Summary:	Event-based init daemon
Summary(pl.UTF-8):	Demon init oparty na zdarzeniach
Name:		einit
Version:	0.40.0
Release:	0.1
License:	GPL v2
Group:		Base
Source0:	http://einit.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	92c65507a4e60993053649c742201605
URL:		http://www.einit.org/
BuildRequires:	expat-devel
BuildRequires:	libnl-devel >= 1.0-0.pre6.3
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	scons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	/usr/include
%define		_prefix	/

%description
eINIT is a replacement for SysVinit, an init system used on UNIX-based
operating systems. eINIT is designed with speed in mind. Many testers
claim that their systems boot up in 30 seconds, whereas SysVinit takes
around two minutes to boot.

%description -l pl.UTF-8
eINIT to zamiennik systemu SysVinit używanego w systemach operacyjnych
opartych na Uniksie. eINIT został zaprojektowany z myślą o szybkości.
Wielu testujących twierdzi, że ich systemy uruchamiają się w 30
sekund, podczas gdy SysVinit potrzebował na to około dwóch minut.

%package devel
Summary:	Header files for eINIT
Summary(pl.UTF-8):	Pliki nagłówkowe systemu eINIT
Group:		Development/Libraries
# doesn't require base

%description devel
eINIT header files for developing plugins for eINIT.

%description devel -l pl.UTF-8
Pliki nagłówkowe systemu eINIT do tworzenia wtyczek dla niego.

%prep
%setup -q

%build
export CFLAGS=-I%{_includedir}/ncurses
export CC='%{__cc}'
export CXX='%{__cxx}'
export CXXFLAGS='%{rpmcxxflags}'
%scons \
	destdir=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	os_cc=1 \
	os_cxx=1 \
	os_cxxflags=1

%install
rm -rf $RPM_BUILD_ROOT

export CFLAGS=-I%{_includedir}/ncurses
export CC='%{__cc}'
export CXX='%{__cxx}'
export CXXFLAGS='%{rpmcxxflags}'
%scons install \
	destdir=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	os_cc=1 \
	os_cxx=1 \
	os_cxxflags=1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
#/etc/dbus-1/system.d/einit.conf
%dir %{_sysconfdir}/einit
%{_sysconfdir}/einit/*.xml
%{_sysconfdir}/einit/rules.edev
%{_sysconfdir}/einit/subsystems.d

%attr(755,root,root) %{_sbindir}/einit
%attr(755,root,root) %{_sbindir}/einit-sysvd

%attr(755,root,root) %{_libdir}/libeinit++.so
%attr(755,root,root) %{_libdir}/libeinit.so

%dir %{_libdir}/einit
%dir %{_libdir}/einit/bin
%attr(755,root,root) %{_libdir}/einit/bin/einit-core
%attr(755,root,root) %{_libdir}/einit/bin/einit-feedback
%attr(755,root,root) %{_libdir}/einit/bin/einit-helper
%attr(755,root,root) %{_libdir}/einit/bin/einit-log
%attr(755,root,root) %{_libdir}/einit/bin/last-rites

%{_libdir}/einit/defaults
%{_libdir}/einit/einit.xml

%dir %{_libdir}/einit/bootstrap
%attr(755,root,root) %{_libdir}/einit/bootstrap/bootstrap-configuration-stree.so
%attr(755,root,root) %{_libdir}/einit/bootstrap/bootstrap-configuration-xml-expat.so

%dir %{_libdir}/einit/modules
%attr(755,root,root) %{_libdir}/einit/modules/bundle-base.so
%attr(755,root,root) %{_libdir}/einit/modules/bundle-compatibility.so
%attr(755,root,root) %{_libdir}/einit/modules/bundle-linux.so
%attr(755,root,root) %{_libdir}/einit/modules/ipc-9p.so
%attr(755,root,root) %{_libdir}/einit/modules/linux-urandom.so
%attr(755,root,root) %{_libdir}/einit/modules/module-logic-v4.so
%attr(755,root,root) %{_libdir}/einit/modules/shadow-exec.so

%dir %{_libdir}/einit/schemata
%{_libdir}/einit/schemata/data-types.rnc
%{_libdir}/einit/schemata/einit-module.rnc
%{_libdir}/einit/schemata/einit-network.rnc
%{_libdir}/einit/schemata/einit.rnc

%dir %{_libdir}/einit/scripts
%attr(755,root,root) %{_libdir}/einit/scripts/import-fstab
%attr(755,root,root) %{_libdir}/einit/scripts/make-initramfs

%files devel
%defattr(644,root,root,755)
%{_includedir}/einit
%{_includedir}/einit-modules
