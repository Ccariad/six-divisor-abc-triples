C, modulus = 2401, 59**2
assert pow(C, 665, modulus) == modulus - 2
assert pow(C, 1711, modulus) == 1
assert pow(C, 29, modulus) == 886

expected = [1, 127, 421, 421]
for j in range(4):
    modulus = 7**(2 + j)
    order = 6 * 7**(j + 1)
    residue = 1
    for e in range(1, order + 1):
        residue = (243 * residue) % modulus
        if residue == modulus - 2:
            break
    else:
        raise AssertionError("Target residue not found")
    assert e == expected[j]
    print(j, modulus, order, e)

# Expected output: j, modulus, order, least positive e
# 0    49     42      1
# 1    343    294     127
# 2    2401   2058    421
# 3    16807 14406    421
assert pow(2401, 29, 59) == 1
assert pow(2401, 29, 59**2) == 886
assert 23**2 % 59 == 59 - 2
assert pow(2401, 830500, 5**4) == 1
assert pow(2401, 830500, 59**3) == 59**3 - 2

# Verify Table 1: (base, j, k, least exponent, period).
rows = [
    (243, 0, 0, 1, 42),
    (243, 1, 0, 127, 294),
    (243, 0, 1, 253, 462),
    (243, 1, 1, 715, 3234),
    (2401, 0, 0, 665, 8555),
    (2401, 1, 0, 325755, 504745),
    (2401, 0, 1, 17775, 42775),
    (2401, 1, 1, 830500, 2523725),
]
for base, j, k, least, period in rows:
    prime, factor = (7, 6) if base == 243 else (59, 29)
    modulus = prime**(j + 2)
    order = factor * prime**(j + 1)
    divisor = 11**k if base == 243 else 5**(k + 1)
    residue = 1
    for e in range(1, order + 1):
        residue = residue * base % modulus
        if residue == modulus - 2:
            break
    else:
        raise AssertionError("Target residue not found")
    candidates = [e + order*t for t in range(divisor)
                  if (e + order*t) % divisor == 0]
    assert candidates == [least]
    assert period == order * divisor
print("Table 1: all 8 rows verified")
# Expected final line: Table 1: all 8 rows verified
