Summary:	Visualization of monotone ancestry graphs
Summary(pl):	Wizualizacja grafów dziedziczenia monotone
Name:		monotone-viz
Version:	0.10
Release:	1
License:	GPL
Group:		Development/Version Control
Source0:	http://oandrieu.nerim.net/monotone-viz/%{name}-%{version}.tar.gz
# Source0-md5:	1dfe3563f84e9be1ef5db2bf9e87bcd7
URL:		http://oandrieu.nerim.net/monotone-viz/
BuildRequires:	gtk+2-devel >= 1:2.2.0
BuildRequires:	graphviz
BuildRequires:	ocaml
BuildRequires:	ocaml-camlp4
BuildRequires:	ocaml-lablgtk >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ application for visualization of monotone ancestry graphs.

%description -l pl
Aplikacja GTK+ do wizualizacji grafów dziedziczenia monotone.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc FIXME
%attr(755,root,root) %{_bindir}/FIXME
