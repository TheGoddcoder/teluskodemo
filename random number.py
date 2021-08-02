# import random as ra
# print(ra.randrange(1,25))

# s="my name is Bhoopendra Singh"
# print(len(s))

# Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# Sample String : google.com'
# from collections import Counter
s="google.com"
# d={}
# d=Counter(s)
# print(d)

# 2nd method


# dict={}
#
#
# for i in s:
#     # keys=dict.keys()
#     if i in s:
#         dict[i]=+1
#     else:
#         dict[i]=1
#
# print(dict)
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.
# s=str(input("enter the string"))
# y=""
# if len(s)<2:
#     print(y)
# else:
#     print(s[0:2]+""+s[-2:])
# print("w" in s)
# if "re" in s:
#     print("yes present")
# else:
#     print("not present")



# b="hello World"
# # print(b[-5:-2])
# # print(b.upper())
# # print(b.lower())
# # print(b.capitalize())
# print(b.replace("W","sameer's w"))
# name="bhoopendra Singh"
# age=26
# print(f"my name is {name} and i am {age} year old")



# n=str(5)
# n=int(n)
# nnn=str(5)+str(5)+str(5)
# nnn=int(nnn)
# nn=str(5)+str(5)
# nn=int(nn)
# print(nnn+nn+n)

# n1=(input("enter the number1"))
# n2=(input("enter the number2"))
# try:
#   print(int(n1+n2))
# except Exception as e:
#     print(e)
# print("this is very important")

# to reverse the string or any sequence

# s="1234abcd"
# print(s[::-1])

#  Write a Python program to read an entire text file


# f=open("demo.txt","wt")
# f.write("my name is sameer singh")
# f.close()
# f=open("demo.txt","rt")
#
# print(f.readlines())

# Write a Python program to read first n lines of a file
def file(n):
    # n=int(input("enter the number of lines to be printed"))
    f=open("demo.txt","rt")
    for i in range(n):
        print(f.readline())
file(1)















