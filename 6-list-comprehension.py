a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
r,r2 = set(),set()

for i in a:
    if i % 2 == 0:
        r.add(i)

print(sorted(r))

r2 = [i for i in a if i %2 == 0]
print(sorted(r2))