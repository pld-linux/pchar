Summary:	Pchar: A Tool for Measuring Internet Path Characteristics 
Summary(pl):	Pchar: Narzędzie do określania charakterystyk łącz Internetu
Name:		pchar
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://www.employees.org/~bmah/Software/pchar/%{name}-%{version}.tar.gz
URL:		http://www.employees.org/~bmah/Software/pchar/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
Pchar is a reimplementation of the pathchar utility written
by Van Jacobson, formerly of Lawrence Berkeley Laboratories. Both programs
attempt to characterize the bandwidth, latency, and loss of links along an
end-to-end path through the Internet.

%description -l pl
Pchar jest reimplementacją programu pathchar napisanego przez Van Jacobsona
z Lawrence Berkeley Laboratories. Pozwala na określenie charakterystyk
przepustowości, opóźnienia i strat pakietów na łączach poprzez Internet.

%prep
%setup -q
%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}
install pchar $RPM_BUILD_ROOT%{_bindir}/pchar
install pchar.8 $RPM_BUILD_ROOT%{_mandir}/man8/pchar.8

gzip -9nf README FAQ CHANGES
	
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz FAQ.gz CHANGES.gz

%attr(755,root,root) %{_bindir}/pchar
%{_mandir}/man8/*
