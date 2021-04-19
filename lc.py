#!/usr/bin/python3
from eea import eea
from mod_inv import mmi


def linear_congruence_solver(a: int, b: int, m: int, verbose: bool = False):
    # return list of size gcd(a, m) [x0, x1 ...]
    d, s, t = eea(a, m)

    if verbose:
        print(f'GCD of a and m: {d}')

    if b % d != 0:
        print(f'{b} is not divisible by the gcd {d}')
        # No solution empty list
        return []

    # d solutions exist
    solns = []
    if verbose:
        print('Divide the equation by the gcd')
    a //= d
    b //= d
    m //= d
    if verbose:
        print(a, b, m)

    inv = mmi(n=m, b=a)

    x0 = (inv*b) % m
    for i in range(d):
        solns.append(x0+i*m)

    return solns


lc = linear_congruence_solver

if __name__ == '__main__':
    print('ax = b (mod m)')
    a = int(input('Value of a: '))
    b = int(input('Value of b: '))
    m = int(input('Value of m: '))
    verbose = bool(input("Require process? ('1' - Yes) (Empty - No)"))

    solns = lc(a, b, m, verbose)

    if solns:
        print(f'There are {len(solns)} solutions and they are:')
        print(*solns, sep=", ")
    else:
        print('No solutions')
