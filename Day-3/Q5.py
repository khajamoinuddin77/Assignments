res = []
given_str=input("enter string")
temp = given_str.split()
for idx in temp:
    if any(chr.isalpha() for chr in idx) and any(chr.isdigit() for chr in idx):
        res.append(idx)

# printing result
print("Words with alphabets and numbers : " + str(res))