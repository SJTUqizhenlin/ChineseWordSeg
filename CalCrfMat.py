"""

This py is used to calculate transform matrix, 
which is from previous status to out status

That means, from (hide, out_prev) --> out

"""


import pickle
import numpy
import sys


print("Calculating CRF matrix...")
infile1 = open("SglMap.pkl", mode="rb")
char_map = pickle.load(infile1)
infile1.close()

infile2 = open("AllChr.pkl", mode="rb")
all_char = pickle.load(infile2)
infile2.close()

Count_Mat = numpy.zeros((4, 4, len(char_map), len(char_map)), dtype=numpy.int32)
Proba_Mat = numpy.zeros((4, 4, len(char_map), len(char_map)), dtype=numpy.float64)
HeadC_Mat = numpy.zeros((4, len(char_map)), dtype=numpy.int32)
HeadP_Mat = numpy.zeros((4, len(char_map)), dtype=numpy.float64)

for i in range(1, len(all_char)):
	Count_Mat[all_char[i - 1][0]][all_char[i][0]][char_map[all_char[i - 1][1]]][char_map[all_char[i][1]]] += 1
	if all_char[i - 1][1] == (b"\xe3\x80\x82").decode("utf-8"):
		HeadC_Mat[all_char[i][0]][char_map[all_char[i][1]]] += 1


def cal_proba(c_mat, p_mat):
	sums = 0
	total = 1
	for k in range(len(c_mat)):
		sums += c_mat[k]
	if sums == 0:
		for k in range(len(c_mat)):
			p_mat[k] = 0
		return
	thr = sys.maxsize;
	for k in range(len(c_mat)):
		if c_mat[k] < thr:
			thr = c_mat[k]
	tmp_lst = []
	zero_lst = []
	for k in range(len(c_mat)):
		if c_mat[k] == thr:
			tmp_lst.append(k)
		if c_mat[k] == 0:
			zero_lst.append(k)
	for k in range(len(c_mat)):
		if c_mat[k] > thr:
			p_mat[k] = c_mat[k] / sums
			total -= p_mat[k]
	ratio = thr * 0.95
	for k in range(len(tmp_lst)):
		p_mat[tmp_lst[k]] = ratio / sums
		total -= p_mat[tmp_lst[k]]
	total = total / len(zero_lst)
	for k in range(len(zero_lst)):
		p_mat[zero_lst[k]] = total


for i in range(4):
	cal_proba(HeadC_Mat[i], HeadP_Mat[i])

for x in range(4):
	for y in range(4):
		for z in range(len(char_map)):
			cal_proba(Count_Mat[x][y][z], Proba_Mat[x][y][z])

outfile1 = open("hdCrfMat.pkl", mode="wb")
pickle.dump(HeadP_Mat, outfile1)
outfile1.close()

outfile2 = open("CrfMat.pkl", mode="wb")
pickle.dump(Proba_Mat, outfile2)
outfile2.close()
print("Finished.")
