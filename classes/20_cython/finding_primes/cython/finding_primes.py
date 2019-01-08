from timeit import timeit

def main():
    number_trials = 3
    max_prime = 10000

    print("\nNaive, first pass at the Sieve of Eratosthenes:")
    print(timeit("seive_naive(" + str(max_prime) + ")", "from __main__ import seive_naive", number=3))

    print("\nA decent pass at the Sieve of Eratosthenes:")
    print(timeit("seive_decent(" + str(max_prime) + ")", "from __main__ import seive_decent", number=3))


def seive_naive(n):
    """ The Sieve of Eratosthenes - first pass
    """
    # Python indexes start at zero
    m = n + 1

    # make a list of for all numbers up to n, initially all prime
    numbers = [True for i in range(m)]

    # go through and remove all numbers that are a multiple of the others
    for i in range(2, n + 1):
      if numbers[i]:
        for j in range(i * i, m, i):
          numbers[j] = False

    # what is left are primes
    primes = []
    for i in range(2, m):
      if numbers[i]:
        primes.append(i)

    return primes


def seive_decent(n):
    """ The Sieve of Eratosthenes:
        a couple small speed improvements
    """
    # Python indexes start at zero
    m = n + 1

    # make a list of for all numbers up to n, initially all prime
    numbers = [True] * m  # NOTE: faster due to Python magic

    # go through and remove all numbers that are a multiple of the others
    for i in range(2, int(n**0.5 + 1)):  # NOTE: faster due to basic math
      if numbers[i]:
        for j in range(i * i, m, i):
          numbers[j] = False

    # what is left are primes
    primes = []
    for i in range(2, m):
      if numbers[i]:
        primes.append(i)

    return primes


if __name__ == '__main__':
    main()
