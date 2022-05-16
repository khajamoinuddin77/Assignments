list1 = ["a", "b"]
list2 = ["c", "d"]

res = [x + y for x in list1 for y in list2]
print(res)