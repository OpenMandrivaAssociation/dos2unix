Summary:	Converts DOS-style EOLs to UNIX-style EOLs and vice versa
Name:		dos2unix
Version:	7.3
Release:	2
License:	BSD
Group:		Text tools
Url:		http://waterlan.home.xs4all.nl/dos2unix.html
Source0:	http://waterlan.home.xs4all.nl/dos2unix/%{name}-%{version}.tar.gz
BuildRequires:	gettext
BuildRequires:	perl-devel
Provides:	unix2dos = %{EVRD}
Provides:	mac2unix = %{EVRD}
Provides:	unix2mac = %{EVRD}

%description
A filter used to convert DOS-style EOLs to UNIX-style EOLs and vice
versa (EOL - End Of Line character).

This package contains updated Benjamin Lin's implementations of dos2unix
and unix2dos.

Benjamin Lin's implementations of dos2unix and unix2dos are a part of many
Linux distributions such as RedHat, Fedora, Suse, Gentoo and others.
This update includes all RedHat patches and fixes several other problems.
Internationalization has been added and ports to various OS have been made.

%prep
%setup -q

%build
%make CC=%{__cc}

%install
%makeinstall_std

# doc is installed two times in doc dir
mv %{buildroot}%{_docdir}/%{name}-%{version}/ %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc %{_docdir}/%{name}/*
%{_bindir}/dos2unix
%{_bindir}/unix2dos
%{_bindir}/mac2unix
%{_bindir}/unix2mac
%{_mandir}/man1/*.1*
%{_mandir}/es/man1/*.1*
%{_mandir}/de/man1/*.1*
%{_mandir}/uk/man1/*.1*
%{_mandir}/fr/man1/*.1*
%{_mandir}/pl/man1/*.1*
%{_mandir}/pt_BR/man1/*.1*
%{_mandir}/nl/man1/*.1*
