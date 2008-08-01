%define name pine2mutt
%define version 0.3
%define release %mkrel 7

Summary: Pine2mutt makes mutt behave somewhat pine-like
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch: %name-makefile.patch.bz2
License: GPL
URL: http://www.netmeister.org/apps/pine2mutt/index.html
Group: Networking/Mail
Buildroot: %{_tmppath}/%{name}-buildroot
Buildarch: noarch

%description
Pine2mutt is a simple perl-script interesting to people who switch from using
pine to mutt. It converts pine's .addressbook into mutt-readable aliases,
enables pine-like sent-mail-folder handling and provides pine-like keybindings
by sourcing the file "Pine.rc" which comes with mutt.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%patch -p1

%build

%install
export DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT%_mandir/man1

make install

%clean

%files
%defattr(-,root,root)
%doc README COPYING
%_bindir/*
%_mandir/man1/*

