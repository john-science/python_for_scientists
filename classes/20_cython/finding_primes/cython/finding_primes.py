from time import time
from sieves import sieve


def main():
    max_prime = 100000

    print("\nA decent pass at the Sieve of Eratosthenes, in Cython:")
    start = time()
    sieve(max_prime)
    print('{0} seconds'.format(time() - start))


if __name__ == '__main__':
    main()
