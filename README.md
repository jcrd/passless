# passless ![test](https://github.com/jcrd/passless/actions/workflows/test.yml/badge.svg)

passless manages a user-edited GPG-encrypted file containing arguments for the
[lesspass](https://pypi.org/project/lesspass/) command-line client.

## Packages

* **RPM** package available from [copr][1]. [![Copr build status](https://copr.fedorainfracloud.org/coprs/jcrd/passless/package/passless/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/jcrd/passless/package/passless/)

  Install with:
  ```
  dnf copr enable jcrd/passless
  dnf install passless
  ```

## Usage

```
usage: passless [options] [command|SITE]

options:
  -h            Show help message
  -f CONFIG     Path to config file
  -l LOGIN      Get password of SITE with given login
  -s            Print password
  -p            Push commits to git remote after editing
  -P            Do not pull from git remote before editing
  -v            Show version

commands:
  edit          Edit config file
  list          List sites and logins
  find          Select site with fuzzy finder
  log           Show git commit log
  status        Show git status
  push          Push commits to git remote
  pull          Pull commits from git remote
  encrypt FILE  Encrypt existing file
```

### Automatic sync with remote git repository
If passless detects that its configuration file exists in a git repository,
it will:
* pull changes from remote before editing
* commit after editing and re-encryption
* push commits when the `-p` flag is present
  (allows amending commits before push)

Set up a local git repository using the remote `origin` and branch `master`:
```sh
cd ~/.config/passless
git init
git remote add origin <remote-url>
git branch --set-upstream-to origin/master
```

## Configuration

The configuration file is an INI file where section names are sites
and section keys correspond to **lesspass** command-line arguments.

If a configuration file doesn't exist, the _edit_ command will create one using
a default template.

An existing plain configuration file can be encrypted using the _encrypt_
command.

Example:
```
[example.com]
login=myusername
symbols=false
counter=2
```

See below for valid keys.

* `master_password=`

The master password.
Corresponds to **lesspass** _MASTER_PASSWORD_ argument.

* `login=`

The site login.
Corresponds to **lesspass** _LOGIN_ argument.

* `length=`

The generated password length.
Corresponds to **lesspass** _--length_ flag.

* `counter=`

Password counter.
Corresponds to **lesspass** _--counter_ flag.

* `lowercase=`

Include lowercase in password if set to `true`.
Corresponds to **lesspass** _--lowercase_ or _--no-lowercase_ flags.

* `uppercase=`

Include uppercase in password if set to `true`.
Corresponds to **lesspass** _--uppercase_ or _--no-uppercase_ flags.

* `digits=`

Include digits in password if set to `true`.
Corresponds to **lesspass** _--digits_ or _--no-digits_ flags.

* `symbols=`

Include symbols in password if set to `true`.
Corresponds to **lesspass** _--symbols_ or _--no-symbols_ flags.

* `password=`

Use this password instead of generating one.

## License

This project is licensed under the MIT License (see [LICENSE](LICENSE)).

[1]: https://copr.fedorainfracloud.org/coprs/jcrd/passless/
