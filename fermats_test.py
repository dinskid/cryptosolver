#!/usr/bin/python3

from eulers import fermats


def fermats_primality_test(n: int, a: int = 2, verbose: bool = False):
    soln = fermats(a, n-1, n, verbose)
    return soln == 1


isprime_fermats = fermats_primality_test

if __name__ == '__main__':
    n = int(input('Enter the value of the n: '))
    a = int(input('Enter the base (if mentioned in the question else -1): '))
    verbose = bool(input("Require process? ('1' - Yes) (Empty - No)"))

    if a == -1:
        prime = isprime_fermats(n, verbose=verbose)
    else:
        prime = isprime_fermats(n, a, verbose=verbose)

    if prime:
        print(f'According to Fermat\'s test {n} is a prime')
    else:
        print(f'According to Fermat\'s test {n} is a not prime')

    print(f'Please note that {n} may or may not be prime - the result here is \
just according to Fermat\'s test')
