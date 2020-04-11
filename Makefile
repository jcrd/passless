VERSIONCMD = git describe --dirty --tags --always 2> /dev/null
VERSION := $(shell $(VERSIONCMD) || cat VERSION)

PREFIX ?= /usr/local
BINPREFIX ?= $(PREFIX)/bin
MANPREFIX ?= $(PREFIX)/share/man

MANPAGE = passless.1

all: passless $(MANPAGE)

passless: passless.in
	sed "s/VERSION=/VERSION=$(VERSION)/" passless.in > passless
	chmod +x passless

$(MANPAGE): man/$(MANPAGE).pod
	pod2man -n=passless -c=passless -r=$(VERSION) $< $(MANPAGE)

install:
	mkdir -p $(DESTDIR)$(BINPREFIX)
	cp -p passless $(DESTDIR)$(BINPREFIX)
	mkdir -p $(DESTDIR)$(MANPREFIX)/man1
	cp -p $(MANPAGE) $(DESTDIR)$(MANPREFIX)/man1

uninstall:
	rm -f $(DESTDIR)$(BINPREFIX)/passless
	rm -f $(DESTDIR)$(MANPREFIX)/man1/passless.1

clean:
	rm -f passless $(MANPAGE)

test: passless
	$(MAKE) -C test

test-podman: clean
	podman run --rm -v $(shell pwd):/passless:Z -w /passless \
		supplantr/passless make test

.PHONY: all install uninstall clean test
