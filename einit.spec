Summary:	Event-based init daemon
Name:		einit
Version:	0.24.2
Release:	0.1
License:	GPL v2
Group:		Base
Source0:	http://download.berlios.de/einit/%{name}-%{version}.tar.bz2
# Source0-md5:	3434c56760a8b3d27856a794367e09e4
URL:		http://www.einit.org/project/einit-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/
%define		_includedir	/usr/include

%description
eINIT is a replacement for SysVinit, an init system used on UNIX-based
operating systems. eINIT is designed with speed in mind. Many testers
claim that their systems boot up in 30 seconds, whereas sysvinit takes
around two minutes to boot.

%package devel
Summary:	Header files for eINIT
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
eINIT header files for developing plugins for eINIT.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
/etc/dbus-1/system.d/einit.conf
%{_sysconfdir}/einit/*.xml
%{_sysconfdir}/einit/subsystems.d

%attr(755,root,root) %{_sbindir}/einit
%attr(755,root,root) %{_sbindir}/einit-control

%dir %{_libdir}/einit
%dir %{_libdir}/einit/bin
%attr(755,root,root) %{_libdir}/einit/bin/crash-handler
%{_libdir}/einit/defaults
%{_libdir}/einit/einit.xml

%dir %{_libdir}/einit/modules
%attr(755,root,root) %{_libdir}/einit/modules/compatibility-sysv-initctl.so
%attr(755,root,root) %{_libdir}/einit/modules/compatibility-sysv-utmp.so
%attr(755,root,root) %{_libdir}/einit/modules/cron.so
%attr(755,root,root) %{_libdir}/einit/modules/exec.so
%attr(755,root,root) %{_libdir}/einit/modules/external.so
%attr(755,root,root) %{_libdir}/einit/modules/feedback-aural-festival.so
%attr(755,root,root) %{_libdir}/einit/modules/feedback-aural.so
%attr(755,root,root) %{_libdir}/einit/modules/feedback-visual-fbsplash.so
%attr(755,root,root) %{_libdir}/einit/modules/feedback-visual-textual.so
%attr(755,root,root) %{_libdir}/einit/modules/fqdn.so
%attr(755,root,root) %{_libdir}/einit/modules/ipc-configuration.so
%attr(755,root,root) %{_libdir}/einit/modules/ipc-core-helpers.so
%attr(755,root,root) %{_libdir}/einit/modules/ipc.so
%attr(755,root,root) %{_libdir}/einit/modules/linux-module-kernel.so
%attr(755,root,root) %{_libdir}/einit/modules/linux-mount.so
%attr(755,root,root) %{_libdir}/einit/modules/linux-process.so
%attr(755,root,root) %{_libdir}/einit/modules/linux-sysconf.so
%attr(755,root,root) %{_libdir}/einit/modules/module-network.so
%attr(755,root,root) %{_libdir}/einit/modules/module-transformations.so
%attr(755,root,root) %{_libdir}/einit/modules/module-xml.so
%attr(755,root,root) %{_libdir}/einit/modules/mount.so
%attr(755,root,root) %{_libdir}/einit/modules/parse-sh.so
%attr(755,root,root) %{_libdir}/einit/modules/process.so
%attr(755,root,root) %{_libdir}/einit/modules/scheduler.so
%attr(755,root,root) %{_libdir}/einit/modules/shadow-exec.so
%attr(755,root,root) %{_libdir}/einit/modules/tty.so

%dir %{_libdir}/einit/scripts
%attr(755,root,root) %{_libdir}/einit/scripts/configuration
%attr(755,root,root) %{_libdir}/einit/scripts/einit.d_erc.sh
%attr(755,root,root) %{_libdir}/einit/scripts/install-config
%attr(755,root,root) %{_libdir}/einit/scripts/update_conf.d.sh
%attr(755,root,root) %{_libdir}/einit/scripts/write_devroot_rules

%files devel
%defattr(644,root,root,755)
%{_includedir}/einit
%{_includedir}/einit-modules
