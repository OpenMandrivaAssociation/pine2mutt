%define name pine2mutt
%define version 0.3
%define release  9

Summary: Makes mutt behave somewhat pine-like
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch: %name-makefile.patch.bz2
License: GPL
URL: http://www.netmeister.org/apps/pine2mutt/index.html
Group: Networking/Mail
Buildarch: noarch

%description
Pine2mutt is a simple perl-script interesting to people who switch from using
pine to mutt. It converts pine's .addressbook into mutt-readable aliases,
enables pine-like sent-mail-folder handling and provides pine-like keybindings
by sourcing the file "Pine.rc" which comes with mutt.

%prep

%setup

%patch -p1

%build

%install
export DESTDIR=%{buildroot}

mkdir -p %{buildroot}%_bindir
mkdir -p %{buildroot}%_mandir/man1

make install

%clean

%files
%doc README COPYING
%_bindir/*
%_mandir/man1/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.3-8mdv2010.0
+ Revision: 430736
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-7mdv2009.0
+ Revision: 259065
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-6mdv2009.0
+ Revision: 246980
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.3-4mdv2008.1
+ Revision: 125377
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import pine2mutt


* Wed May 11 2005 Lenny Cartier <lenny@mandriva.com> 0.3-4mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.3-3mdk
- rebuild

* Wed Jan 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.3-2mdk
- rebuild

* Mon Dec 03 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3-1mdk
- 0.3
- refresh patch

* Thu Aug 30 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.2-4mdk
- rebuild

* Tue Mar 20 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.2-3mdk
- rebuild

* Wed Jan 24 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.2-2mdk
- rebuild

* Thu Nov 16 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.2-1mdk
- used srpm from Jan  Schaumann <jschauma@netmeister.org> 0.2-1mdk
	- Changed mutt's default alias-file to "~/.pine2mutt":
  	People might use "~/.aliases" for bash-aliases (for example) or
  	otherwise.
	- added new feature: pine-like sent-mail-folder handling
	- added new feature: Mutt provides a "Pine.rc" file which we source
  	to enable pine-like key-bindings

* Thu Nov 09 2000 Jan Schaumann <jschauma@netmeister.org> 0.1-1mdk
- First RPM package
