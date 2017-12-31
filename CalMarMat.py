"""

This py calculate Marcov matrix, from hiden to hiden.

Result is stored in a 4 * 4 numpy matrix.

"""


import pickle
import numpy


print("Calculating Marcov-transform matrix...")
Count_Mat = numpy.zeros((4, 4), dtype=numpy.int32)
Proba_Mat = numpy.zeros((4, 4), dtype=numpy.float64)
Head_Mat = numpy.zeros(4, dtype=numpy.float64)

infile = open("AllChr.pkl", mode="rb")
list1 = pickle.load(infile)
infile.close()

for i in range(len(list1) - 1):
	Count_Mat[list1[i][0]][list1[i + 1][0]] += 1
	if (list1[i][1] == (b"\xe3\x80\x82").decode("utf-8")):
		Head_Mat[list1[i + 1][0]] += 1

Sum_arr = numpy.zeros(4, dtype=numpy.int32)
for i in range(4):
	for j in range(4):
		Sum_arr[i] += Count_Mat[i][j]

for i in range(4):
	for j in range(4):
		Proba_Mat[i][j] = Count_Mat[i][j] / Sum_arr[i]

Head_sum = 0
for nums in Head_Mat:
	Head_sum += nums

for i in range(4):
	Head_Mat[i] = Head_Mat[i] / Head_sum

print(Proba_Mat)

outfile = open("MarcovMat.pkl", mode="wb")
pickle.dump(Proba_Mat, outfile)
outfile.close()

outfile = open("hdMarcovMat.pkl", mode="wb")
pickle.dump(Head_Mat, outfile)
outfile.close()
print("Finished.")
