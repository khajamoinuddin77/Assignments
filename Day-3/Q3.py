st=input("enter a string")
def func(l):
    if l.islower():
        return ord(l) - 32
    elif l.isupper():
        return ord(l) + 32
    elif l.isdigit():
        if int(l) % 2 == 0:
            return ord(l) + 200
        else:
            return ord(l) + 100

print(*sorted(st, key=func), sep='')