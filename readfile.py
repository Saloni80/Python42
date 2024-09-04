with open('example.txt','r')as file:
    content=file.read()
    print('Read entire file')
    print(content)

#another method
with open('example.txt','r')as file:
    line=file.readline()
    print('Read entire file')
    print(line)
