import os
with open('sample.txt','w')as file:
    file.write('This is sample file')

os.remove('sample.txt')
print("file 'sample.txt'deleted")

#os.unlike('sample.txt')
#print("file'sample.txt'deleted")