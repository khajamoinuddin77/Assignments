lst1 = ["apple", "banana", "coconut","dragon fruit"]
lst2 = [1, 2, 3, 4, 5]

res = {}
for key in lst2:
	for value in lst1:
		res[key] = value
		lst1.remove(value)
		break

# Printing resultant dictionary
print ("Resultant dictionary is : " + str(res))
