''' Program:2
Write a python program to sort elements of a list in ascending and descending order by using bubble sort.
Write user defined function. '''

def BSort(Arr, S):

    for i in range(S -1):
        for j in range(S - i - 1):
            if(Arr[j] > Arr[j + 1]):
                 temp = Arr[j]
                 Arr[j] = Arr[j + 1]
                 Arr[j + 1] = temp

Arr = [ ]
S = int(input("Please Enter the Total Number of Elements : "))
for i in range(S):
    value = int(input("Please enter the %d Element of List1 : " %i))
    Arr.append(value)

BSort(Arr, S)
print("The Sorted List in Ascending Order : ", Arr)
print("The Sorted List in Descending Order : ", Arr[::-1])
