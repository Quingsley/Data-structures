fhand = open("romeo.txt")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, value in counts.items():
    new_tup = (value, key)
    lst.append(new_tup)

lst = sorted(lst, reverse=True)

for value, key in lst[:10]:
    print(key, value)