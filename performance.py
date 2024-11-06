a=int(input("Enter marks of maths:"))
b=int(input("Enter marks of physics:"))
c=int(input("Enter marks of chemistry:"))
Total=a+b+c
avg=Total/3
if avg>=90:
    print("Excellent performance")
elif avg>=80:
    print("Very good performance")
elif avg>=70:
    print("Good performance")
elif avg>=60:
    print("Average performance")
else:
    print("Poor performance")
