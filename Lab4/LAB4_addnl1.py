import LAB4_addnl1mod

str1=input('enter string: ')
str1=str1.lower()
str2=LAB4_addnl1mod.rev(str1)

if(str1==str2):
    print("palindrome!")
else:
    print("not palindrone")
