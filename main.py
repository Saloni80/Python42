from mypackage import module1,module2
print(module1.func1())
print(module2.func2())

# 2nd 
print("2nd method :")
import mypackage
print(mypackage.module1.func1())
print(module2.func2())

#3rd
print("3rd method")
from mypackage.module1 import func1
from mypackage.module2 import func2
print(func1())
print(func2())