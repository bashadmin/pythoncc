import psutil

def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    print("DEBUG: CPU usage: {}".format(usage))
    return usage < percent

if not check_cpu_usage(75):
    print("ERROR! CPU is overloaded!!!")
else:
    print("Everything is ok.")

# The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups.
# Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.

def groups_per_user(group_dictionary):
	user_groups = {}
	#temp_groups = {}
	# Go through group_dictionary, not allowed to modify dict's while iterating.
	for users, groups in group_dictionary.items():
		print(users,groups)
		# Now go through the users in the group
		for user in groups:
			#print(user)
			user_groups[user] = [key for key in group_dictionary if user in group_dictionary[key] ]
# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  return guests2.update(guests1)

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))
