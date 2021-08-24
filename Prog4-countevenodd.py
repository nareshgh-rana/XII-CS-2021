''' Program 4:
Write a Python program input n numbers in tuple and count how many even and odd numbers are entered.
'''

l=[]

S = int(input("Please Enter the Total Number of Elements : "))
for i in range(S):
    value = int(input("Please enter the %d Element of List1 : " %i))
    l.append(value)
numbers=tuple(l)
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :", count_odd)
