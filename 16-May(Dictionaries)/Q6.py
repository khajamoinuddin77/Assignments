dict = {
    "name": "Khaja",
    "age": 21,
    "salary": 25000,
    "city": "vijayawada"
}
# Keys to remove
keys = ["name", "salary"]

for k in keys:
    dict.pop(k)
print(dict)