Name: passless
Version: 0.4.0
Release: 1%{?dist}
Summary: A declarative password manager based on lesspass

License: MIT
URL: https://github.com/jcrd/passless
Source0: https://github.com/jcrd/passless/archive/v0.4.0.tar.gz

BuildArch: noarch

BuildRequires: perl

# Required for testing.
BuildRequires: iniq
BuildRequires: python-lesspass

Requires: bash
Requires: gawk
Requires: coreutils
Requires: gnupg2
Requires: iniq
Requires: python-lesspass
Requires: xsel

Recommends: rofi
Recommends: git

%global debug_package %{nil}

%description
passless manages a user-edited GPG-encrypted file containing arguments for the lesspass command-line client.

%prep
%setup

%build
%make_build PREFIX=/usr

%install
%make_install PREFIX=/usr

%check
make test

%files
%license LICENSE
%doc README.md
/usr/bin/%{name}
/usr/bin/%{name}-rofi
/usr/share/man/man1/%{name}.1.gz

%changelog
* Wed Jan 26 2022 James Reed <james@twiddlingbits.net> - 0.4.0-1
- Release v0.4.0

* Tue Aug 10 2021 James Reed <james@twiddlingbits.net> - 0.3.0-1
- Release v0.3.0

* Wed Apr 14 2021 James Reed <james@twiddlingbits.net> - 0.2.3-1
- Release v0.2.3

* Tue Apr 13 2021 James Reed <james@twiddlingbits.net> - 0.2.2-1
- Release v0.2.2

* Fri Dec 18 2020 James Reed <jcrd@tuta.io> - 0.2.1-1
- Release v0.2.1

* Sat Nov 28 2020 James Reed <jcrd@tuta.io> - 0.2.0-1
- Release v0.2.0

* Mon Jun 15 2020 James Reed <jcrd@tuta.io> - 0.1.2-2
- Add missing requires: bash, gawk, coreutils

* Wed Jun 10 2020 James Reed <jcrd@tuta.io> - 0.1.2-1
- Release v0.1.2

* Mon Jun  1 2020 James Reed <jcrd@tuta.io> - 0.1.1-1
- Release v0.1.1
- Recommends rofi for using passless-rofi

* Mon May 11 2020 James Reed <jcrd@tuta.io> - 0.1.0
- Initial package
