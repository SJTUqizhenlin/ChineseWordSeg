"""

Running it is just a test for Chinese character in python3

"""


print("你好")
s = input("Input: ")
print(s)
byte = s.encode("utf-8")
print(byte)
print(len(byte))
ss = byte.decode("utf-8")
print(ss)
print(len(ss))


"""

Every time you update msr.txt, or change new corpus,

Please run py files as:

1. ReadnStore.py
2. SetUpDict.py
3. SetUpMap.py
4. CalMarMat.py
5. CalMarMat2.py
6. CalCrfMat.py
7. Main.py

"""
