# Six-Divisor Pairs, abc Triples, and the Square Nagell–Ljunggren Equation

Verification code for my number theory paper.

The paper shows that for integers n > 1, if n − 1 and n both have exactly six divisors, then (1, n − 1, n) is an abc triple if and only if n = 243. It then builds families of abc triples around powers of 243 and 2401.

- Paper: https://doi.org/10.5281/zenodo.24131376
- Paper page on my site: https://www.zephyreweatherford.com/mathematical-research.html
- OEIS sequence A399632: https://oeis.org/A399632
- ORCID: https://orcid.org/0009-0005-1621-4024

## The code

`check.py` recomputes the numbers in the paper using exact integer arithmetic. It needs only Python 3. The proofs themselves are in the paper, and the lemma, corollary and table numbers below match it.

It checks:

- the congruences modulo 3481 = 59² used for the base 2401 (Corollary 2 and Lemma 7)
- the least exponents e with 243^e ≡ −2 (mod 7^(2+j)) for j = 0, 1, 2, 3
- a higher-power example for the 2401 branch
- every exponent and period in Table 1

Run it with:

```
python3 check.py
```

Output:

```
0 49 42 1
1 343 294 127
2 2401 2058 421
3 16807 14406 421
Table 1: all 8 rows verified
```

In the first four lines, the columns are j, the modulus 7^(2+j), the range searched (6 · 7^(j+1)), and the least positive e with 243^e ≡ −2 modulo that modulus. The last line means all eight rows of Table 1 passed.

## Cite

Weatherford, Z. (2026). Six-Divisor Pairs, abc Triples, and the Square Nagell–Ljunggren Equation. Zenodo. https://doi.org/10.5281/zenodo.24131376
