Summary:	Pluma - MATE Text Editor
Summary(pl.UTF-8):	Pluma - edytor tekstu dla środowiska MATE
Name:		pluma
Version:	1.8.0
Release:	2
License:	GPL v2+
Group:		X11/Applications/Editors
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	cdebd8c3e32bb4624354f2b435fecc23
Patch0:		%{name}-python.patch
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.63.2
BuildRequires:	automake >= 1:1.10
BuildRequires:	docbook-dtd412-xml
BuildRequires:	enchant-devel >= 1.2.0
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gtk+2-devel >= 2:2.20
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gtksourceview2-devel >= 2.9.7
BuildRequires:	intltool >= 0.40.0
BuildRequires:	iso-codes >= 0.35
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 1:2.5.0
BuildRequires:	mate-common
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-gtksourceview2-devel >= 2.9.2
BuildRequires:	python-pygobject-devel >= 2.15.4
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	xorg-lib-libSM-devel >= 1.0.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	enchant >= 1.2.0
Requires:	glib2 >= 1:2.26.0
Requires:	gtk+2 >= 2:2.20
Requires:	gtksourceview2 >= 2.9.7
Requires:	iso-codes >= 0.35
Requires:	libxml2 >= 1:2.5.0
Requires:	python-gtksourceview2 >= 2.9.2
Requires:	python-pygobject >= 2.15.4
Requires:	python-pygtk-gtk >= 2:2.12.0
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
Requires:	glib2-devel >= 1:2.26.0
Requires:	gtk+2-devel >= 2:2.20
Requires:	gtksourceview2-devel >= 2.9.7

%description devel
Header files for Pluma plugins development.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek edytora Pluma.

%package apidocs
Summary:	Pluma API documentation
Summary(pl.UTF-8):	Dokumentacja API edytora Pluma
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Pluma API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API edytora Pluma.

%prep
%setup -q
%patch0 -p1

%build
mate-doc-common --copy
%{__intltoolize}
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/pluma/{plugin-loaders,plugins}/*.la

# mate < 1.5 did not exist in PLD, avoid dependency on mate-conf
%{__rm} $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/pluma.convert

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/cmn

%find_lang pluma --with-mate --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f pluma.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/pluma
%dir %{_libdir}/pluma
%attr(755,root,root) %{_libdir}/pluma/pluma-bugreport.sh
%dir %{_libdir}/pluma/plugin-loaders
%attr(755,root,root) %{_libdir}/pluma/plugin-loaders/libcloader.so
%attr(755,root,root) %{_libdir}/pluma/plugin-loaders/libpythonloader.so
%dir %{_libdir}/pluma/plugins
# C plugins
%attr(755,root,root) %{_libdir}/pluma/plugins/libchangecase.so
%{_libdir}/pluma/plugins/changecase.pluma-plugin
%attr(755,root,root) %{_libdir}/pluma/plugins/libdocinfo.so
%{_libdir}/pluma/plugins/docinfo.pluma-plugin
%attr(755,root,root) %{_libdir}/pluma/plugins/libfilebrowser.so
%{_libdir}/pluma/plugins/filebrowser.pluma-plugin
%attr(755,root,root) %{_libdir}/pluma/plugins/libmodelines.so
%{_libdir}/pluma/plugins/modelines.pluma-plugin
%attr(755,root,root) %{_libdir}/pluma/plugins/libsort.so
%{_libdir}/pluma/plugins/sort.pluma-plugin
%attr(755,root,root) %{_libdir}/pluma/plugins/libspell.so
%{_libdir}/pluma/plugins/spell.pluma-plugin
%attr(755,root,root) %{_libdir}/pluma/plugins/libtaglist.so
%{_libdir}/pluma/plugins/taglist.pluma-plugin
%attr(755,root,root) %{_libdir}/pluma/plugins/libtime.so
%{_libdir}/pluma/plugins/time.pluma-plugin
# Python plugins
%{_libdir}/pluma/plugins/externaltools
%{_libdir}/pluma/plugins/externaltools.pluma-plugin
%{_libdir}/pluma/plugins/pythonconsole
%{_libdir}/pluma/plugins/pythonconsole.pluma-plugin
%{_libdir}/pluma/plugins/quickopen
%{_libdir}/pluma/plugins/quickopen.pluma-plugin
%{_libdir}/pluma/plugins/snippets
%{_libdir}/pluma/plugins/snippets.pluma-plugin
%{_datadir}/glib-2.0/schemas/org.mate.pluma.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.filebrowser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.time.gschema.xml
%{_datadir}/pluma
%{_desktopdir}/pluma.desktop
%{_mandir}/man1/pluma.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/pluma
%{_pkgconfigdir}/pluma.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/pluma
