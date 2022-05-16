dict1 = {
    "name": "Khaja",
    "age": 21,
    "salary": 25000,
    "city": "Vijayawada"}

# keys to extract
keys = ["name", "salary"]
res = dict()

for k in keys:
    res.update({k: dict1[k]})
print(res)
