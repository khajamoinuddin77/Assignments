employees = ['khaja', 'nithin']
defaults = {"designation": 'intern', "salary": 25000}

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["khaja"])