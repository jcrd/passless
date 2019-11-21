#!/bin/sh

test_description='Test passless'

. ./sharness/sharness.sh

# abort if `iniq` dependency is not found
command -v iniq > /dev/null || exit 1

cd "$SHARNESS_TEST_DIRECTORY" || exit 1

export PASSLESS_PLAIN_FILE=true
export PASSLESS_CONFIG='passless.ini'
export LESSPASS_MASTER_PASSWORD=test_password

test_expect_success 'List sites' '
test "$(passless)" = "example.com
false.com
master.net"
'

test_expect_success 'Test example.com' '
test "$(passless example.com)" = "$(lesspass example.com myusername \
    --no-lowercase --length 12 --counter 2)"
'

test_expect_success 'Test false.com' '
test "$(passless false.com)" = "$(lesspass false.com name \
    --no-uppercase --no-symbols --no-digits)"
'

test_expect_success 'Test master.net' '
test "$(passless master.net)" = "$(lesspass master.net login best_password)"
'

test_done

# vim: ft=sh
