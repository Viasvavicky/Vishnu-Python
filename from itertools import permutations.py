from itertools import permutations
n = str(123)
for i in permutations(n):
    print(" ".join(i))  
