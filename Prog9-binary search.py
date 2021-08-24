'''Program 9:
Write a python code using function to search an element in a list using Binary search method.

'''
def binary_search(list1, n):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:  
        # for get integer result   
        mid = (high + low) // 2  
  
        # Check if n is present at mid   
        if list1[mid] < n:  
            low = mid + 1
             # If n is greater, compare to the right of mid   
        elif list1[mid] > n:  
            high = mid - 1  
  
        # If n is smaller, compared to the left of mid  
        else:  
            return mid  
  
            # element was not present in the list, return -1  
    return -1  
  
  
# Initial list1
list1=[]
y=int(input('How many elements you want in list?:'))
for i in range(0,y):
    n1=int(input('Enter item in ascending/descending order in list:'))
    list1.append(n1)
x=(int(input('Enter item to search:')))
  
# Function call   
result = binary_search(list1, x)  
  
if result != -1:  
    print("Element is present at index", str(result),'and at position:',str(result+1))  
else:  
    print("Element is not present in list1")  
