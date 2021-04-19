from eea import extended_euclidean_algorithm


def modular_multiplicative_inverse(n: int, b: int, verbose: bool = False):
    gcd, s, t = extended_euclidean_algorithm(n, b, verbose)
    if gcd == 1:
        if verbose:
            print(f'Inverse of {b} in {n} is : {t}')
            if (t < 0):
                print(f"or {t % n}")
        return t % n
    else:
        if verbose:
            print('INV doesnot exists')
        return -1


mmi = modular_multiplicative_inverse  # Alias

if __name__ == "__main__":
    n = int(input("Value of n: "))
    b = int(input("Value of b: "))
    verbose = bool(input("Require process? ('1' - Yes) (Empty - No)"))
    mmi(n, b, verbose)
