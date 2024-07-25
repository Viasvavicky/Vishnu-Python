first={1,2,3,4,5,6}
second={4,5,6,7,8,9}
inter=first.intersection(second)
print(inter)
for i in inter:
    first.remove(i)
print(first)
