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
    
#print(sum_divisors(0))
# 0
#print(sum_divisors(3)) # Should sum of 1
# 1
#print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
#print(sum_divisors(102)) # Should be sum of 1+2+3+6+17+34+51
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
  

#print(is_power_of_two(0)) # Should be False
#print(is_power_of_two(1)) # Should be True
#print(is_power_of_two(8)) # Should be True
#print(is_power_of_two(9)) # Should be False

# def skip_elements(elements):
# 	# Initialize variables
# 	new_list = []
# 	i = 0

# 	# Iterate through the list
# 	for x in elements:
# 		# Does this element belong in the resulting list?
# 		if i % 2 == 0:
# 			# Add this element to the resulting list
# 			new_list.append(x)
# 		# Increment i
# 		i += 1

# 	return new_list

def skip_elements(elements):
	return elements[::2]


#print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
#print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
#print(skip_elements([])) # Should be []


def file_size(file_info):
  file_name, file_type, file_size = file_info
  new_string = "{}.{}: {:.2f} kilobytes.".format(file_name, file_type, file_size/1024)
  return new_string
  

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

def skip_elements2(elements):
	return [x for i, x in enumerate(elements) if i % 2 == 0]

print(skip_elements2(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements2(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


def odd_numbers(n):
	return [x for x in range(1,n+1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for key_value in cool_beasts.items():
    print("{} have {}".format(*key_value))

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothes, colors in wardrobe.items():
	for color in colors:
		print("{} {}".format(color, clothes))