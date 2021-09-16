fname = input("Enter file name: ")
fh = open(fname)
count = 0


for x in fh:
    if x.startswith("From") and not x.startswith("From:"):
        y = x.split()
        print(y[1])
        count += 1

print(f"There were {count} lines in the file with From as the first word ")


