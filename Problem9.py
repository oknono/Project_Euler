
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# So there are some conditions
# we know that a != b != c
# and 0 < a, b, c < 1000
# and a + b + c = 1000
# and a **2 + b**2 = c**2

# We can do a for loop for a, b and c each
#  check the range
def triplet():
    for a in range (0,501):
        for b in range (1,501):
            for c in range(0,501):
                if a < b and b < c and a + b + c == 1000 and a**2 + b**2 == c**2:
                    return a * b * c
print triplet()