#!/usr/bin/python3

from mod_inv import mmi
from sympy import gcd


def chinese_remainder_theorem(a: list, m: list, verbose: bool = False):
    assert(gcd(m) == 1)
    M = 1
    for v in m:
        M *= v

    if verbose:
        print('M = ', end='')
        print(*m, sep='*')
        print(f'M= {M}')

    ms = []
    m_invs = []

    for v in m:
        ms.append(M//v)
        m_invs.append(mmi(v, M//v))

    if verbose:
        print('M1, M2 ... Mn: ', end='')
        print(*ms, sep=' ')

        print("M1', M2' ... Mn': ", end='')
        print(*m_invs, sep=' ')

    soln = 0

    if verbose:
        print('Solution x', end='')

    for i in range(len(a)):
        soln += (a[i]*ms[i]*m_invs[i]) % M
        if verbose:
            if i == 0:
                print(' = ', end='')
            else:
                print(' * ', end='')
            print(f'{a[i]}*{ms[i]}*{m_invs[i]}', end='')

    if verbose:
        print()
    return soln % M


crt = chinese_remainder_theorem

if __name__ == '__main__':
    n = int(input('Enter the number of equations: '))

    A = []
    M = []
    for i in range(n):
        a, m = map(int, input(
            'Enter the values of a and m separated by spaces: ').split())
        A.append(a)
        M.append(m)

    verbose = bool(input("Require process? ('1' - Yes) (Empty - No)"))

    print(f'Solution to those set of equations is: {crt(A, M, verbose)}')
