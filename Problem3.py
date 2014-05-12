# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# implement in two steps:
# find list of prime factors of given number
# select highest numbet in list

def greatest_prime(n):
    # used http://www.dreamincode.net/forums/topic/228408-algorithm-for-finding-the-prime-factorization-of-a-number/ for inspiration
    # limited range so function will computer
    primes = []
    for i in range(2, 100000):
        while n % i == 0:
            primes.append(i)
            n /= i
    return max(primes)

#print greatest_prime(13195)
print greatest_prime(600851475143)