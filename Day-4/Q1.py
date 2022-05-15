from calendar import month_name
month_lookup = list(month_name)
months = ['December', 'August', 'October', 'April', 'February', 'November', 'January', 'September', 'May', 'March', 'July', 'June']
months_sorted=sorted(months, key=month_lookup.index)
print(f"months in sorted order: {months_sorted}")