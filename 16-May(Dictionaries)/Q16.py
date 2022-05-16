def marksofsub(lst, marks):
    result = [d[marks] for d in lst if marks in d]

    return result

marks = [{'Math': 90, 'Science': 92},
         {'Math': 89, 'Science': 94},
         {'Math': 92, 'Science': 88}]

print(marks)
subj = "Science"
print(marksofsub(marks, subj))

