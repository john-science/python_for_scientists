cimport cython

@cython.locals(m=cython.int, i=cython.int, j=cython.int, numbers=list, primes=list)
cpdef list sieve(int n)
