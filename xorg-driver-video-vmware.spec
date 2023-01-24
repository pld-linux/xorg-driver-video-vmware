Summary:	X.org video driver for VMware virtual video cards
Summary(pl.UTF-8):	Sterownik obrazu X.org dla wirtualnych kart graficznych VMware
Name:		xorg-driver-video-vmware
Version:	13.4.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-vmware-%{version}.tar.xz
# Source0-md5:	8c9ec4decaa262eb33a474219232bb1b
URL:		https://xorg.freedesktop.org/
BuildRequires:	Mesa-libxatracker-devel >= 8
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4.96
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.12.0
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	libdrm >= 2.4.96
Requires:	xorg-xserver-server >= 1.12.0
Provides:	xorg-driver-video
Obsoletes:	X11-driver-vmware < 1:7.0.0
Obsoletes:	XFree86-driver-vmware < 1:7.0.0
ExclusiveArch:	%{ix86} %{x8664} x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for VMware virtual video cards. It auto-detects the
version of any virtual VMware SVGA adapter.

%description -l pl.UTF-8
Sterownik obrazu X.org dla wirtualnych kart graficznych VMware.
Wykrywa automatycznie wersję dowolnej wirtualnej karty SVGA VMware.

%prep
%setup -q -n xf86-video-vmware-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-vmwarectrl-client

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/vmwarectrl
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_mandir}/man4/vmware.4*
