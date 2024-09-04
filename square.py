import random
str=input("Enter name:")
print(str)
#num=int(input("Enter the number :"))
#if  num<=100:
num=random.randint(1,100)
print("What is square of",num)
square=num*num
ans=int(input("Put your ans: "))
if ans==square:
    print("correct answer")
else:
    print("Wrong answer")

