# Six-Divisor Pairs, abc Triples, and the Square Nagell–Ljunggren Equation

Verification code for the paper by Zephyre Weatherford.

`check.py` uses exact integer arithmetic and needs only Python 3, with no external packages. It checks:

- the congruences modulo 3481 = 59² used for the base 2401 (Corollary 2 and Lemma 7);
- the least exponents e with 243^e ≡ −2 (mod 7^(2+j)) for j = 0, 1, 2, 3;
- a higher-power example for the 2401 branch;
- every exponent and period in Table 1.

## Run

```
python3 check.py
```

Expected output:

```
0 49 42 1
1 343 294 127
2 2401 2058 421
3 16807 14406 421
Table 1: all 8 rows verified
```
