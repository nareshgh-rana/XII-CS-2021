'''Program 8:
Write a Python program to remove duplicates element from a list.
'''
a=[]
n=int(input('How many elements you want in list:'))
for i in range(1,n+1):
    n1=int(input('Enter item %d in list:'%i))
    a.append(n1)
print('Original list is:',a)
print('List after removing duplicate elements:')
dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x) 
        dup_items.add(x)
print(dup_items)

