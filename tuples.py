x = ("Glenn", "Sally", "Joseph")
print(x[2])
y = (1, 9, 2)
print(y)
print(max(y))
for iter in y:
    print(iter)


(x, y) = (3, 6)
print(y)
(z, v) = ("fred", "cosmic")
print(v)

d = dict()
d["cven"] = 2
d["kreok"] = 8
for a, b in d.items():
    print(a, b)


tups = d.items()
print(tups)

# sorted using key
g = {"a":10, "b":1, "c":22}
g.items()
print(g.items())
sorted((g.items()))
print(sorted(g.items()))
for k, v in sorted(g.items()):
    print(k, v)


# sorted using value
f = {"a":10, "b":1, "c":22}
tmp = list()
for k, v in f.items():
    tmp.append((v, k))

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)