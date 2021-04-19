#!/usr/bin/python3
from epf import phi
from binary_exponentiation import binexp


def eulers(a: int, e: int, m: int, verbose: bool = False):
    p = phi(m)

    k = e//p
    r = e % p
    soln = binexp(a, r, m)
    if verbose:
        print(f'{a}^{e} (mod {m}) = {a}^({k}*{p} + {r} (mod {m}))')
        print(f'{a}^{e} (mod {m}) = {a}^{r} (mod {m})')

    return soln


fermats = eulers

if __name__ == '__main__':
    base = int(input('Enter the value of the base: '))
    exp = int(input('Enter the value of the exponent: '))
    mod = int(input('Enter the value of the modulus: '))
    verbose = bool(input("Require process? ('1' - Yes) (Empty - No)"))

    print(f'{base}^{exp} (mod {mod}) = {eulers(base, exp, mod, verbose)}')
