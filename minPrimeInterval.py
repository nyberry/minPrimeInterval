import math


def solve(left, right):

    # call a function to return a list of all primes between left and right inclusive
    primes = listPrimes(left, right)

    # call a function to iterate through list finding the interval between consecutive elements, returning the pair with the minimum interval. The pair with smallest num1 if multiple smallest pairs.
    solution = findMinInterval(primes)

    if solution:
        return solution


# function to return a list of all primes between left and right inclusive
def listPrimes(left, right):
    primes = []
    for n in range(left, right + 1):
        if isPrime(n):
            primes.append(n)
    return primes


# recursive function to check if n is prime
def isPrime(n, divisor=None):
    if n < 2:
        return False
    if divisor is None:
        divisor = int(math.sqrt(n))
    if divisor < 2:
        return True
    if n % divisor == 0:
        return False
    return isPrime(n, divisor - 1)


# a function to iterate through list finding the interval between consecutive elements, returning the pair with the minimum interval. The pair with smallest num1 if multiple smallest pairs.
def findMinInterval(primes):

    if len(primes) < 2:
        return None

    minPair = None
    minInterval = math.inf

    for i in range(len(primes) - 2):
        num1 = primes[i]
        num2 = primes[i + 1]
        diff = num2 - num1
        if diff < minInterval:
            minPair = [num1, num2]
            minInterval = diff

    return minPair


if __name__ == "__main__":
    solution = solve(3, 19)
    print(solution) if solution else print("No solution")
