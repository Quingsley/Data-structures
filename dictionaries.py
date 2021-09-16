purse = dict()
purse["money"] = 12
purse["candy"] = 3
purse["tissue"] = 75
print(purse)
print(purse["candy"])
purse["candy"] = purse["candy"] + 2
print(purse)

ddd = dict()
ddd["age"] = 23
ddd ["course"] = "compscience"
print(ddd)
ddd["age"] =25
ddd["course"] = "evh"
print(ddd)

counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1


print(counts)
print(counts.get("wan", 0))

counts = dict()
y = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in y:
    if name in y:
        counts[name] = counts.get(name, 0) + 1


print(counts)
print(counts.keys())
print(counts.values())
print(counts.items())


greez = {"chuck" : 1, "fred" : 42, "jan" : 100}
for key in greez:
    print(key,greez[key])


for keyy, value in greez.items():
    print(keyy, value)






