Summary:	Pchar: A Tool for Measuring Net Path Characteristics
Summary(pl):	Pchar: Narzêdzie do okre¶lania charakterystyk po³±czeñ sieciowych
Name:		pchar
Version:	1.4
Release:	4
License:	GPL
Group:		Applications/Networking
Source0:	http://www.employees.org/~bmah/Software/pchar/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fixes.patch
URL:		http://www.employees.org/~bmah/Software/pchar/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	ucd-snmp-devel >= 4.2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pchar is a reimplementation of the pathchar utility written by Van
Jacobson, formerly of Lawrence Berkeley Laboratories. Both programs
attempt to characterize the bandwidth, latency, and loss of links
along an end-to-end path through the network.

%description -l pl
Pchar jest reimplementacj± programu pathchar napisanego przez Van
Jacobsona z Lawrence Berkeley Laboratories. Pozwala na okre¶lenie
charakterystyk przepustowo¶ci, opó¼nienia i strat pakietów na ³±czach
poprzez sieæ.

%prep
%setup -q
%patch0 -p1

%build
autoconf
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti -fno-implicit-templates"
%configure \
	--with-ipv6 \
	--without-pcap \
	--with-snmp
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
%doc *.gz
%attr(755,root,root) %{_bindir}/pchar
%{_mandir}/man8/*
