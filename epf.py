#!/usr/bin/python3

from collections import Counter
import sympy
import math

def euler_phi_function(n: int, verbose: bool=False):
    prime_factors = sympy.primefactors(n)
    factors_count = dict(Counter(prime_factors))
    step1 = []
    step2 = []
    step3 = []
    phi = 1

    for i in factors_count:
        temp = math.pow(i, factors_count[i]) - math.pow(i,factors_count[i]-1)
        step1.append (f"({i}^{factors_count[i]} - {i}^({factors_count[i]} - 1))")
        step2.append (f"({i}^{factors_count[i]} - {i}^{factors_count[i] - 1})")
        step3.append (f"({temp})")
        phi *= temp
    if verbose: 
        print(f" φ({n}) =",end= " ")
        print(*step1,sep = " X ")
        print(f" φ({n}) =",end= " ")
        print(*step2,sep = " X ")
        print(f" φ({n}) =",end= " ")
        print(*step3,sep = " X ")
    return int(phi)

phi = euler_phi_function

if __name__ == "__main__":
    n = int(input("Value of n : "))
    verbose = bool(input("VERBOSE : ('1' - Yes), (Enter - No) : "))

    print(f" φ({n}) =", phi(n,verbose))
