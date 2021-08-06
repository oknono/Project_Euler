# Update using PDF from Euler Website 28 September
# This works with larger numbers as well!
# Two importan steps:
# 1. sum of all numbers divisible by x or y is equal to
#   ( sum of all numbers divisible by x +
#	sum of all numbers divisible by x ) -
#	sum of all numbers divisible by x * y
# 2. The sum of all multiples of x can be rewritten from
# 	- [x, 2x, 3x, 4x, ...] to
#   - x * [1,2,3,4... floor(target / x) ]
import math

target = 999


def sum_divisible_by(n):
    p = math.floor(target / n)  # step 2
    return n * ((p * (p + 1)) / 2)


print(sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15))  # step 1
