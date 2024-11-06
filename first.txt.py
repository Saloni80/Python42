f1=open("first.txt","r")
print("File is read successfully")
with open("second.txt","w")as f:
    content=f1.read()
    print(content)
    for word in content.split():
       if word[0]=='a' or 'e' or 'i' or 'o' or 'u':
           f.write(word)
