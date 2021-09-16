fname = input("Enter file name: ")
fh = open(fname)
counts = dict()


for x in fh:
    x.rstrip()
    if x.startswith("From") and not x.startswith("From:"):
        y = x.split()
        counts[y[1]] = counts.get(y[1], 0) + 1

    bigcount = None
    bigword = None
    for mail, count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = mail
            bigcount = count


print(bigword, bigcount)



