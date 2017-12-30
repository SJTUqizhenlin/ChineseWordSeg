"""

This py read msr.txt and store all the chars 
with their labels 

B:0 
M:1 
E:2 
S:3

Outfile is AllChr.pkl

"""

import pickle


list1 = []
infile = open("msr.txt", mode="r")

line = infile.readline()

while line:
	if line[-1] == "\n":
		line = line[:-1]
	if len(line) == 1:
		if line[0] != " ":
			list1.append((3, line[0]))
		line = infile.readline()
		continue
	for i in range(len(line)):
		if line[i] == " ":
			continue
		else:
			if i == 0:
				if line[i + 1] == " ":
					list1.append((3, line[i]))
				else:
					list1.append((0, line[i]))
			elif i == len(line) - 1:
				if line[i - 1] == " ":
					list1.append((3, line[i]))
				else:
					list1.append((2, line[i]))
			else:
				if (line[i - 1] == " ") and (line[i + 1] == " "):
					list1.append((3, line[i]))
				elif (line[i - 1] == " ") and (line[i + 1] != " "):
					list1.append((0, line[i]))
				elif (line[i - 1] != " ") and (line[i + 1] == " "):
					list1.append((2, line[i]))
				else:
					list1.append((1, line[i]))
	line = infile.readline()

infile.close()

outfile = open("AllChr.pkl", mode="wb")
pickle.dump(list1, outfile)
outfile.close()
