a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = set()
result2 = set()
for i in a:
    for j in b:
        if i == j:
            result2.add(i)
for i in a:
    if i in b:
        result.add(i)

print(result)
print(result2)

r = [i for i in a if i in b]
print(set(r))
