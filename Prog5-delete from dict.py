'''Practical 5:
Write a menu driven program in python to delete name of a student from dictionary and to search phone no of a student by student name. Create menu as below:
MENU
1. Delete from Dictionary
2. Search Phone number using name from Dictionary
3. Exit'''


phonebook=dict()
while True:
    print("_"*50)
    print("******MENU\*******")
    print("_"*50)
    print('1:Delete from Dictionary')
    print('2:Search Phone number using name from Dictionary')
    print('3:Exit\n')
    print("_"*50)
    ch=int(input('Enter your choice:'))
    if ch==1:
        n=int(input("Enter total number of friends:"))
        i=1
        while(i<=n):
            a=input("enter name :")
            b=int(input("enter phone number:"))
            phonebook[a]=b
            i=i+1
            print(phonebook)
            print('-'*50)
        name=input("Enter name to delete:")
        del phonebook[name]
        k=phonebook.keys()
        print("Phonebook Information")
        print(print('-'*50))
        print("Name",'\t',"Phone number")
        print('-'*50)
        for i in k:
            print(i,'\t',phonebook[i])
            print('-'*50)
    if ch==2:
        name=input("Enter name to search:")
        f=0
        k=phonebook.keys()
        for i in k:
            if(i==name):
                print("Phone number= ",phonebook[i])
                print('-'*50)
                f=1
        if (f==0):
            print("Entered  name  doe not exist in the dictionary,Try again")
    if ch==3:
            break
