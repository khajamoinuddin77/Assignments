list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
new_list = ["h", "i", "j"]
list1[2][1][2].extend(new_list)
print(list1)
