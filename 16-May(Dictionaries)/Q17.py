
color_dict = {1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}
result = {}
for val in color_dict.values():
    result[val] = len(val)
print(result)

name_dict = {'1' : 'Austin Little', '2' : 'Natasha Howard', '3' : 'Alfred Mullins', '4' : 'Jamie Rowe'}
result = {}
for val in name_dict.values():
    result[val] = len(val)
print(result)