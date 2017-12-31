"""

This py store a map into SglMap.pkl

The map is dictionary for index of list in SglDict.pkl

"""


import pickle


print("Some test are shown below...")
dict1 = {}
infile = open("SglDict.pkl", mode="rb")
list1 = pickle.load(infile)
infile.close()

for i in range(len(list1)):
	dict1[list1[i]] = i;

testlist = ["０", "１", "２", "３", "４", "５", "６", "７", "８", "９"]
for t in testlist:
	print(dict1[t], end=" ")
print()

testlist2 = ["ａ","ｂ","ｃ","ｄ","ｅ","ｆ","ｇ","ｈ",
	"ｉ", "ｊ", "ｋ","ｌ","ｍ","ｎ","ｏ","ｐ",
	"ｑ","ｒ","ｓ","ｔ","ｕ","ｖ","ｗ","ｘ",
	"ｙ","ｚ"]

for t in testlist2:
	print(dict1[t], end=" ")
print()

testlist3 = ["Ａ","Ｂ","Ｃ","Ｄ","Ｅ","Ｆ","Ｇ","Ｈ",
	"Ｉ","Ｊ","Ｋ","Ｌ","Ｍ","Ｎ","Ｏ", "Ｐ",
	"Ｑ","Ｒ","Ｓ","Ｔ","Ｕ","Ｖ","Ｗ","Ｘ",
	"Ｙ","Ｚ"]

for t in testlist3:
	print(dict1[t], end=" ")
print()

outfile = open("SglMap.pkl", mode="wb")
pickle.dump(dict1, outfile)
outfile.close()
print("Finished.")
