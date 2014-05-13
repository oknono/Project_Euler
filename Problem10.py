#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

def primes_below(n):
    sum = 0
    for x in range(0, n):
        if is_prime(x):
            sum += x
    return sum

# from https://en.wikipedia.org/wiki/Primality_test
def is_prime(num):
    if num <= 3:
        if num <= 1:
            return False
        return True
    if not num%2 or not num%3:
        return False
    for i in range(5, int(num**0.5) + 1, 6):
        if not num%i or not num%(i + 2):
            return False
    return True

print primes_below(10)
print primes_below(2000000)