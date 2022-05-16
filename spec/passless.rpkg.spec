Name: {{{ git_cwd_name name="passless" }}}
Version: {{{ git_cwd_version lead="$(git tag | sed -n 's/^v//p' | sort --version-sort -r | head -n1)" }}}
Release: 1%{?dist}
Summary: A declarative password manager based on lesspass

License: MIT
URL: https://github.com/jcrd/passless
VCS: {{{ git_cwd_vcs }}}
Source0: {{{ git_cwd_pack }}}

BuildArch: noarch

BuildRequires: perl

# Required for testing.
BuildRequires: iniq >= 0.4.0
BuildRequires: python-lesspass

Requires: bash
Requires: gawk
Requires: coreutils
Requires: gnupg2
Requires: iniq >= 0.4.0
Requires: python-lesspass
Requires: xsel

Recommends: rofi
Recommends: git

%global debug_package %{nil}

%description
passless manages a user-edited GPG-encrypted file containing arguments for the lesspass command-line client.

%prep
{{{ git_cwd_setup_macro }}}

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
{{{ git_cwd_changelog }}}
