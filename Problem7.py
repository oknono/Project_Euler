# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# we will run through number starting at 2. If a number is prime, we increase the counter. As soon as the counter is equal to 10 001, we want the prime number that raised the counter

def prime_no(n):
    counter = 0
    x = 1
    while counter < n:
        x +=1
        if is_prime(x):
            counter += 1
    return x

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


print prime_no(10001)
