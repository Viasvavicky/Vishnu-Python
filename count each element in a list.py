def frag_count(array):
    n = {}
    for i in array:
        if i in n:
            n[i] += 1
        else:
            n[i] = 1
    return n
array = [1, 2, 3, 4, 1, 2, 1, 2, 1]
ans = frag_count(array)
print(ans)
