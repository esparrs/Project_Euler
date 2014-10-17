# Project Euler Problem 1 SOLVED
count_problem_1 = 0
for x in xrange(0,1000):
	if x % 3 == 0:
		count_problem_1 += x
	elif x % 5 == 0:
		count_problem_1 += x
print count_problem_1

# ----------------------------------------------------------------------------

# Project Euler Problem 2 SOLVED
# Example 1: Using looping technique
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print fib(6)
 
# Example 2: Using recursion
def fibR(n):
 if n==1 or n==2:
  return 1
 return fib(n-1)+fib(n-2)
print fibR(7)

# Example 4: Using memoization
def memoize(fn, arg):
 memo = {}
 if arg not in memo:
  memo[arg] = fn(arg)
  return memo[arg]
 
# fib() as written in example 1.
fibm = memoize(fib,5)
print fibm

counter_problem_2 will act as n in this case
counter_problem_2 = 0
# keeps track of last number as part of fibonacci sequence
last_fib = 0
even_sum_problem_2 = 0
while last_fib < 4000000:
	fibn = memoize(fib,counter_problem_2)
	if fibn % 2 == 0 and fibn < 4000000:
		even_sum_problem_2 += fibn
	last_fib = fibn
	counter_problem_2 += 1
print even_sum_problem_2

# ----------------------------------------------------------------------------

# Project Euler Problem 3 SOLVED!!!!!
def check_prime(n):
	print "checking prime"
	end_of_tmp_range = int(n**0.5)
	if n % 2 == 0:
		return False
	for i in range(3,end_of_tmp_range,2):
		if n % i == 0:
			return False
	return True

largest_prime = 0
other_factor_problem_three = 0
end_of_range = int(600851475143**0.5)

# only odd numbers
for current in xrange(1,end_of_range):
	if 600851475143 % current == 0:
		print current
		if check_prime(current) == True:
			largest_prime = current
		other_factor_problem_three = float(600851475143) / float(current)
		if check_prime(other_factor_problem_three) == True:
			print "other factor: " + str(other_factor_problem_three)
			break 
print "largest_prime: " + str(largest_prime)

# ----------------------------------------------------------------------------

# Project Euler Problem 4 SOLVED
# Should look to refactor and get rid of all of the for loops - this is not pretty by any stretch of the
# imagination

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit 
# numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# 999*999 = 998001
# with six digit numbers, 0 = 5, 1 = 4, 2 = 3
# 100*100 = 10000
# with five digit numbers, 0 = 4, 1 = 3, 2

# Instead of just going through all of the three digit numbers (and respective multiplication)
# let's just try the palindromes between 10000 and 998001
# Heuristically speaking, we should start with the 6 digit palidromes

# Build string of palindrome

greatest_palidromes = []
digit_list = [0,0,0,0,0,0]
for i in xrange(9,-1,-1):
	digit_list[0] = str(i)
	digit_list[5] = str(i)
	for j in xrange(9,-1,-1):
		digit_list[1] = str(j)
		digit_list[4] = str(j)
		for k in xrange(9,-1,-1):
			digit_list[2] = str(k)
			digit_list[3] = str(k) 
			palindrome = ''.join(digit_list)
			print palindrome
			for l in xrange(100,999):
				if int(palindrome) != 0 and int(palindrome) % l == 0:
					other_factor_problem_four = int(palindrome) / l
					if other_factor_problem_four > 99 and other_factor_problem_four < 1000:
						greatest_palidromes.append((int(palindrome),l,other_factor_problem_four))
print "greatest palidrome: " + str(greatest_palidromes[0])
					
# ----------------------------------------------------------------------------

# Project Euler Problem 5 
# Probably should be refactored as well. Nested if statements make me cringe

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the
# numbers from 1 to 20?

# If it's divisible by 20, it's then divisible by 1,2,4,5, and 10
# In addition, if it's divisible by 18, it's then divisible by 3,6,9, and any combination of the multiples of 
# 18 and 20: 12 and 15
# In addition, if it's divisble by 16, it's then divisible by 8 as well
# In addition, if it's divisble by 14, it's then divisible by 7 as well
# We then have narrowed the scope to 20,19,18,17,16,14,13, and 11

counter_problem_5 = 40
evenly_divisble_bool = False
while evenly_divisble_bool == False:
	if counter_problem_5 % 19 == 0:
		if counter_problem_5 % 18 == 0:
			if counter_problem_5 % 17 == 0:
				if counter_problem_5 % 16 == 0:
					if counter_problem_5 % 14 == 0:
						if counter_problem_5 % 13 == 0:
							if counter_problem_5 % 11 == 0:
								evenly_divisble_bool = True
	counter_problem_5 += 20
counter_problem_5 -= 20
print "evenly divisible number: " + str(counter_problem_5)
