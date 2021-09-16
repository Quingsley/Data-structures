fname =input("enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    line.rstrip()
    x = line.split()
    for word in x:
        lst.append(word)
    y = []
    for i in lst:
        if i not in y:
            y.append(i)
    y.sort()


new_lst = y

print(new_lst)























