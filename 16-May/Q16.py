# i used iteration-utilities package to flatten the nested list
# pip install iteration-utilities --- to install iteration utilities
from iteration_utilities import deepflatten

l = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

ans = list(deepflatten(l))
print(ans)
