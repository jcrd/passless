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
master.net
samesite.com
samesite.com
badsite.com"
'

test_expect_success 'List sites and logins' '
test "$(passless list)" = "example.com | myusername
false.com | name
master.net | login
samesite.com | login1
samesite.com | login2
badsite.com | username"
'

test_expect_success 'Test example.com' '
test "$(passless -s example.com)" = "$(lesspass example.com myusername \
    --no-lowercase --length 12 --counter 2)"
'

test_expect_success 'Test false.com' '
test "$(passless -s false.com)" = "$(lesspass false.com name \
    --no-uppercase --no-symbols --no-digits)"
'

test_expect_success 'Test master.net' '
test "$(passless -s master.net)" = "$(lesspass master.net login best_password)"
'

test_expect_success 'Get site by login' '
test "$(passless -s -l login1 samesite.com)" = "$(lesspass samesite.com login1)" &&
test "$(passless -s -l login2 samesite.com)" = "$(lesspass samesite.com login2 \
    --no-symbols)"
'

test_expect_success 'Test predefined password' '
test "$(passless -s badsite.com)" = "testpass"
'

test_done

# vim: ft=sh
