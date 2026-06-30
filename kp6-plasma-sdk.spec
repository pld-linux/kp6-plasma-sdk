#
# Conditional build:
%bcond_with	tests		# build with tests
# TODO:
# PackageKit qt5
#
%define		kdeplasmaver	6.7.2
%define		qtver		5.15.2
%define		kpname		plasma-sdk

Summary:	KDE Plasma Desktop
Name:		kp6-%{kpname}
Version:	6.7.2
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	c0abba5c8b5495dbac8bbdde3a6a823a
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	fontconfig-devel
BuildRequires:	kf6-attica-devel
BuildRequires:	kf6-kauth-devel
BuildRequires:	kf6-kcmutils-devel
BuildRequires:	kf6-kdbusaddons-devel
BuildRequires:	kf6-kdeclarative-devel
BuildRequires:	kf6-kdoctools-devel
BuildRequires:	kf6-kglobalaccel-devel
BuildRequires:	kf6-ki18n-devel
BuildRequires:	kf6-knewstuff-devel
BuildRequires:	kf6-knotifications-devel
BuildRequires:	kf6-knotifyconfig-devel
BuildRequires:	kf6-kpeople-devel
BuildRequires:	kf6-krunner-devel
BuildRequires:	kf6-kwallet-devel
BuildRequires:	kp6-libplasma-devel >= %{version}
BuildRequires:	kp6-plasma-activities-stats-devel >= %{version}
BuildRequires:	kp6-plasma5support-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xorg-driver-input-evdev-devel
BuildRequires:	xorg-driver-input-synaptics-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
%requires_eq_to Qt6Core Qt6Core-devel
Obsoletes:	kp5-%{kpname} < 6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
Applications useful for Plasma Development.

%description -l pl.UTF-8
Aplikacje przydatne przy rozwijaniu Plazmy.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post

%postun
/sbin/ldconfig
%update_desktop_database_postun

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lookandfeelexplorer
%attr(755,root,root) %{_bindir}/plasmaengineexplorer
%attr(755,root,root) %{_bindir}/plasmathemeexplorer
%attr(755,root,root) %{_bindir}/plasmoidviewer
%{_libdir}/qt6/plugins/kf6/ktexteditor/iconexplorerplugin.so
%{_mandir}/man1/kqml.1*
%{_mandir}/man1/plasmaengineexplorer.1*
%{_mandir}/man1/plasmoidviewer.1*
%{_datadir}/metainfo/org.kde.plasma.plasmoidviewershell.appdata.xml
%{_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell
%{_desktopdir}/org.kde.plasmaengineexplorer.desktop
%{_desktopdir}/org.kde.plasmoidviewer.desktop
%{_datadir}/metainfo/org.kde.plasmaengineexplorer.appdata.xml
%{_datadir}/metainfo/org.kde.plasmoidviewer.appdata.xml
%{_desktopdir}/org.kde.plasma.lookandfeelexplorer.desktop
%{_desktopdir}/org.kde.plasma.themeexplorer.desktop

%lang(ca) %{_mandir}/ca/man1/kqml.1*
%lang(ca) %{_mandir}/ca/man1/plasmaengineexplorer.1*
%lang(ca) %{_mandir}/ca/man1/plasmoidviewer.1*
%lang(de) %{_mandir}/de/man1/plasmaengineexplorer.1*
%lang(de) %{_mandir}/de/man1/plasmoidviewer.1*
%lang(el) %{_mandir}/el/man1/plasmaengineexplorer.1*
%lang(el) %{_mandir}/el/man1/plasmoidviewer.1*
%lang(es) %{_mandir}/es/man1/kqml.1*
%lang(es) %{_mandir}/es/man1/plasmaengineexplorer.1*
%lang(es) %{_mandir}/es/man1/plasmoidviewer.1*
%lang(et) %{_mandir}/et/man1/plasmaengineexplorer.1*
%lang(et) %{_mandir}/et/man1/plasmoidviewer.1*
%lang(fr) %{_mandir}/fr/man1/plasmaengineexplorer.1*
%lang(fr) %{_mandir}/fr/man1/plasmoidviewer.1*
%lang(id) %{_mandir}/id/man1/plasmaengineexplorer.1*
%lang(id) %{_mandir}/id/man1/plasmoidviewer.1*
%lang(it) %{_mandir}/it/man1/kqml.1*
%lang(it) %{_mandir}/it/man1/plasmaengineexplorer.1*
%lang(it) %{_mandir}/it/man1/plasmoidviewer.1*
%lang(nl) %{_mandir}/nl/man1/kqml.1*
%lang(nl) %{_mandir}/nl/man1/plasmaengineexplorer.1*
%lang(nl) %{_mandir}/nl/man1/plasmoidviewer.1*
%lang(pt) %{_mandir}/pt/man1/plasmaengineexplorer.1*
%lang(pt) %{_mandir}/pt/man1/plasmoidviewer.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kqml.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/plasmaengineexplorer.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/plasmoidviewer.1*
%lang(ru) %{_mandir}/ru/man1/plasmaengineexplorer.1*
%lang(ru) %{_mandir}/ru/man1/plasmoidviewer.1*
%lang(sl) %{_mandir}/sl/man1/plasmaengineexplorer.1*
%lang(sl) %{_mandir}/sl/man1/plasmoidviewer.1*
%lang(sv) %{_mandir}/sv/man1/plasmaengineexplorer.1*
%lang(sv) %{_mandir}/sv/man1/plasmoidviewer.1*
%lang(tr) %{_mandir}/tr/man1/kqml.1*
%lang(tr) %{_mandir}/tr/man1/plasmaengineexplorer.1*
%lang(tr) %{_mandir}/tr/man1/plasmoidviewer.1*
%lang(uk) %{_mandir}/uk/man1/kqml.1*
%lang(uk) %{_mandir}/uk/man1/plasmaengineexplorer.1*
%lang(uk) %{_mandir}/uk/man1/plasmoidviewer.1*
%{zsh_compdir}/_plasmoidviewer

%attr(755,root,root) %{_bindir}/iconexplorer
%attr(755,root,root) %{_bindir}/kqml
%{_desktopdir}/org.kde.iconexplorer.desktop
%{_iconsdir}/hicolor/scalable/apps/org.kde.iconexplorer.svg
%{_datadir}/metainfo/org.kde.plasma.iconexplorer.appdata.xml
%{zsh_compdir}/_kqml
