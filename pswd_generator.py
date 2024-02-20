import random
import string

len=int(input("Enter the length of the password to be created : "))
char=""
print("""Enter the number to choose the character set for password \n
      1.Uppercase\n
      2.Lowercase\n
      3.Digits\n
      4.Special characters\n
      5.Exit\n""")
while(True):
    ch=int(input("Enter the choice : "))
    if (ch==1):
        char+=string.ascii_uppercase
    elif (ch==2):
        char+=string.ascii_lowercase 
    elif (ch==3):
        char+=string.digits
    elif (ch==4):
        char+=string.punctuation
    elif (ch==5):
        break     
    else:
        print("please pick valid option!")  

pwsd=[]
for i in range(len):
    random_char =random.choice(char)
    pwsd.append(random_char)
print("The random password is "+ "".join(pwsd))                