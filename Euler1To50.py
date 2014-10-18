# Abstracted methods used in multiple problems:

# check_prime is used in problems 3 and 7
def check_prime(n):
	print "checking prime: " + str(n)
	# +1 is added because the end of the range function is exclusive
	end_of_tmp_range = int(n**0.5)+1
	if n % 2 == 0:
		return False
	for i in range(3,end_of_tmp_range,2):
		if n % i == 0:
			return False
	return True


# Project Euler Problem 1 SOLVED
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

count_problem_1 = 0
for x in xrange(0,1000):
	if x % 3 == 0:
		count_problem_1 += x
	elif x % 5 == 0:
		count_problem_1 += x
print count_problem_1

# ----------------------------------------------------------------------------

# Project Euler Problem 2 SOLVED
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

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

# counter_problem_2 will act as n in this case
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
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

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

# Project Euler Problem 5 SOLVED
# Probably should be refactored as well. Nested if statements make me cringe. Honestly, one plausible idea is 
# to find the lcm of some of the ints in the narrowed scope... 

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

# ----------------------------------------------------------------------------

# Project Euler Problem 6 SOLVED
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the 
# sum is 3025 minus 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square 
# of the sum.

sum_of_squares = 0
square_of_sum = 0
for i in xrange(0,101):
	sum_of_squares += i**2
	square_of_sum += i
square_of_sum = square_of_sum**2
print "difference: " + str(sum_of_squares - square_of_sum)

# ----------------------------------------------------------------------------

# Project Euler Problem 7 SOLVED
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Using the fact that all primes are either (6n-1) or (6n+1)

# this will serve as n in our prime trick calculations
counter_problem_7 = 3
prime_list = [2,3,5,7,11,13]
while len(prime_list) != 10001:
	lower_prime = (6*counter_problem_7)-1
	upper_prime = (6*counter_problem_7)+1
	if check_prime(lower_prime) == True and len(prime_list) != 10001:
		prime_list.append(lower_prime)
	if check_prime(upper_prime) == True and len(prime_list) != 10001:
		prime_list.append(upper_prime)
	counter_problem_7 += 1
# this is just cool because it actually has over 100000 primes in it
print prime_list
# should be the 10001 element
print "10001st: " + str(prime_list[10000])

# ----------------------------------------------------------------------------

# Project Euler Problem 8 SOLVED
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 * 9 * 8 * 9 = 5832.
# this thousand digit number is a long
thousand_digit_number = int("""
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace("\n", ""))
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value 
# of this product?

# this sounds like a little interval search and multiply

greatest_product_problem_eight = (0,0,0)
thousand_digit_string = str(thousand_digit_number)
digit_map_problem_eight = map(int,thousand_digit_string)
for start_digit_problem_eight in xrange(0,len(digit_map_problem_eight)):
	# 988 / 13 = 76
	if start_digit_problem_eight < 987:
		tmp_product_problem_eight = 1
		for one_of_thirteen_digits in xrange(0,13):
			tmp_product_problem_eight = tmp_product_problem_eight * digit_map_problem_eight[start_digit_problem_eight + one_of_thirteen_digits]
	else:
		tmp_product_problem_eight = 1
		end_digit_problem_eight = 1000 - start_digit_problem_eight
		for one_of_thirteen_digits in xrange(0,end_digit_problem_eight):
			tmp_product_problem_eight = tmp_product_problem_eight * digit_map_problem_eight[start_digit_problem_eight + one_of_thirteen_digits]
	print "tmp_product_problem_eight: " + str(tmp_product_problem_eight)
	if tmp_product_problem_eight > greatest_product_problem_eight[0]:
		greatest_product_problem_eight = (tmp_product_problem_eight,start_digit_problem_eight,start_digit_problem_eight+13)
print greatest_product_problem_eight









