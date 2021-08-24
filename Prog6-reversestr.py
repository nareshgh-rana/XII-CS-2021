'''Program 6: 
Write a menu driven program in python to do following
MENU
1.	Reverse String
2.	Check Whether string is Palindrome
3.	Make half string in Uppercase
4.	Exit
'''

while True:
    print("******MENU*******")
    print('1:Reverse String')
    print('2:Check whether string is palindrome')
    print('3:Make half string in Uppercase')
    print('4:Exit\n')
    ch=int(input('Enter your choice:'))
    if ch==1:
        st = input('Enter String:')
        print(st[::-1])
    if ch==2:
        st = input('Enter String:')
        if st==st[::-1]:
            print('This string is palindrome')
        else:
            print('String is not palindrome')
    if ch==3:
        st = input('Enter String:')
        print("The original string is : " + str(st))
        # computing half index
        hlf_idx = len(st) // 2
        res = ''
        for idx in range(len(st)):
        # uppercasing later half
            if idx >= hlf_idx:
              res += st[idx].upper()
            else :
              res += st[idx]
          # printing result 
        print("The resultant string : " + str(res))
    if ch==4:
        break
