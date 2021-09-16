fname = input("Enter file name: ")
fh = open(fname,'r')
count = 0
totalconfidence = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    index_space = line.find(" ")
    num = float(line[index_space + 1:])
    totalconfidence += num
    count+=1
print("Average spam confidence is: ", totalconfidence/count)



















