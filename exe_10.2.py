fh = open("mbox-short.txt")
counts = dict()


for x in fh:
    if x.startswith("From") and not x.startswith("From:"):
        y = x.split()
        lst = y[5].split(":")
        counts[lst[0]] = counts.get(lst[0], 0) + 1


flst = list()
for key, value in counts.items():
    new_tup = (key, value)
    flst.append(new_tup)


flst.sort()
for key , value in flst:
    print(key, value)


