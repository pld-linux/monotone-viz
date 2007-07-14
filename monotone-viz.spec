# TODO:
# - change static linking with libcrypto into dynamic one.
Summary:	Visualization of monotone ancestry graphs
Summary(pl.UTF-8):	Wizualizacja grafów dziedziczenia monotone
Name:		monotone-viz
Version:	0.15
Release:	1.1
License:	GPL
Group:		Development/Version Control
Source0:	http://oandrieu.nerim.net/monotone-viz/%{name}-%{version}-nolablgtk.tar.gz
# Source0-md5:	3a26011f6cc1aeb7fd50e31ed7f33333
URL:		http://oandrieu.nerim.net/monotone-viz/
BuildRequires:	gtk+2-devel >= 1:2.2.0
BuildRequires:	graphviz
BuildRequires:	ocaml
BuildRequires:	ocaml-camlp4
BuildRequires:	ocaml-lablgtk2-devel >= 2.4.0
BuildRequires:	ocaml-lablgtk2-gnome-devel
BuildRequires:	openssl-devel
# !!!!!! FIXME !!!!!
BuildRequires:	openssl-static
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ application for visualization of monotone ancestry graphs.

%description -l pl.UTF-8
Aplikacja GTK+ do wizualizacji grafów dziedziczenia monotone.

%prep
%setup -q

%build
%{__autoconf}
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
%doc NEWS README %{name}.style.sample
%attr(755,root,root) %{_bindir}/%{name}
