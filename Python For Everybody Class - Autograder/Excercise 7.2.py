fname = input("Enter file name: ")
fh = open(fname)

x = 0
y = 0

for i in fh:
    if i.startswith("X-DSPAM-Confidence:"):
        x = x + 1
	if not i.startswith("X-DSPAM-Confidence:"):
		continue
        z = i.find("0")
        a = float(i[z:len(i)])
        y = float(y) + a
	b = y/x

c = round(b, 12)
print("Average spam confidence: {0}".format(c))