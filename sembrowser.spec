Summary:        Faceted side panel using nepomuk
Name:           sembrowser
Version:        0.2
Release:        %mkrel 1
License:        GPLv2+
Group:          Graphical desktop/KDE
Source0:        117692-%name-%version.tar.gz
URL:            http://www.kde-apps.org/content/show.php/Sembrowser?content=117692
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  kdelibs4-devel
BuildRequires:  kdebase4-devel

%description
A prototype of a semantic faceted file manager for KDE 4.
The faceted side panel is based on the Nepomuk technology and libraries.

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/sembrowser
%_kde_datadir/applications/kde4/sembrowser.desktop
%_kde_appsdir/sembrowser
%_kde_iconsdir/hicolor/*/apps/*.png

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT
