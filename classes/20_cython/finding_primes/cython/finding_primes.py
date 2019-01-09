from time import time
from sieves import sieve


def main():
    number_trials = 3
    max_prime = 100000

    print("\nA decent pass at the Sieve of Eratosthenes, in Cython:")
    start = time()
    sieve(max_prime)
    print(time() - start)
    #print(timeit("sieve(" + str(max_prime) + ")", "from finding_primes import sieve", number=3))



if __name__ == '__main__':
    main()
