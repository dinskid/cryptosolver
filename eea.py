#!/usr/bin/python3

import math


def extended_euclidean_algorithm(a, b, verbose):

    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    if verbose:
        print("q\tr1\tr2\tr\ts1\ts2\ts\tt1\tt2\tt")

    while (r2 > 0):
        q = r1//r2

        r = r1 - q * r2
        s = s1 - q*s2
        t = t1 - q * t2

        if verbose:
            print(q, r1, r2, r, s1, s2, s, t1, t2, t, sep="\t")

        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t

    if verbose:
        print(" ", r1, r2, " ", s1, s2, " ", t1, t2, "\n", sep="\t")

    return r1, s1, t1


eea = extended_euclidean_algorithm  # Alias

if __name__ == '__main__':
    n = int(input("Value of a : "))
    b = int(input("Value of b : "))
    verbose = bool(input("Require process? ('1' - Yes) (Empty - No)"))
    gcd, S1, T1 = eea(a=n, b=b, verbose=verbose)

    print(f"GCD = {r1}, S1 = {s1}, T1 = {t1}")
