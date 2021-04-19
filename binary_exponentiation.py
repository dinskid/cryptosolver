#!/usr/bin/python3

def binaray_exponentiation_under_modulo(n: int, e: int, m: int = 1, verbose: bool = False):
    # TODO: add verbose functionality

    assert(m >= 0)
    if e == 0:
        return 1
    if e == 1:
        return n

    x = binaray_exponentiation_under_modulo(n, e//2, m)

    soln = (x*x) % m
    if e % 2 == 0:
        return soln

    # odd case
    soln *= n
    soln %= m
    return soln


binexp = binaray_exponentiation_under_modulo

if __name__ == '__main__':
    base = int(input('Enter the value of the base: '))
    exp = int(input('Enter the value of the exponent: '))
    mod = int(input('Enter the value of the modulo: '))
    # verbose = bool(input("Require process? ('1' - Yes) (Empty - No)"))

    print(f'({base}^{exp})%{mod} = {binexp(base, exp, mod, verbose)}')
