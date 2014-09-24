# Find the difference between the sum of the squares of the first one hundred natural # numbers and the square of the sum.

def prob_six():
    res = 0
    for item1 in range(1,101):
        res += item1
    sum2 = res**2
# print "(1+..+100)2 = " sum2
    sum1 = 0
    for item2 in range(1,101):
        sum1 += item2**2
#  print "(sum 2, 1^2+..+ 100 ^2 = )" sum1
    return sum2-sum1

print prob_six()