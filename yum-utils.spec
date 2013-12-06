Summary:	A collection of utilities related to yum
Summary(pl.UTF-8):	Zestaw narzędzi związanych z yumem
Name:		yum-utils
Version:	1.1.31
Release:	6
License:	GPL
Group:		Applications/System
Source0:	http://yum.baseurl.org/download/yum-utils/%{name}-%{version}.tar.gz
# Source0-md5:	b2859b89321b98f2581243536e1b4993
Source1:	yum-plugin-pld-kernel.py
Source2:	yum-plugin-pld-kernel.conf
URL:		http://yum.baseurl.org/download/yum-utils/
BuildRequires:	gettext-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.228
Requires:	python >= 1:2.5
Requires:	yum >= 3.2.29
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_prefix}/lib/%{name}

%description
Yum-utils is a collection of utilities, plugins and examples related
to the yum package manager.

%description -l pl.UTF-8
yum-utils to zestaw narzędzi, wtyczek i przykładów związanych z
zarządcą pakietów yum.

%package -n yum-updateonboot
Summary:	Run yum update on system boot
Summary(pl.UTF-8):	Uruchamianie yum update przy starcie systemu
Group:		Base
Requires(post):	/sbin/chkconfig
Requires(pre):	/sbin/chkconfig
Requires:	python
Requires:	yum >= 2.4

%description -n yum-updateonboot
Runs yum update on system boot. This allows machines that have been
turned off for an extended amount of time to become secure
immediately, instead of waiting until the next early morning cron job.

%description -n yum-updateonboot -l pl.UTF-8
Uruchamianie yum update przy starcie systemu. Pozwala to maszynom
wyłączonym na dłuższy czas stać się bezpiecznymi natychmiast, bez
czekania na kolejne poranne zadanie crona.

%package -n yum-plugin-changelog
Summary:	Yum plugin for viewing package changelogs before/after updating
Summary(pl.UTF-8):	Wtyczka yuma do oglądania list zmian pakietów przed/po uaktualnieniu
Group:		Base
# changelog requires new update_md.UpdateMetadata() API in 3.2.23
Requires:	python-dateutil
Requires:	yum >= 3.2.23
Obsoletes:	yum-changelog

%description -n yum-plugin-changelog
This plugin adds a command line option to allow viewing package
changelog deltas before or after updating packages.

%description -n yum-plugin-changelog -l pl.UTF-8
Ta wtyczka dodaje opcję linii poleceń pozwalającą oglądać przyrostowo
listę zmian pakietu (changelog) przed lub po uaktualnieniu.

%package -n yum-plugin-fastestmirror
Summary:	Yum plugin which chooses fastest repository from a mirrorlist
Summary(pl.UTF-8):	Wtyczka yuma wybierająca najszybsze repozytorium z listy serwerów lustrzanych
Group:		Base
Requires:	yum >= 3.0
Obsoletes:	yum-fastestmirror

%description -n yum-plugin-fastestmirror
This plugin sorts each repository's mirrorlist by connection speed
prior to downloading packages.

%description -n yum-plugin-fastestmirror -l pl.UTF-8
Ta wtyczka sortuje listy serwerów lustrzanych każdego repozytorium po
szybkości połączenia przed rozpoczęciem ściągania pakietów.

%package -n yum-plugin-protectbase
Summary:	Yum plugin to protect packages from certain repositories
Summary(pl.UTF-8):	Wtyczka yuma zabezpieczająca pakiety z pewnych repozytoriów
Group:		Base
Requires:	yum >= 3.0
Obsoletes:	yum-protectbase

%description -n yum-plugin-protectbase
This plugin allows certain repositories to be protected. Packages in
the protected repositories can't be overridden by packages in
non-protected repositories even if the non-protected repo has a later
version.

%description -n yum-plugin-protectbase -l pl.UTF-8
Ta wtyczka pozwala na zabezpieczenie pewnych repozytoriów. Pakiety z
zabezpieczonych repozytoriów nie mogą być przykryte przez pakiety z
repozytoriów niezabezpieczonych, nawet jeśli w niezabezpieczonym jest
nowsza wersja.

%package -n yum-plugin-versionlock
Summary:	Yum plugin to lock specified packages from being updated
Summary(pl.UTF-8):	Wtyczka yuma blokująca uaktualnianie określonych pakietów
Group:		Base
Requires:	yum >= 3.2.24
Obsoletes:	yum-versionlock

%description -n yum-plugin-versionlock
This plugin allows certain packages specified in a file to be
protected from being updated by newer versions.

%description -n yum-plugin-versionlock -l pl.UTF-8
Ta wtyczka pozwala chronić pewne pakiety określone w pliku przed
uaktualnieniem do nowszych wersji.

%package -n yum-plugin-tsflags
Summary:	Yum plugin to add tsflags by a commandline option
Summary(pl.UTF-8):	Wtyczka yuma dodająca flagi transakcji opcją linii poleceń
Group:		Base
Requires:	yum >= 3.0
Obsoletes:	yum-tsflags

%description -n yum-plugin-tsflags
This plugin allows you to specify optional transaction flags on the
yum command line.

%description -n yum-plugin-tsflags -l pl.UTF-8
Ta wtyczka pozwala określić dodatkowe flagi transakcji z linii
poleceń.

# TODO: figure if to remove in pld
%package -n yum-kernel-module
Summary:	Yum plugin to handle kernel-module-foo type of kernel module
Summary(pl.UTF-8):	Wtyczka yuma obsługująca moduły jądra typu kernel-module-foo
Group:		Base
Requires:	yum >= 3.0

%description -n yum-kernel-module
This plugin handle installation of kernel-module-foo type of kernel
modules when new version of kernels are installed.

%description -n yum-kernel-module -l pl.UTF-8
Ta wtyczka obsługuje instalację modułów jądra typu kernel-module-foo
kiedy zainstalowane są nowe wersje jądra.

%package -n yum-plugin-downloadonly
Summary:	Yum plugin to add downloadonly command option
Summary(pl.UTF-8):	Wtyczka yuma dodająca opcję linii poleceń downloadonly
Group:		Base
Requires:	yum >= 3.0
Obsoletes:	yum-downloadonly

%description -n yum-plugin-downloadonly
This plugin adds a --downloadonly flag to yum so that yum will only
download the packages and not install/update them.

%description -n yum-plugin-downloadonly -l pl.UTF-8
Ta wtyczka dodaje flagę --downloadonly do yuma, powodującą, że yum
tylko ściąga pakiety bez ich instalacji/uaktualniania.

%package -n yum-allowdowngrade
Summary:	Yum plugin to enable manual downgrading of packages
Summary(pl.UTF-8):	Wtyczka yuma umożliwiająca ręczne instalowanie starszych pakietów
Group:		Base
Requires:	yum >= 3.0

%description -n yum-allowdowngrade
This plugin adds a --allow-downgrade flag to yum to make it possible
to manually downgrade packages to specific versions.

%description -n yum-allowdowngrade -l pl.UTF-8
Ta wtyczka dodaje do yuma flagę --allow-downgrade, umożliwiającą
ręczne zastępowanie pakietów określonymi starszymi wersjami
(downgrade).

%package -n yum-plugin-pld-kernel
Summary:	Yum plugin to handle PLD kernel installs
Summary(pl.UTF-8):	Wtyczka yuma obsługująca instalację jąder PLD
Group:		Base
Requires:	yum >= 3.0
Obsoletes:	yum-pld-kernel

%description -n yum-plugin-pld-kernel
This plugin handle installation of PLD kernels.

%description -n yum-plugin-pld-kernel -l pl.UTF-8
Ta wtyczka obsługuje instalację jąder PLD.

%package -n yum-plugin-priorities
Summary:	Plugin to give priorities to packages from different repos
Summary(pl.UTF-8):	Wtyczka nadająca priorytety pakietom z różnych repozytoriów
Group:		Base
Requires:	yum >= 3.0
Obsoletes:	yum-priorities

%description -n yum-plugin-priorities
This plugin allows repositories to have different priorities. Packages
in a repository with a lower priority can't be overridden by packages
from a repository with a higher priority even if repo has a later
version.

%description -n yum-plugin-priorities -l pl.UTF-8
Ta wtyczka umożliwia przypisanie repozytoriom różnych priorytetów.
Pakiety z repozytorium o niższym priorytecie nie mogą być przykryte
przez pakiety z repozytorium o wyższym priorytecie nawet jeśli te
drugie mają nowszą wersję.

%package -n yum-plugin-refresh-updatesd
Summary:	Tell yum-updatesd to check for updates when yum exits
Summary(pl.UTF-8):	Sprawdzanie uaktualnień przez yum-updatesd przy zakończeniu yuma
Group:		Base
Requires:	yum >= 3.0
Requires:	yum-updatesd
Obsoletes:	yum-refresh-updatesd

%description -n yum-plugin-refresh-updatesd
yum-plugin-refresh-updatesd tells yum-updatesd to check for updates
when yum exits. This way, if you run 'yum update' and install all
available updates, puplet will almost instantly update itself to
reflect this.

%description -n yum-plugin-refresh-updatesd -l pl.UTF-8
yum-plugin-refresh-updatesd przekazuje yum-updatesd, aby sprawdzał
uaktualnienia kiedy yum kończy pracę. W ten sposób po uruchomieniu
"yum update" i zainstalowaniu wszystkich dostępnych uaktualnień puplet
prawie natychmiast uaktualni swoje informacje.

%package -n yum-plugin-merge-conf
Summary:	Yum plugin to merge configuration changes when installing packages
Summary(pl.UTF-8):	Wtyczka yuma do włączania zmian konfiguracji przy instalacji pakietów
Group:		Base
Requires:	yum >= 3.0
Obsoletes:	yum-merge-conf

%description -n yum-plugin-merge-conf
This yum plugin adds the "--merge-conf" command line option. With this
option, Yum will ask you what to do with config files which have
changed on updating a package.

%description -n yum-plugin-merge-conf -l pl.UTF-8
Ta wtyczka yuma dodaje opcję linii poleceń --merge-conf. Przy jej
użyciu yum pyta co zrobić z plikami konfiguracyjnymi, które zmieniły
się przy uaktualnianiu pakietu.

%package -n yum-plugin-security
Summary:	Yum plugin to enable security filters
Summary(pl.UTF-8):	Wtyczka yuma włączająca filtry bezpieczeństwa
Group:		Base
Requires:	yum >= 3.2.18
Obsoletes:	yum-security

%description -n yum-plugin-security
This plugin adds the options --security, --cve, --bz and --advisory
flags to yum and the list-security and info-security commands. The
options make it possible to limit list/upgrade of packages to specific
security relevant ones. The commands give you the security
information.

%description -n yum-plugin-security -l pl.UTF-8
Ta wtyczka dodaje do yuma flagi --security, --cve, --bz i --advisory
oraz polecenia list-security i info-security. Opcje te umożliwiają
ograniczenie listy/uaktualnień pakietów do związanych z
bezpieczeństwem w określony sposób. Polecenia podają informacje
związane z bezpieczeństwem.

%package -n yum-protect-packages
Summary:	Yum plugin to prevents Yum from removing itself and other protected packages
Summary(pl.UTF-8):	Wtyczka yuma zapobiegająca usunięciu siebie lub innych chronionych pakietów
Group:		Base
Requires:	yum >= 3.0

%description -n yum-protect-packages
This plugin prevents Yum from removing itself and other protected
packages. By default, yum is the only package protected, but by
extension this automatically protects everything on which yum depends
(rpm, python, glibc, and so on).Therefore, the plugin functions well
even without compiling careful lists of all important packages.

%description -n yum-protect-packages -l pl.UTF-8
Ta wtyczka zapobiega usunięciu przez yuma siebie samego lub innych
chronionych pakietów. Domyślnie jedynym chronionym pakietem jest yum,
ale poprzez rozszerzenie automatycznie zabezpiecza to wszystkie
pakiety będące zależnościami yuma (rpm, python, glibc itd.). W ten
sposób wtyczka funkcjonuje dobrze nawet bez troskliwego tworzenia list
wszystkich ważnych pakietów.

%package -n yum-basearchonly
Summary:	Yum plugin to let Yum install only basearch packages
Summary(pl.UTF-8):	Wtyczka yuma pozwalająca instalować tylko pakiety basearch
Group:		Base
Requires:	yum >= 3.0

%description -n yum-basearchonly
This plugin makes Yum only install basearch packages on multiarch
systems. If you type 'yum install foo' on a x68_64 system, only
'foo-x.y.x86_64.rpm' is installed. If you want to install the
foo-x.y.i386.rpm, you have to type 'yum install foo.i386'. The plugin
only works with 'yum install'.

%description -n yum-basearchonly -l pl.UTF-8
Ta wtyczka powoduje, że yum instaluje tylko pakiety basearch na
systemach multiarch. Po wpisaniu "yum install foo" na systemie x86_64
zostanie zainstalowany tylko "foo-x.y.x86_64.rpm. Aby zainstalować
foo-x.y.i386.rpm, trzeba wpisać "yum install foo.i386". Wtyczka działa
tylko z "yum install".

%package -n yum-plugin-upgrade-helper
Summary:	Yum plugin to help upgrades to the next distribution version
Summary(pl.UTF-8):	Wtyczka yuma pomagająca przy uaktualnianiu do kolejnej wersji dystrybucji
Group:		Base
Requires:	yum >= 3.0
Obsoletes:	yum-upgrade-helper

%description -n yum-plugin-upgrade-helper
This plugin allows yum to erase specific packages on install/update
based on an additional metadata file in repositories. It is used to
simplify distribution upgrade hangups.

%description -n yum-plugin-upgrade-helper -l pl.UTF-8
Ta wtyczka pozwala yumowi usunąć określone pakiety przy instalacji lub
uaktualnianiu w oparciu o dodatkowe pliki metadanych w repozytoriach.
Służy do uproszczenia uaktualnień wersji dystrybucji.

%package -n yum-plugin-aliases
Summary:	Yum plugin to enable aliases filters
Summary(pl.UTF-8):	Wtyczka yuma włączająca filtry aliasów
Group:		Base
# Requires args_hook
Requires:	yum >= 3.2.23
Obsoletes:	yum-aliases

%description -n yum-plugin-aliases
This plugin adds the command alias, and parses the aliases config.
file to enable aliases.

%description -n yum-plugin-aliases -l pl.UTF-8
Ta wtyczka dodaje polecenie alias i analizuje konfigurację aliasów w
celu włączenia aliasów.

%package -n yum-plugin-list-data
Summary:	Yum plugin to list aggregate package data
Summary(pl.UTF-8):	Wtyczka yuma wypisująca zagregowane dane pakietów
Group:		Base
Requires:	yum >= 3.0.5
Obsoletes:	yum-list-data

%description -n yum-plugin-list-data
This plugin adds the commands list- vendors, groups, packagers,
licenses, arches, committers, buildhosts, baseurls, package-sizes,
archive-sizes and installed-sizes.

%description -n yum-plugin-list-data -l pl.UTF-8
Ta wtyczka dodaje polecenia list- vendors, groups, packagers,
licenses, arches, committers, buildhosts, baseurls, package-sizes,
archive-sizes i installed-sizes.

%package -n yum-plugin-filter-data
Summary:	Yum plugin to list filter based on package data
Summary(pl.UTF-8):	Wtyczka yuma dodająca filtry oparte na danych pakietu
Group:		Base
Requires:	yum >= 3.2.17
Obsoletes:	yum-filter-data

%description -n yum-plugin-filter-data
This plugin adds the options --filter- vendors, groups, packagers,
licenses, arches, committers, buildhosts, baseurls, package-sizes,
archive-sizes and installed-sizes. Note that each package must match
at least one pattern/range in each category, if any were specified.

%description -n yum-plugin-filter-data -l pl.UTF-8
Ta wtyczka dodaje opcje --filter- vendors, groups, packagers,
licenses, arches, committers, buildhosts, baseurls, package-sizes,
archive-sizes i installed-sizes. Każdy pakiet musi pasować do
przynajmniej jednego wzorca/zakresu w każdej wybranej kategorii.

%package -n yum-plugin-tmprepo
Summary:	Yum plugin to add temporary repositories
Summary(pl.UTF-8):	Wtyczka yuma dodająca repozytoria tymczasowe
Group:		Base
Requires:	createrepo
Requires:	yum >= 3.2.11
Obsoletes:	yum-tmprepo

%description -n yum-plugin-tmprepo
This plugin adds the option --tmprepo which takes a URL to a .repo
file downloads it and enables it for a single run. This plugin tries
to ensure that temporary repositories are safe to use, by default, by
not allowing gpg checking to be disabled.

%description -n yum-plugin-tmprepo -l pl.UTF-8
Ta wtyczka dodaje opcję --tmprepo przyjmującą URL do pliku .repo i
włączająca go dla jednego uruchomienia. Wtyczka próbuje zapewnić
bezpieczne użycie repozytoriów tymczasowych domyślnie nie pozwalając
na wyłączenie sprawdzania gpg.

%package -n yum-plugin-verify
Summary:	Yum plugin to add verify command, and options
Summary(pl.UTF-8):	Wtyczka yuma dodająca polecenie i opcje weryfikacji
Group:		Base
Requires:	yum >= 3.2.12
Obsoletes:	yum-verify

%description -n yum-plugin-verify
This plugin adds the commands verify, verify-all and verify-rpm. There
are also a couple of options. This command works like rpm -V, to
verify your installation.

%description -n yum-plugin-verify -l pl.UTF-8
Ta wtyczka dodaje polecenia verify, verify-all i verify-rpm, a także
kilka opcji. Działa podobnie jak rpm -V, weryfikując instalację.

%package -n yum-plugin-keys
Summary:	Yum plugin to deal with signing keys
Group:		Base
Requires:	yum >= 3.2.19

%description -n yum-plugin-keys
This plugin adds the commands keys, keys-info, keys-data and
keys-remove. They allow you to query and remove signing keys.

%package -n yum-plugin-remove-with-leaves
Summary:	Yum plugin to remove dependencies which are no longer used because of a removal
Group:		Base
Requires:	yum >= 3.2.19

%description -n yum-plugin-remove-with-leaves
This plugin removes any unused dependencies that were brought in by an
install but would not normally be removed. It helps to keep a system
clean of unused libraries and packages.

%package -n yum-plugin-post-transaction-actions
Summary:	Yum plugin to run arbitrary commands when certain pkgs are acted on
Group:		Base
Requires:	yum >= 3.2.19

%description -n yum-plugin-post-transaction-actions
This plugin allows the user to run arbitrary actions immediately
following a transaction when specified packages are changed.

%package -n yum-NetworkManager-dispatcher
Summary:	NetworkManager script which tells yum to check it's cache on network change
Group:		Base
Requires:	yum >= 3.2.17

%description -n yum-NetworkManager-dispatcher
This NetworkManager "dispatch script" forces yum to check its cache
if/when a new network connection happens in NetworkManager. Note that
currently there is no checking of previous data, so if your WiFi keeps
going up and down (or you suspend/resume a lot) yum will recheck its
cached data a lot.

%package -n yum-plugin-rpm-warm-cache
Summary:	Yum plugin to access the rpmdb files early to warm up access to the db
Group:		Base
Requires:	yum >= 3.2.19

%description -n yum-plugin-rpm-warm-cache
This plugin reads the rpmdb files into the system cache before
accessing the rpmdb directly. In some cases this should speed up
access to rpmdb information

# Works by searching for *-debuginfo ... so it shouldn't trigger on
itself.
%package -n yum-plugin-auto-update-debug-info
Summary:	Yum plugin to enable automatic updates to installed debuginfo packages
Group:		Base
Requires:	yum >= 3.2.19

%description -n yum-plugin-auto-update-debug-info
This plugin looks to see if any debuginfo packages are installed, and
if there are it enables all debuginfo repositories that are "children"
of enabled repositories.

%package -n yum-plugin-show-leaves
Summary:	Yum plugin which shows newly installed leaf packages
Group:		Base
Requires:	yum >= 3.2.23

%description -n yum-plugin-show-leaves
Yum plugin which shows newly installed leaf packages and packages that
became leaves after a transaction

%package -n yum-plugin-local
Summary:	Yum plugin to automatically manage a local repo. of downloaded packages
Group:		Base
# Who the hell knows what version:)
Requires:	createrepo
Requires:	yum >= 3.2.22

%description -n yum-plugin-local
When this plugin is installed it will automatically copy all
downloaded packages to a repository on the local filesystem, and
(re)build that repository. This means that anything you've downloaded
will always exist, even if the original repo. removes it (and can
thus. be reinstalled/downgraded/etc.).

%package -n yum-plugin-fs-snapshot
Summary:	Yum plugin to automatically snapshot your filesystems during updates
Group:		Base
Requires:	yum >= 3.2.22

%description -n yum-plugin-fs-snapshot
When this plugin is installed it will automatically snapshot any
filesystem that is touched by the packages in a yum update or yum
remove.

%package -n yum-plugin-ps
Summary:	Yum plugin to look at processes, with respect to packages
Group:		Base
Requires:	yum >= 3.2.27

%description -n yum-plugin-ps
When this plugin is installed it adds the yum command "ps", which
allows you to see which running processes are accociated with which
packages (and if they need rebooting, or have updates, etc.)

%package -n yum-plugin-puppetverify
Summary:	Yum plugin to add puppet checksums to verify data
Group:		Base
Requires:	puppet
Requires:	python-PyYAML >= 3.09
Requires:	yum >= 3.2.12

%description -n yum-plugin-puppetverify
Supplies checksums for files in packages from puppet's state file.

%package -n bash-completion-%{name}
Summary:	bash-completion for Yum Utils
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla Yum Utils
Group:		Applications/Shells
Requires:	%{name}
Requires:	bash-completion

%description -n bash-completion-%{name}
bash-completion for Yum Utils.

%description -n bash-completion-%{name} -l pl.UTF-8
bashowe uzupełnianie nazw dla Yum Utils.

%prep
%setup -q

mv plugins/README README.plugins

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PYLIBDIR=%{py_scriptdir} \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C updateonboot install \
	DESTDIR=$RPM_BUILD_ROOT

# Plugins to install
plugins="
changelog
fastestmirror
protectbase
versionlock
tsflags
kernel-module
downloadonly
allowdowngrade
priorities
refresh-updatesd
merge-conf
security
basearchonly
upgrade-helper
aliases
list-data
filter-data
tmprepo
verify

keys
remove-with-leaves
post-transaction-actions
rpm-warm-cache
auto-update-debuginfo
show-leaves
local
fs-snapshot
ps
puppetverify
"

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/yum/{pluginconf.d,post-actions},%{_libexecdir}}

cd plugins
for plug in $plugins; do
	cp -p $plug/*.conf $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d
	cp -p $plug/*.py $RPM_BUILD_ROOT%{_libexecdir}
done

cp -p aliases/aliases $RPM_BUILD_ROOT%{_sysconfdir}/yum/aliases.conf
cp -p versionlock/versionlock.list $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d

# need for for the ghost in files section of yum-plugin-local
install -d $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
touch $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/_local.repo

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_libexecdir}/pld-kernel.py
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d/pld-kernel.conf

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post -n yum-updateonboot
/sbin/chkconfig --add yum-updateonboot

%preun -n yum-updateonboot
if [ "$1" = 0 ]; then
	%service yum-updateonboot stop
	/sbin/chkconfig --del yum-updateonboot
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.plugins TODO
%doc yum-util-cli-template
%attr(755,root,root) %{_bindir}/debuginfo-install
%attr(755,root,root) %{_bindir}/find-repos-of-install
%attr(755,root,root) %{_bindir}/needs-restarting
%attr(755,root,root) %{_bindir}/package-cleanup
%attr(755,root,root) %{_bindir}/repo-graph
%attr(755,root,root) %{_bindir}/repo-rss
%attr(755,root,root) %{_bindir}/repoclosure
%attr(755,root,root) %{_bindir}/repodiff
%attr(755,root,root) %{_bindir}/repomanage
%attr(755,root,root) %{_bindir}/repoquery
%attr(755,root,root) %{_bindir}/reposync
%attr(755,root,root) %{_bindir}/repotrack
%attr(755,root,root) %{_bindir}/show-changed-rco
%attr(755,root,root) %{_bindir}/show-installed
%attr(755,root,root) %{_bindir}/verifytree
%attr(755,root,root) %{_bindir}/yum-builddep
%attr(755,root,root) %{_bindir}/yum-config-manager
%attr(755,root,root) %{_bindir}/yum-debug-dump
%attr(755,root,root) %{_bindir}/yum-debug-restore
%attr(755,root,root) %{_bindir}/yum-groups-manager
%attr(755,root,root) %{_bindir}/yumdownloader
%attr(755,root,root) %{_sbindir}/yum-complete-transaction
%attr(755,root,root) %{_sbindir}/yumdb
%dir %{_libexecdir}
%dir %{py_sitescriptdir}/yumutils
%{py_sitescriptdir}/yumutils/*.py[co]
%{_mandir}/man1/debuginfo-install.1*
%{_mandir}/man1/package-cleanup.1.*
%{_mandir}/man1/repo-rss.1.*
%{_mandir}/man1/repodiff.1*
%{_mandir}/man1/repoquery.1.*
%{_mandir}/man1/reposync.1.*
%{_mandir}/man1/show-changed-rco.1*
%{_mandir}/man1/show-installed.1*
%{_mandir}/man1/yum-aliases.1*
%{_mandir}/man1/yum-builddep.1.*
%{_mandir}/man1/yum-debug-dump.1*
%{_mandir}/man1/yum-groups-manager.1*
%{_mandir}/man1/yum-utils.1.*
%{_mandir}/man1/yum-versionlock.1*
%{_mandir}/man1/yumdownloader.1.*
%{_mandir}/man5/yum-versionlock.conf.5*
%{_mandir}/man8/yum-complete-transaction.8.*
%{_mandir}/man8/yumdb.8*

%files -n yum-updateonboot
%defattr(644,root,root,755)
%doc updateonboot/README
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/yum-updateonboot
%attr(754,root,root) /etc/rc.d/init.d/yum-updateonboot

%files -n yum-plugin-changelog
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/changelog.conf
%{_libexecdir}/changelog.*
%{_mandir}/man1/yum-changelog.1.*
%{_mandir}/man5/yum-changelog.conf.5.*

%files -n yum-plugin-fastestmirror
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/fastestmirror.conf
%{_libexecdir}/fastestmirror.*

%files -n yum-plugin-protectbase
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/protectbase.conf
%{_libexecdir}/protectbase.*

%files -n yum-plugin-versionlock
%defattr(644,root,root,755)
%doc plugins/versionlock/README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/versionlock.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/versionlock.list
%{_libexecdir}/versionlock.*

%files -n yum-plugin-tsflags
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/tsflags.conf
%{_libexecdir}/tsflags.*

# TODO: remove in pld? removed in fedora
%files -n yum-kernel-module
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/kernel-module.conf
%{_libexecdir}/kernel-module.*

%files -n yum-plugin-downloadonly
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/downloadonly.conf
%{_libexecdir}/downloadonly.*

# TODO: remove like fedora?
%files -n yum-allowdowngrade
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/allowdowngrade.conf
%{_libexecdir}/allowdowngrade.*

%files -n yum-plugin-pld-kernel
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/pld-kernel.conf
%{_libexecdir}/pld-kernel.*

%files -n yum-plugin-priorities
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/priorities.conf
%{_libexecdir}/priorities.*

%files -n yum-plugin-refresh-updatesd
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/refresh-updatesd.conf
%{_libexecdir}/refresh-updatesd.*

%files -n yum-plugin-merge-conf
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/merge-conf.conf
%{_libexecdir}/merge-conf.*

%files -n yum-plugin-security
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/security.conf
%{_libexecdir}/security.*
%{_mandir}/man8/yum-security.8.*

%if 0
# TODO: renamed to protectbase?
%files -n yum-protect-packages
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/protect-packages.conf
%{_libexecdir}/protect-packages.*
%endif

# TODO: rename to basearchonly like fedora?
%files -n yum-basearchonly
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/basearchonly.conf
%{_libexecdir}/basearchonly.*

%files -n yum-plugin-upgrade-helper
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/upgrade-helper.conf
%{_libexecdir}/upgrade-helper.*

%files -n yum-plugin-aliases
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/aliases.conf
%config(noreplace) %{_sysconfdir}/yum/aliases.conf
%{_libexecdir}/aliases.*

%files -n yum-plugin-list-data
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/list-data.conf
%{_libexecdir}/list-data.*
%{_mandir}/man1/yum-list-data.1.*

%files -n yum-plugin-filter-data
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/filter-data.conf
%{_libexecdir}/filter-data.*
%{_mandir}/man1/yum-filter-data.1.*

%files -n yum-plugin-tmprepo
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/tmprepo.conf
%{_libexecdir}/tmprepo.*

%files -n yum-plugin-verify
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/verify.conf
%{_libexecdir}/verify.*
%{_mandir}/man1/yum-verify.1.*

%files -n yum-plugin-keys
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/keys.conf
%{_libexecdir}/keys.*

%files -n yum-NetworkManager-dispatcher
%defattr(644,root,root,755)
%{_sysconfdir}/NetworkManager/dispatcher.d/yum-NetworkManager-dispatcher

%files -n yum-plugin-remove-with-leaves
%defattr(644,root,root,755)
%{_libexecdir}/remove-with-leaves.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/remove-with-leaves.conf

%files -n yum-plugin-post-transaction-actions
%defattr(644,root,root,755)
%{_libexecdir}/post-transaction-actions.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/post-transaction-actions.conf
%doc plugins/post-transaction-actions/sample.action
# Default *.action file dropping dir.
%dir %{_sysconfdir}/yum/post-actions

%files -n yum-plugin-rpm-warm-cache
%defattr(644,root,root,755)
%{_libexecdir}/rpm-warm-cache.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/rpm-warm-cache.conf

%files -n yum-plugin-auto-update-debug-info
%defattr(644,root,root,755)
%{_libexecdir}/auto-update-debuginfo.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/auto-update-debuginfo.conf

%files -n yum-plugin-show-leaves
%defattr(644,root,root,755)
%{_libexecdir}/show-leaves.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/show-leaves.conf

%files -n yum-plugin-local
%defattr(644,root,root,755)
%ghost %{_sysconfdir}/yum.repos.d/_local.repo
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/local.conf
%{_libexecdir}/local.*

%files -n yum-plugin-fs-snapshot
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/fs-snapshot.conf
%{_libexecdir}/fs-snapshot.*
%{_mandir}/man1/yum-fs-snapshot.1.*
%{_mandir}/man5/yum-fs-snapshot.conf.5.*

%files -n yum-plugin-ps
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/ps.conf
%{_libexecdir}/ps.*

%files -n yum-plugin-puppetverify
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/puppetverify.conf
%{_libexecdir}/puppetverify.*

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
/etc/bash_completion.d/*
