Name:		vgabios
Version:	0.6c
Release:	1
Summary:	LGPL implementation of a vga video bios

Group:		Emulators		
License:	LGPLv2
URL:		http://www.nongnu.org/vgabios/
Source0:	http://savannah.gnu.org/download/%{name}/%{name}-%{version}.tgz
Patch01:		0001-Makefile-cleanup.patch
Patch02:		0002-Add-defines-for-PCI-IDs.patch
Patch03:		0003-Add-qemu-stdvga-pci-bios.patch
Patch04:		0004-update-pci_get_lfb_addr-for-vmware-vga.patch 
Patch05:		0005-Add-qemu-vmware-vga-pci-bios.patch 
Patch06:		0006-Add-qemu-qxl-vga-pci-bios.patch 

BuildRequires:	dev86
BuildArch: noarch

%description
vgabios is an LPGL implementation of a bios for a video card.
It is tied to plex86/bochs, althoug it will likely work on other
emulators. It is not intended for use in real cards.


%prep 
%setup -q -n %{name}-%{version}

%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch04 -p1
%patch05 -p1
%patch06 -p1

%build 
make clean
make biossums %{?_smp_mflags}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vgabios
install -m 0644 VGABIOS-lgpl-*.bin $RPM_BUILD_ROOT%{_datadir}/vgabios 


%files
%dir %{_datadir}/vgabios/
%doc README COPYING
%{_datadir}/vgabios/VGABIOS-lgpl-latest.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.cirrus.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.qxl.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.stdvga.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.vmware.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.cirrus.debug.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.debug.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.qxl.debug.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.stdvga.debug.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.vmware.debug.bin
