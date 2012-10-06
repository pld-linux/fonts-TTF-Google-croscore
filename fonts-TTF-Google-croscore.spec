Summary:	The width-compatible fonts for improved on-screen readability
Name:		fonts-TTF-Google-croscore
Version:	1.21.0
Release:	3
License:	OFL
Group:		Fonts
Source0:	http://gsdview.appspot.com/chromeos-localmirror/distfiles/croscorefonts-%{version}.tar.gz
# Source0-md5:	61f59e4110781cbe66b46449eadac231
Source1:	62-google-croscore-arimo-fontconfig.conf
Source2:	62-google-croscore-cousine-fontconfig.conf
Source3:	62-google-croscore-tinos-fontconfig.conf
Source4:	30-0-google-croscore-arimo-fontconfig.conf
Source5:	30-0-google-croscore-cousine-fontconfig.conf
Source6:	30-0-google-croscore-tinos-fontconfig.conf
Source7:	62-google-croscore-symbolneu-fontconfig.conf
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
Requires:	fontconfig >= 1:2.10.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
This package contains a collections of fonts that offers improved
on-screen \ readability characteristics and the pan-European WGL
character set and solves \ the needs of developers looking for
width-compatible fonts to address document \ portability across
platforms.

%prep
%setup -q -n croscorefonts-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/fonts/conf.d,%{_ttffontsdir}}
install -d $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail
install -p *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

# Repeat for every font family
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/62-google-croscore-arimo.conf
install -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/62-google-croscore-cousine.conf
install -p %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/62-google-croscore-tinos.conf
install -p %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/30-0-google-croscore-arimo.conf
install -p %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/30-0-google-croscore-cousine.conf
install -p %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/30-0-google-croscore-tinos.conf
install -p %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/62-google-croscore-symbolneu.conf

for fconf in 62-google-croscore-arimo.conf 30-0-google-croscore-arimo.conf \
	    62-google-croscore-cousine.conf 30-0-google-croscore-cousine.conf \
	    62-google-croscore-tinos.conf 30-0-google-croscore-tinos.conf \
	    62-google-croscore-symbolneu.conf; do
		ln -s %{_datadir}/fontconfig/conf.avail/$fconf \
			$RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/$fconf
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc LICENSE
%{_ttffontsdir}/Arimo*.ttf
%{_ttffontsdir}/Cousine*.ttf
%{_ttffontsdir}/Symbol*.ttf
%{_ttffontsdir}/Tinos*.ttf
%{_datadir}/fontconfig/conf.avail/*.conf
%{_sysconfdir}/fonts/conf.d/*.conf
