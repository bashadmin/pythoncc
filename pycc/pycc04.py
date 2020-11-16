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
	temp_groups = {}
	# Go through group_dictionary, not allowed to modify dict's while iterating.
	for users, groups in group_dictionary.items():
		#print(users,groups)
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