'''Program 7:
Write a program to read a list of n integers (positive as well as negative). Create two new lists, one having all positive numbers with sum and the other having all negative numbers with sum from the given list. 
'''

list1=[]
postlist1=[]
neglist1=[]
sum=0
sum1=0
n=int(input('How many elements u want in list:'))
for i in range(1,n+1):
    a=int(input('Enter item %d in list:'%i))
    list1.append(a)
print('Original element of list is:',list1)
for i in range(0,n):
    if list1[i]<0:
        neglist1.append(list1[i])
        sum=sum+list1[i]
    else:
        postlist1.append(list1[i])
        sum1=sum1+list1[i]
print('Positive list of Element is:',postlist1)
print('sum of Positive(+ve) numbers:',sum1)
print('Negative list of element is:',neglist1)
print('sum of negative(-ve) numbers:',sum)
