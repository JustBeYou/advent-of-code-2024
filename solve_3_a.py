from string import digits

def mul(s):
    r = 0
    i = 0
    enabled = True
    while i < len(s):
        # enable/disable instructions
        if s[i:].startswith("do()"):
            i += 4
            enabled = True
            continue

        if s[i:].startswith("don't()"):
            i += 7
            enabled = False
            continue

        # read function invocation
        if s[i:i+4] != "mul(":
            i += 1
            continue

        i += 4

        # read first argument
        a, len_a = consume_number(s[i:])
        if a is None:
            continue
        i += len_a
        if i > len(s) or s[i] != ',':
            continue
        i+= 1

        # read second argument
        b, len_b = consume_number(s[i:])
        if b is None:
            continue
        i += len_b
        if i > len(s) or s[i] != ')':
            continue

        # compute mul and sum
        if enabled:
            r += a * b

    return r


def consume_number(s):
    acc = ""
    for c in s:
        if c not in digits:
            break

        acc += c

    if len(acc) == 0:
        return None, 0

    return int(acc), len(acc)

def test_consume_number():
    assert consume_number("2345") == (2345, 4)
    assert consume_number("1234,,,123") == (1234, 4)
    assert consume_number("#") == (None, 0)

def test_mul():
    assert mul("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))") == 161
    assert mul("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))") == 48

test_consume_number()
test_mul()

with open('input_3.txt') as f:
    print(mul(f.read()))