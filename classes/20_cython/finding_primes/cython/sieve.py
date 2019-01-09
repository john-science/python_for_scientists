
def sieve(n):
    """ The Sieve of Eratosthenes
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
