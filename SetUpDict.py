"""

This py is used to count all the Chinese character. 
But it is impossible to get "ALL", so I just use 
msr.txt as sample 
(hope it is not too incomplete :D)

"""


import pickle


print("Finding all character and setup dictionary...")
set1 = set()
list1 = []
infile = open("msr.txt", mode="r")

line = infile.readline()
while line:
	for ch in line:
		if (ch == " ") or (ch == "\n"):
			continue
		else:
			if not (ch in set1):
				set1.add(ch)
				list1.append(ch)
	line = infile.readline()

infile.close()

outfile = open("SglDict.pkl", mode="wb")
pickle.dump(list1, outfile)
outfile.close()
print("Finished.")
