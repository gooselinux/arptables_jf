Summary: Userspace control program for the arptables network filter

Name: arptables_jf

Epoch: 0
Version: 0.0.8
Release: 20%{?dist}
Source: %{name}-%{version}.tbz
#Source1: Makefile
#Source2: arptables.h
#Source3: arptables.8
#Source4: libarptc.c
#Source5: libarptc.h
#Source6: arptables.init
Patch1: arptables_jf-0.0.8-2.6-kernel.patch
Patch2: arptables_jf-0.0.8-man.patch
Patch3: arptables_jf-0.0.8-warnings.patch
Patch4: arptables_jf-0.0.8-header.patch
Patch5: arptables_jf-0.0.8-initscript.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Group: System Environment/Base

License: GPLv2+

BuildRequires: perl

Requires: kernel >= 2.4.0

Requires(post): chkconfig
Requires(postun): chkconfig

%description

The arptables_jf utility controls the arpfilter network packet filtering
code in the Linux kernel.  You do not need this program for normal
network firewalling.  If you need to manually control which arp
requests and/or replies this machine accepts and sends, you should
install this package.

%prep
%setup -q
%patch1 -p1 -b .2.6-kernel
%patch2 -p1 -b .man
%patch3 -p1 -b .warnings
%patch4 -p1 -b .header
%patch5 -p1 -b .initscript

%build
make all LIBDIR=/%{_lib} 'COPT_FLAGS=%{optflags} -fno-strict-aliasing' %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=%{buildroot} LIBDIR=/%{_lib}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add arptables_jf

%preun
if [ "$1" = 0 ]; then
        /sbin/chkconfig --del arptables_jf
fi

%files
%defattr(-,root,root,0755)
%attr(0755,root,root) /etc/rc.d/init.d/arptables_jf
/sbin/arptables*
%{_mandir}/*/arptables*


%changelog
* Thu May 27 2010 Jiri Skala <jskala@redhat.com> - 0:0.0.8-20
- Resolves: #596149 - RPMdiff run failed - added -fno-strict-aliasing flag

* Mon Apr 26 2010 Jiri Skala <jskala@redhat.com> - 0:0.0.8-19
- Resolves: #576103 - init script LSB is not compliant (returned condrestart to Usage)

* Tue Mar 24 2010 Jiri Skala <jskala@redhat.com> - 0:0.0.8-18
- Resolves: #576103 - init script LSB is not compliant

* Tue Jan 05 2010 Jiri Skala <jskala@redhat.com> - 0:0.0.8-17
- Related: rhbz#543948
- fixed rpmlint errors and warnings
- header patch moved from sources to cvs

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0:0.0.8-16.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Jiri Skala <jskala@redhat.com> - 0:0.0.8-15
- replaced config directive before arptables_jf init script 

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.8-13
- fix license tag
- drop conflicts

* Thu Apr 03 2008 Martin Nagy <mnagy@redhat.com> - 0.0.8-12
- compile with proper CFLAGS
- add %%{_smp_mflags}

* Mon Feb 25 2008 Martin Nagy <mnagy@redhat.com> - 0.0.8-11
- fix init script (#237778)
- add LSB header (#246868)

* Mon Feb 11 2008 Martin Nagy <mnagy@redhat.com> - 0.0.8-10
- rebuild for gcc-4.3

* Wed Aug 29 2007 Maros Barabas <mbarabas@redhat.com> - 0:0.0.8-9
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0:0.0.8-8
- rebuild
- Add patch to not include linux/compiler.h
- Remove br on glibc-kernheaders, part of the build-env.

* Fri May 26 2006 Jay Fenlason <fenlason@redhat.com> 0:0.0.8-7
- Add warnings patch to close
  bz#191688 arptables_jf fails to build in mock

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0:0.0.8-6.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0:0.0.8-6.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Aug 18 2005 Florian La Roche <laroche@redhat.com>
- change the requires into a conflicts for "kernel"

* Thu Jun 9 2005 Jay Fenlason <fenlason@redhat.com> 0.0.8-5
- add -man patch to correct the names of the default tables.
  bz#123089 aptables man pages is not correct: built in chain name are wrong.

* Tue Mar 8 2005 Jay Fenlason <fenlason@redhat.com> 0.0.8-4
- rebuilt with gcc4

* Fri Nov 26 2004 Florian La Roche <laroche@redhat.com>
- add a %%clean target into .spec

* Tue Aug 31 2004 Jay Fenlason <fenlason@redhat.com> 0.0.8-2
- backport latest version from 3E branch.
- Add 2.6-kernel patch, since glibc_kernheaders has incorrect
  arptables headers for the 2.6 kernel.

* Mon Jul 7 2003 Jay Fenlason <fenlason@redhat.com> 0.0.2-0
- first attempt at a packaged version of arptables_jf, for
  cambridge.
