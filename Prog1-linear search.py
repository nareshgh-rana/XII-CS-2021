'''Practical 1:
Write a python program to search first occurrence of an element in a list by using Linear search and display frequency of each element present in list [List and search element should be entered by user]
'''
L=[]
c=0
n=int(input('How many items you want to enter in list?:'))
for i in range(1,n+1):
    a=int(input('Enter item %d:'%i))
    L.append(a)
print(L)
S=set(L) 
S=list(S) 
D={} 
for i in S:
    c=0 
    for j in L: 
        if i==j: 
            c+=1 
    D[i]=c 
for k in D: 
    print("The frequency of ",k," is ", D[k])

ele=int(input("Enter item to be search:"))
flag=0
for i in range(0, n):
    if (ele==L[i]):
        flag=1
        break
if (flag==1):
    print("Element found at index",i,"and position",i+1)  
else:
    print("Element not found")

