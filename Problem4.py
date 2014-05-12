# Find the largest palindrome made from the product of two 3-digit numbers.

# smallest three digit number is 100
# largest three digit number is 999

def largest_palindrome():
    # we need to store N1 en N2 and the largest palindrome as a check
    palin = 0
    for n1 in range(100,1000):
        for n2 in range(100,1000):
            res = n1 * n2
            if str(res) == str(res)[::-1] and res > palin:
                palin = res
    return palin

print largest_palindrome()