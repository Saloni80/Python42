with open('example.txt','r')as file:
    file.seek(5)
    content =file.read()
    print(content)