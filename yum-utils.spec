Summary:	A collection of utilities related to yum
Summary(pl.UTF-8):	Zestaw narzędzi związanych z yumem
Name:		yum-utils
Version:	1.1.13
Release:	0.2
License:	GPL
Group:		Applications/System
Source0:	http://linux.duke.edu/yum/download/yum-utils/%{name}-%{version}.tar.gz
# Source0-md5:	29eedb17fd40b158c129c84dc865d889
Source1:	yum-plugin-pld-kernel.py
Source2:	yum-plugin-pld-kernel.conf
URL:		http://linux.duke.edu/yum/download/yum-utils/
BuildRequires:	gettext-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.228
Requires:	python >= 1:2.5
Requires:	yum >= 3.1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yum-utils is a collection of utilities, plugins and examples related
to the yum package manager.

%description -l pl.UTF-8
yum-utils to zestaw narzędzi, wtyczek i przykładów związanych z
zarządcą pakietów yum.

%package -n yum-updateonboot
Summary:	Run yum update on system boot
Group:		Base
Requires(post):	/sbin/chkconfig
Requires(pre):	/sbin/chkconfig
Requires:	python
Requires:	yum >= 2.4

%description -n yum-updateonboot
Runs yum update on system boot. This allows machines that have been
turned off for an extended amount of time to become secure
immediately, instead of waiting until the next early morning cron job.

%package -n yum-changelog
Summary:	Yum plugin for viewing package changelogs before/after updating
Group:		Base
Requires:	yum >= 3.0

%description -n yum-changelog
This plugin adds a command line option to allow viewing package
changelog deltas before or after updating packages.

%package -n yum-fastestmirror
Summary:	Yum plugin which chooses fastest repository from a mirrorlist
Group:		Base
Requires:	yum >= 3.0

%description -n yum-fastestmirror
This plugin sorts each repository's mirrorlist by connection speed
prior to downloading packages.

%package -n yum-protectbase
Summary:	Yum plugin to protect packages from certain repositories
Group:		Base
Requires:	yum >= 3.0

%description -n yum-protectbase
This plugin allows certain repositories to be protected. Packages in
the protected repositories can't be overridden by packages in
non-protected repositories even if the non-protected repo has a later
version.

%package -n yum-versionlock
Summary:	Yum plugin to lock specified packages from being updated
Group:		Base
Requires:	yum >= 3.0

%description -n yum-versionlock
This plugin allows certain packages specified in a file to be
protected from being updated by newer versions.

%package -n yum-tsflags
Summary:	Yum plugin to add tsflags by a commandline option
Group:		Base
Requires:	yum >= 3.0

%description -n yum-tsflags
This plugin allows you to specify optional transaction flags on the
yum command line

%package -n yum-kernel-module
Summary:	Yum plugin to handle kernel-module-foo type of kernel module
Group:		Base
Requires:	yum >= 3.0

%description -n yum-kernel-module
This plugin handle installation of kernel-module-foo type of kernel
modules when new version of kernels are installed.


%package -n yum-downloadonly
Summary:	Yum plugin to add downloadonly command option
Group:		Base
Requires:	yum >= 3.0

%description -n yum-downloadonly
This plugin adds a --downloadonly flag to yum so that yum will only
download the packages and not install/update them.

%package -n yum-allowdowngrade
Summary:	Yum plugin to enable manual downgrading of packages
Group:		Base
Requires:	yum >= 3.0

%description -n yum-allowdowngrade
This plugin adds a --allow-downgrade flag to yum to make it possible
to manually downgrade packages to specific versions.

%package -n yum-skip-broken
Summary:	Yum plugin to handle skiping packages with dependency problems
Group:		Base
Requires:	yum >= 3.0

%description -n yum-skip-broken
This plugin adds a --skip-broken to yum to make it possible to check
packages for dependency problems and skip the one with problems.

%package -n yum-pld-kernel
Summary:	Yum plugin to handle pld kernel installs
Group:		Base
Requires:	yum >= 3.0

%description -n yum-pld-kernel
This plugin handle installation of pld kernels

%package -n yum-priorities
Summary:	plugin to give priorities to packages from different repos
Group:		Base
Requires:	yum >= 3.0

%description -n yum-priorities
This plugin allows repositories to have different priorities. Packages
in a repository with a lower priority can't be overridden by packages
from a repository with a higher priority even if repo has a later
version.

%package -n yum-refresh-updatesd
Summary:	Tell yum-updatesd to check for updates when yum exits
Group:		Base
Requires:	yum >= 3.0
Requires:	yum-updatesd

%description -n yum-refresh-updatesd
yum-refresh-updatesd tells yum-updatesd to check for updates when yum
exits. This way, if you run 'yum update' and install all available
updates, puplet will almost instantly update itself to reflect this.

%package -n yum-merge-conf
Summary:	Yum plugin to merge configuration changes when installing packages
Group:		Base
Requires:	yum >= 3.0

%description -n yum-merge-conf
This yum plugin adds the "--merge-conf" command line option. With this
option, Yum will ask you what to do with config files which have
changed on updating a package.

%package -n yum-security
Summary:	Yum plugin to enable security filters
Group:		Base
Requires:	yum >= 3.0.5

%description -n yum-security
This plugin adds the options --security, --cve, --bz and --advisory
flags to yum and the list-security and info-security commands. The
options make it possible to limit list/upgrade of packages to specific
security relevant ones. The commands give you the security
information.

%package -n yum-protect-packages
Summary:	Yum plugin to prevents Yum from removing itself and other protected packages
Group:		Base
Requires:	yum >= 3.0

%description -n yum-protect-packages
this plugin prevents Yum from removing itself and other protected
packages. By default, yum is the only package protected, but by
extension this automatically protects everything on which yum depends
(rpm, python, glibc, and so on).Therefore, the plugin functions well
even without compiling careful lists of all important packages.

%package -n yum-basearchonly
Summary:	Yum plugin to let Yum install only basearch packages
Group:		Base
Requires:	yum >= 3.0

%description -n yum-basearchonly
this plugin makes Yum only install basearch packages on multiarch
systems. If you type 'yum install foo' on a x68_64 system, only
'foo-x.y.x86_46.rpm' is installed. If you want to install the
foo-x.y.i386.rpm, you have to type 'yum install foo.i386'. The plugin
only works with 'yum install'.

%package -n yum-upgrade-helper
Summary:	Yum plugin to help upgrades to the next distribution version
Group:		Base
Requires:	yum >= 3.0

%description -n yum-upgrade-helper
this plugin allows yum to erase specific packages on install/update
based on an additional metadata file in repositories. It is used to
simplify distribution upgrade hangups.

%package -n yum-aliases
Summary:	Yum plugin to enable aliases filters
Group:		Base
Requires:	yum >= 3.0.5

%description -n yum-aliases
This plugin adds the command alias, and parses the aliases config.
file to enable aliases.

%package -n yum-list-data
Summary:	Yum plugin to list aggregate package data
Group:		Base
Requires:	yum >= 3.0.5

%description -n yum-list-data
This plugin adds the commands list- vendors, groups, packagers,
licenses, arches, committers, buildhosts, baseurls, package-sizes,
archive-sizes and installed-sizes.

%package -n yum-filter-data
Summary:	Yum plugin to list filter based on package data
Group:		Base
Requires:	yum >= 3.0.5

%description -n yum-filter-data
This plugin adds the options --filter- vendors, groups, packagers,
licenses, arches, committers, buildhosts, baseurls, package-sizes,
archive-sizes and installed-sizes. Note that each package must match
at least one pattern/range in each category, if any were specified.

%package -n yum-tmprepo
Summary:	Yum plugin to add temporary repositories
Group:		Base
Requires:	yum >= 3.2.11

%description -n yum-tmprepo
This plugin adds the option --tmprepo which takes a url to a .repo
file downloads it and enables it for a single run. This plugin tries
to ensure that temporary repositories are safe to use, by default, by
not allowing gpg checking to be disabled.

%package -n yum-verify
Summary:	Yum plugin to add verify command, and options
Group:		Base
Requires:	yum >= 3.2.12

%description -n yum-verify
This plugin adds the commands verify, verify-all and verify-rpm. There
are also a couple of options. This command works like rpm -V, to
verify your installation.

%prep
%setup -q

mv plugins/README README.plugins

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install
%{__make} -C updateonboot DESTDIR=$RPM_BUILD_ROOT install

# Plugins to install
plugins="changelog fastestmirror protectbase versionlock tsflags kernel-module \
         downloadonly allowdowngrade skip-broken priorities refresh-updatesd merge-conf \
         security protect-packages basearchonly upgrade-helper aliases list-data filter-data tmprepo verify"

install -d $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d/ $RPM_BUILD_ROOT%{_datadir}/yum-plugins

cd plugins
for plug in $plugins; do
	install -m 644 $plug/*.conf $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d
	install $plug/*.py $RPM_BUILD_ROOT%{_datadir}/yum-plugins
done
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/yum-plugins/pld-kernel.py
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d/pld-kernel.conf

install aliases/aliases $RPM_BUILD_ROOT%{_sysconfdir}/yum/aliases.conf
install versionlock/versionlock.list $RPM_BUILD_ROOT%{_sysconfdir}/yum/pluginconf.d

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post -n yum-updateonboot
/sbin/chkconfig --add yum-updateonboot

%preun -n yum-updateonboot
if [ $1 = 0 ]; then
	%service yum-updateonboot stop
	/sbin/chkconfig --del yum-updateonboot
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.plugins TODO
%doc yum-util-cli-template
%attr(755,root,root) %{_bindir}/debuginfo-install
%attr(755,root,root) %{_bindir}/package-cleanup
%attr(755,root,root) %{_bindir}/repo-graph
%attr(755,root,root) %{_bindir}/repo-rss
%attr(755,root,root) %{_bindir}/repoclosure
%attr(755,root,root) %{_bindir}/repodiff
%attr(755,root,root) %{_bindir}/repomanage
%attr(755,root,root) %{_bindir}/repoquery
%attr(755,root,root) %{_bindir}/reposync
%attr(755,root,root) %{_bindir}/repotrack
%attr(755,root,root) %{_bindir}/yum-builddep
%attr(755,root,root) %{_bindir}/yumdownloader
%attr(755,root,root) %{_sbindir}/yum-complete-transaction
%{_mandir}/man1/package-cleanup.1.*
%{_mandir}/man1/repo-rss.1.*
%{_mandir}/man1/repoquery.1.*
%{_mandir}/man1/reposync.1.*
%{_mandir}/man1/yum-builddep.1.*
%{_mandir}/man1/yum-utils.1.*
%{_mandir}/man1/yumdownloader.1.*
%{_mandir}/man8/yum-complete-transaction.8.*

%files -n yum-updateonboot
%defattr(644,root,root,755)
%doc updateonboot/README
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/yum-updateonboot
%attr(754,root,root) /etc/rc.d/init.d/yum-updateonboot

%files -n yum-changelog
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/changelog.conf
%{_datadir}/yum-plugins/changelog.*
%{_mandir}/man1/yum-changelog.1.*
%{_mandir}/man5/yum-changelog.conf.5.*

%files -n yum-fastestmirror
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/fastestmirror.conf
%{_datadir}/yum-plugins/fastestmirror.*

%files -n yum-protectbase
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/protectbase.conf
%{_datadir}/yum-plugins/protectbase.*

%files -n yum-versionlock
%defattr(644,root,root,755)
%doc plugins/versionlock/README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/versionlock.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/versionlock.list
%{_datadir}/yum-plugins/versionlock.*

%files -n yum-tsflags
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/tsflags.conf
%{_datadir}/yum-plugins/tsflags.*

%files -n yum-kernel-module
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/kernel-module.conf
%{_datadir}/yum-plugins/kernel-module.*

%files -n yum-downloadonly
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/downloadonly.conf
%{_datadir}/yum-plugins/downloadonly.*

%files -n yum-allowdowngrade
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/allowdowngrade.conf
%{_datadir}/yum-plugins/allowdowngrade.*

%files -n yum-skip-broken
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/skip-broken.conf
%{_datadir}/yum-plugins/skip-broken.*

%files -n yum-pld-kernel
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/pld-kernel.conf
%{_datadir}/yum-plugins/pld-kernel.*

%files -n yum-priorities
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/priorities.conf
%{_datadir}/yum-plugins/priorities.*

%files -n yum-refresh-updatesd
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/refresh-updatesd.conf
%{_datadir}/yum-plugins/refresh-updatesd.*

%files -n yum-merge-conf
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/merge-conf.conf
%{_datadir}/yum-plugins/merge-conf.*

%files -n yum-security
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/security.conf
%{_datadir}/yum-plugins/security.*
%{_mandir}/man8/yum-security.8.*

%files -n yum-protect-packages
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/protect-packages.conf
%{_datadir}/yum-plugins/protect-packages.*

%files -n yum-basearchonly
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/basearchonly.conf
%{_datadir}/yum-plugins/basearchonly.*

%files -n yum-upgrade-helper
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/upgrade-helper.conf
%{_datadir}/yum-plugins/upgrade-helper.*

%files -n yum-aliases
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/aliases.conf
%config(noreplace) %{_sysconfdir}/yum/aliases.conf
%{_datadir}/yum-plugins/aliases.*

%files -n yum-list-data
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/list-data.conf
%{_datadir}/yum-plugins/list-data.*
%{_mandir}/man1/yum-list-data.1.*

%files -n yum-filter-data
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/filter-data.conf
%{_datadir}/yum-plugins/filter-data.*
%{_mandir}/man1/yum-filter-data.1.*

%files -n yum-tmprepo
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/tmprepo.conf
%{_datadir}/yum-plugins/tmprepo.*

%files -n yum-verify
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yum/pluginconf.d/verify.conf
%{_datadir}/yum-plugins/verify.*
%{_mandir}/man1/yum-verify.1.*
