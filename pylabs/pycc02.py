# def sum_divisors(n):
#     divisors = [0]
#     for i in range(1, n):
#         total = 0
#         if n == 0:
#             return total
#         elif (n % i)==0:
#             divisors.append(i)
#     return sum(divisors)
# sum1 = 0
# divisor = 0
def sum_divisors(n):
  divisor = 1
  divsum = 0
  if n == 0:
    return divsum
  else:
    while (n > divisor > 0):
      if (n % divisor) == 0:
        divsum = divsum + divisor
      divisor += 1
    return divsum
    
print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 1+2+3+6+17+34+51
# 114


def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = multiplier * number 
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1


def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n >= 0:
    if n == 0:
      return False
    elif n == 1:
      return True
    elif n % 2 == 0:
      return True
    else:
      return False
  # If after dividing by two the number is 1, it's a power of two
  # if n == 1:
  #   return True
  # return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False