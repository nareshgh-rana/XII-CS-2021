'''Program 3:
Write a python program using function to pass list to a function and double the odd values and half even values of a list and display list element after changing.
for example
Entered elements are: [45, 12, 6, 31, 24]
Even lists: [6, 3, 12]
Odd lists: [2025, 961]
'''

def splitevenodd(A): 
   evenlist = [] 
   oddlist = [] 
   for i in A: 
      if (i % 2 == 0): 
         evenlist.append(i//2) 
      else: 
         oddlist.append(i*i) 
   print("Even lists:", evenlist) 
   print("Odd lists:", oddlist) 
  

A=list()
n=int(input("Enter the size of the  List ::"))
print("Enter the Elements of  List ::")
for i in range(int(n)):
   k=int(input("Enter element %d:=" %i))
   A.append(k)
print("Entered elements are:",A)
   
splitevenodd(A)
