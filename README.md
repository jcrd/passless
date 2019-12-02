# passless [![CircleCI](https://circleci.com/gh/jcrd/passless.svg?style=svg)](https://circleci.com/gh/jcrd/passless)

passless manages a user-edited GPG-encrypted file containing arguments for the
[lesspass](https://pypi.org/project/lesspass/) command-line client.

## Usage

```
usage: passless [options] [SITE]

options:
  -h         Show help message
  -f CONFIG  Path to config file
  -i FILE    Encrypt existing file
  -e         Edit config file
  -l LOGIN   Get password of SITE with given login
  -c         Copy password to clipboard
  -v         Show version
```

## Configuration

The configuration file is an INI file where section names are sites
and section keys correspond to **lesspass** command-line arguments.

If a configuration file doesn't exist, the _-e_ flag will create one using a
default template.

An existing plain configuration file can be encrypted using the _-i_ flag.

Example:
```
[example.com]
login=myusername
symbols=false
counter=2
```

See below for valid keys.

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

## License

This project is licensed under the MIT License (see [LICENSE](LICENSE)).
