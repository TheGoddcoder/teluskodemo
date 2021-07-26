# Write a Python program to get the Python version you are using
# import sys
# print(sys.version_info)
# print(sys.version)

# Write a Python program to display the current date and time
# import datetime
# import time
#
# print(datetime.datetime.now())
# print(time.ctime())

# Write a Python program which accepts the radius of a circle from the user and compute the area
import math

# r=float(input("enter the radius"))
# area=math.pi*r**2
# print(area)

# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

# 1st method
# f="suresh"
# l="singh"
# s=l+" " +f
# print(l,f)
# 2nd method
# y=s.split(" ")
# z=y[::-1]
# print(z)
# z=" ".join(z)
# print(z)

# n=(input("enter the numbers"))
# a=list(n)
# b=tuple(n)
# print(a)
# print(b)


# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
# a=int(input('enter the number'))
# n=int("%s" %a)
# nn=int("%s%s" %(a,a))
# nnn=int("%s%s%s" %(a,a,a))
# print(n+nn+nnn)


# Write a Python program to accept a filename from the user and print the extension of that

# fname=input("enter the name of the file")
# fname=fname.split(".")
# print(fname[-1])

# Write a Python program to display the first and last colors from the following list
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0] ,"and",color_list[-1])

# Write a Python program to print the calendar of a given month and year.
import calendar
print(calendar.month(194000,7))




