'''Program 10:
Write a menu driven program to generate random numbers given in specific range and to display calendar after giving month and year.
MENU
1. Generate Random numbers
2. Calender of a month
3.Exit
'''
# Program to display calendar of the given month and year

import random
import calendar
while True:
    print("******MENU*******\n")
    print('1:Random Number generators')
    print('2:Calender of a month')
    print('3:Exit\n')
    ch=int(input('Enter your choice:'))
    if ch==1:
        num = int(input("How many Number?:"))
        start = int(input("stat Number:"))
        end = int(input("stat End number:"))
        res = []
        for j in range(num):
            res.append(random.randint(start, end))
        print(res)
    if ch==2:
        yy = int(input("Enter year: "))
        mm = int(input("Enter month: "))
        print(calendar.month(yy, mm))
    if ch==3:
        break
