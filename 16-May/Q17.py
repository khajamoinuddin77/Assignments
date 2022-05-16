lst = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

previous_value = None
new_lst = []

for elem in lst:
   if elem != previous_value:
       new_lst.append(elem)
       previous_value = elem

print(f"the new lst: {new_lst}")
