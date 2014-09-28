# Update using PDF from Euler Website 28 September
# This works with larger numbers as well!
# Note that 3 + 6 + 9 + ... is equal to
# 3 * (1 + 2 + 3 + ...) etc.

target = 999999999

def sum_divided_by(n):
	reduced_number = target / n
	return n * (reduced_number * (reduced_number + 1)) / 2

print sum_divided_by(3) + sum_divided_by(5) - sum_divided_by(15)