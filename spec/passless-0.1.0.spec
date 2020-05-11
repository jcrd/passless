Name: passless
Version: 0.1.0
Release: 1%{?dist}
Summary: A declarative password manager based on lesspass

License: MIT
URL: https://github.com/jcrd/passless
Source0: https://github.com/jcrd/passless/archive/v0.1.0.tar.gz

BuildArch: noarch

BuildRequires: perl

Requires: gnupg2
Requires: iniq
Requires: python-lesspass

%global debug_package %{nil}

%description
passless manages a user-edited GPG-encrypted file containing arguments for the lesspass command-line client.

%prep
%setup

%build
%make_build PREFIX=/usr

%install
%make_install PREFIX=/usr

%files
%license LICENSE
%doc README.md
/usr/bin/%{name}
/usr/share/man/man1/%{name}.1.gz

%changelog
* Mon May 11 2020 James Reed <jcrd@tuta.io> - 0.1.0
- Initial package
