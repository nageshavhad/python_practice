sub = ["python","python","c++","java","java","c","javascript"]
d = {}

for s in sub:
    if s in d:
        d[s] = d[s]+1
    else:
        d[s] = 1

print(d)
a =[]
for s in d.keys():
    if d[s]>1:
        a.append(s)
    print(s)
print(a)