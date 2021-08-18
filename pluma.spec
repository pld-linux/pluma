Summary:	Pluma - MATE Text Editor
Summary(pl.UTF-8):	Pluma - edytor tekstu dla środowiska MATE
Name:		pluma
Version:	1.26.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Editors
Source0:	https://pub.mate-desktop.org/releases/1.26/%{name}-%{version}.tar.xz
# Source0-md5:	3d1dff6ae00d576574ef9a6308d6034b
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.63.2
BuildRequires:	automake >= 1:1.10
BuildRequires:	docbook-dtd412-xml
BuildRequires:	enchant2-devel >= 2
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gobject-introspection-devel >= 0.9.3
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gtksourceview4-devel >= 4.0.2
BuildRequires:	iso-codes >= 0.35
BuildRequires:	libpeas-devel >= 1.2.0
BuildRequires:	libpeas-gtk-devel >= 1.2.0
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 1:2.5.0
BuildRequires:	mate-common
BuildRequires:	pkgconfig
BuildRequires:	python3-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libICE-devel >= 1.0.0
BuildRequires:	xorg-lib-libSM-devel >= 1.0.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.50.0
Requires:	glib2 >= 1:2.50.0
Requires:	gobject-introspection >= 0.9.3
Requires:	gtk+3 >= 3.22
Requires:	gtksourceview4 >= 4.0.2
Requires:	iso-codes >= 0.35
Requires:	libpeas >= 1.2.0
Requires:	libpeas-gtk >= 1.2.0
Requires:	libxml2 >= 1:2.5.0
Requires:	python3-pygobject3 >= 3.0
Requires:	xorg-lib-libSM >= 1.0.0
Obsoletes:	mate-text-editor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pluma is a small and lightweight UTF-8 text editor for the MATE
environment. Based on gedit, the text editor for the GNOME 2
environment.

%description -l pl.UTF-8
Pluma to mały i lekki edytor tekstu w UTF-8 dla środowiska MATE. Jest
oparty na programie gedit - edytorze tekstu dla środowiska GNOME 2.

%package devel
Summary:	Header files for Pluma plugins development
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia wtyczek edytora Pluma
Group:		X11/Development/Libraries
# doesn't require base
Requires:	glib2-devel >= 1:2.50.0
Requires:	gtk+3-devel >= 3.22
Requires:	gtksourceview4-devel >= 4.0.2

%description devel
Header files for Pluma plugins development.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek edytora Pluma.

%package apidocs
Summary:	Pluma API documentation
Summary(pl.UTF-8):	Dokumentacja API edytora Pluma
Group:		Documentation
BuildArch:	noarch

%description apidocs
Pluma API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API edytora Pluma.

%prep
%setup -q

%{__sed} -i -e '1s|#!/usr/bin/python$|#!%{__python3}|' plugins/externaltools/data/switch-c.tool.in

grep -lr '#!/usr/bin/sh' . | xargs %{__sed} -i -e '1 s,#!/usr/bin/sh,#!/bin/sh,'

%build
mate-doc-common --copy
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-compile \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/pluma/plugins/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{frp,ie,jv,ku_IQ,pms}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/help/{frp,ie,ku_IQ}

%find_lang pluma --with-mate

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f pluma.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%attr(755,root,root) %{_bindir}/pluma
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/pluma
%endif
%attr(755,root,root) %{_libexecdir}/pluma/pluma-bugreport.sh
%dir %{_libdir}/pluma
%dir %{_libdir}/pluma/plugins
# C plugins
%attr(755,root,root) %{_libdir}/pluma/plugins/libdocinfo.so
%{_libdir}/pluma/plugins/docinfo.plugin
%attr(755,root,root) %{_libdir}/pluma/plugins/libfilebrowser.so
%{_libdir}/pluma/plugins/filebrowser.plugin
%attr(755,root,root) %{_libdir}/pluma/plugins/libmodelines.so
%{_libdir}/pluma/plugins/modelines.plugin
%attr(755,root,root) %{_libdir}/pluma/plugins/libsort.so
%{_libdir}/pluma/plugins/sort.plugin
%attr(755,root,root) %{_libdir}/pluma/plugins/libspell.so
%{_libdir}/pluma/plugins/spell.plugin
%attr(755,root,root) %{_libdir}/pluma/plugins/libtaglist.so
%{_libdir}/pluma/plugins/taglist.plugin
%attr(755,root,root) %{_libdir}/pluma/plugins/libtime.so
%{_libdir}/pluma/plugins/time.plugin
%attr(755,root,root) %{_libdir}/pluma/plugins/libtrailsave.so
%{_libdir}/pluma/plugins/trailsave.plugin
# Python plugins
%{_libdir}/pluma/plugins/externaltools
%{_libdir}/pluma/plugins/externaltools.plugin
%{_libdir}/pluma/plugins/pythonconsole
%{_libdir}/pluma/plugins/pythonconsole.plugin
%{_libdir}/pluma/plugins/quickopen
%{_libdir}/pluma/plugins/quickopen.plugin
%{_libdir}/pluma/plugins/snippets
%{_libdir}/pluma/plugins/snippets.plugin
%{_libdir}/girepository-1.0/Pluma-1.0.typelib
%{_datadir}/metainfo/pluma.appdata.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.filebrowser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.pythonconsole.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.spell.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.time.gschema.xml
%{_datadir}/pluma
%{_desktopdir}/pluma.desktop
%{_mandir}/man1/pluma.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/pluma
%{_pkgconfigdir}/pluma.pc
%{_datadir}/gir-1.0/Pluma-1.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/pluma
