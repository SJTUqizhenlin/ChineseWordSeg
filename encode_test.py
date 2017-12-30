"""

This is just a test for Chinese character 
in python3

Wow, what a nice experience

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
