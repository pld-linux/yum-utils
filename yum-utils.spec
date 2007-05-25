Summary:	A collection of utilities related to yum
Summary(pl.UTF-8):	Zestaw narzędzi związanych z yumem
Name:		yum-utils
Version:	1.1.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://linux.duke.edu/projects/yum/download/yum-utils/%{name}-%{version}.tar.gz
# Source0-md5:	6d5388c557c6ca1df32f14e8509acec0
Patch0:		%{name}-yum-config.patch
URL:		http://linux.duke.edu/projects/yum/
BuildRequires:	gettext-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.228
Requires:	python >= 1:2.5
Requires:	yum
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yum-utils is a collection of utilities, plugins and examples related
to the yum package manager.

%description -l pl.UTF-8
yum-utils to zestaw narzędzi, wtyczek i przykładów związanych z
zarządcą pakietów yum.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYLIBDIR=%{py_sitescriptdir}/..

# Plugins to install
plugins="changelog fastestmirror fedorakmod protectbase versionlock tsflags kernel-module downloadonly allowdowngrade skip-broken priorities refresh-updatesd merge-conf security"
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/yum/pluginconf.d,%{_libdir}/yum-plugins}

cd plugins
for plug in $plugins; do
    install $plug/*.conf $RPM_BUILD_ROOT/%{_sysconfdir}/yum/pluginconf.d
    install $plug/*.py $RPM_BUILD_ROOT/usr/lib/yum-plugins
done

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/debuginfo-install
%attr(755,root,root) %{_bindir}/package-cleanup
%attr(755,root,root) %{_bindir}/repoclosure
%attr(755,root,root) %{_bindir}/repo-graph
%attr(755,root,root) %{_bindir}/repomanage
%attr(755,root,root) %{_bindir}/repoquery
%attr(755,root,root) %{_bindir}/repo-rss
%attr(755,root,root) %{_bindir}/reposync
%attr(755,root,root) %{_bindir}/repotrack
%attr(755,root,root) %{_bindir}/yum-builddep
%attr(755,root,root) %{_bindir}/yumdownloader
%{_sysconfdir}/yum/pluginconf.d/*
%{_libdir}/yum-plugins/*
%{_mandir}/man*/*
