x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))
if(x<=y && x<=z):
    print("X is smaller")
elif(y<=x && y<=z):
    print("Y is smaller")
else:
    print("Z is smaller")