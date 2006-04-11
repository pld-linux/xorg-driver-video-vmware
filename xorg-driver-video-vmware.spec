Summary:	X.org video driver for VMware virtual video cards
Summary(pl):	Sterownik obrazu X.org dla wirtualnych kart graficznych VMware
Name:		xorg-driver-video-vmware
Version:	10.13.0
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vmware-%{version}.tar.bz2
# Source0-md5:	0b8951d07af049b22c90a5a185c897c2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for VMware virtual video cards.

%description -l pl
Sterownik obrazu X.org dla wirtualnych kart graficznych VMware.

%prep
%setup -q -n xf86-video-vmware-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_mandir}/man4/vmware.4*
