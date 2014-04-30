# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
# 3, 5, 6 and 9. The sum of
# these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_3_5(num):
    counter = 0
    for x in xrange(num):
       if x % 3 == 0 or x % 5 == 0:
            counter += x
            # print "x is ", x
            # print "counter is ", counter
    print counter

sum_3_5(1000)
