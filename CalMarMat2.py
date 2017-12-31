"""

This py calculate Marcov matrix, from hiden to hiden.

Result is stored in a 4 * 4 * 4 numpy matrix.

"""


import pickle
import numpy


print("Calculating Marcov-transform matrix2...")
Count_Mat = numpy.zeros((4, 4, 4), dtype=numpy.int32)
Proba_Mat = numpy.zeros((4, 4, 4), dtype=numpy.float64)
Head_Mat = numpy.zeros(4, dtype=numpy.float64)

infile = open("AllChr.pkl", mode="rb")
list1 = pickle.load(infile)
infile.close()

for i in range(len(list1) - 2):
	Count_Mat[list1[i][0]][list1[i + 1][0]][list1[i + 2][0]] += 1

Sum_arr = numpy.zeros((4, 4), dtype=numpy.int32)
for i in range(4):
	for j in range(4):
		for k in range(4):
			Sum_arr[i][j] += Count_Mat[i][j][k]

for i in range(4):
	for j in range(4):
		if Sum_arr[i][j] == 0:
			for k in range(4):
				Proba_Mat[i][j][k] = 0
		else:
			for k in range(4):
				Proba_Mat[i][j][k] = Count_Mat[i][j][k] / Sum_arr[i][j]

print(Proba_Mat)

outfile = open("MarcovMat2.pkl", mode="wb")
pickle.dump(Proba_Mat, outfile)
outfile.close()

print("Finished.")
