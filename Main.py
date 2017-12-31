import pickle
import numpy
import math
import sys
import re


def GoodLog(x):
	try:
		return math.log(x)
	except:
		return (0 - (sys.maxsize / 2))


def Load_Files():
	print("Loading...")
	infile1 = open("MarcovMat.pkl", mode="rb")
	h2h_mat = pickle.load(infile1)
	infile1.close()
	infile2 = open("SglMap.pkl", mode="rb")
	sgl_map = pickle.load(infile2)
	infile2.close()
	infile3 = open("hdCrfMat.pkl", mode="rb")
	hdcrf_mat = pickle.load(infile3)
	infile3.close()
	infile4 = open("hdMarcovMat.pkl", mode="rb")
	hd_label = pickle.load(infile4)
	infile4.close()
	infile5 = open("CrfMat.pkl", mode="rb")
	crf_mat = pickle.load(infile5)
	infile5.close()
	infile6 = open("MarcovMat2.pkl", mode="rb")
	hh2h_mat = pickle.load(infile6)
	infile6.close()
	return h2h_mat, sgl_map, hdcrf_mat, hd_label, crf_mat, hh2h_mat


def getInput():
	str1 = input("Input your text: ")
	return str1


def fillin_dp(dp, dp2, src_str, h2h_mat, sgl_map, hdcrf_mat, hd_label, crf_mat, hh2h_mat):
	for i in range(4):
		dp[i][0] += GoodLog(hd_label[i]) + GoodLog(hdcrf_mat[i][sgl_map[src_str[0]]])
	if len(src_str) == 1:
		return
	for j in range(4):
			index = 0
			max_val = (dp[0][0] + GoodLog(h2h_mat[0][j]) 
				+ GoodLog(crf_mat[0][j][sgl_map[src_str[0]]][sgl_map[src_str[1]]]))
			for k in range(1, 4):
				val = (dp[k][0] + GoodLog(h2h_mat[k][j]) 
					+ GoodLog(crf_mat[k][j][sgl_map[src_str[0]]][sgl_map[src_str[1]]]))
				if val > max_val:
					index = k
					max_val = val
			dp[j][1] = max_val
			dp2[j][1] = index
	if len(src_str) == 2:
		return
	for i in range(2, len(src_str)):
		for j in range(4):
			index = 0
			max_val = (dp[0][i - 1] + GoodLog(hh2h_mat[dp2[0][i - 1]][0][j]) 
				+ GoodLog(crf_mat[0][j][sgl_map[src_str[i - 1]]][sgl_map[src_str[i]]]))
			for k in range(1, 4):
				val = (dp[k][i - 1] + GoodLog(hh2h_mat[dp2[k][i - 1]][k][j]) 
					+ GoodLog(crf_mat[k][j][sgl_map[src_str[i - 1]]][sgl_map[src_str[i]]]))
				if val > max_val:
					index = k
					max_val = val
			dp[j][i] = max_val
			dp2[j][i] = index


def getLabelList(dp, dp2, lengt):
	index = 0
	max_val = dp[0][lengt]
	for i in range(1, 4):
		if dp[i][lengt] > max_val:
			index = i
			max_val = dp[i][lengt]
	res = []
	res.append(index)
	for i in range(lengt, 0, -1):
		index = dp2[index][i];
		res.append(index)
	return res[::-1]


def show_res(l, s):
	for i in range(len(s)):
		if l[i] == 0:
			print(s[i], end="")
		elif l[i] == 1:
			print(s[i], end="")
		elif l[i] == 2:
			print(s[i], end="/")
		else:
			print(s[i], end="/")
	print()


def Split(Text):
	l = re.split("[，。！？：；“”]", Text)
	res = []
	for m in l:
		if m != "":
			res.append(m + "。")
	return res


def main():
	h2h_mat, sgl_map, hdcrf_mat, hd_label, crf_mat, hh2h_mat = Load_Files()
	Text = getInput()
	while Text != "":
		str_lst = Split(Text)
		print("Result:")
		for src_str in str_lst:
			dp = numpy.zeros((4, len(src_str)), dtype=numpy.float64)
			dp2 = numpy.zeros((4, len(src_str)), dtype=numpy.int32)
			fillin_dp(dp, dp2, src_str, h2h_mat, sgl_map, hdcrf_mat, hd_label, crf_mat, hh2h_mat)
			res_lst = getLabelList(dp, dp2, len(src_str) - 1)
			show_res(res_lst, src_str)
		Text = getInput()


if __name__ == "__main__":
	main()
