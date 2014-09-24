# 2520 is the smallest number that can be divided by
# each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?

# nicest way to implement is using prime factorization. If we factorize every element, we can take away doubles and multiple the primes that are left

# For now a less elegant solution. -
# Start with hight number in range. Test if it can be divided by all lower numbers
# As soon as not, increase the highest number with itself

# Even less elegant solution, brute force it.
# while hightest number is not divisible by 2 -- 20, increase by 20 until all conditions are valid
# I bow my head in shaaaame

def smallest(n):
    number = n;

    while number %  2 != 0 or number %  3 != 0 or number %  4 != 0 or number %  5 != 0 or number %  6 != 0 or number %  7 != 0 or number %  8 != 0 or number %  9 != 0 or number % 10 != 0 or number % 11 != 0 or number % 12 != 0 or number % 13 != 0 or number % 14 != 0 or number % 15 != 0 or number % 16 != 0 or number % 17 != 0 or number % 18 != 0 or number % 19 != 0 or number % 20 != 0:
        number += n
    return number

print smallest(20)
