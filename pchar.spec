Summary:	Pchar: A Tool for Measuring Net Path Characteristics
Summary(pl.UTF-8):	Pchar: Narzędzie do określania charakterystyk połączeń sieciowych
Name:		pchar
Version:	1.5
Release:	0.1
License:	BSD
Group:		Applications/Networking
Source0:	http://www.employees.org/~bmah/Software/pchar/%{name}-%{version}.tar.gz
# Source0-md5:	1199a30db4b128b9acbc6979ca9b53e6
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-build.patch
Patch2:		%{name}-gcc4.patch
URL:		http://www.employees.org/~bmah/Software/pchar/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	net-snmp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pchar is a reimplementation of the pathchar utility written by Van
Jacobson, formerly of Lawrence Berkeley Laboratories. Both programs
attempt to characterize the bandwidth, latency, and loss of links
along an end-to-end path through the network.

%description -l pl.UTF-8
Pchar jest reimplementacją programu pathchar napisanego przez Van
Jacobsona z Lawrence Berkeley Laboratories. Pozwala na określenie
charakterystyk przepustowości, opóźnienia i strat pakietów na łączach
poprzez sieć.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README FAQ CHANGES
%attr(755,root,root) %{_bindir}/pchar
%{_mandir}/man8/*
