file = open("fruits.txt",'r')
#content = file.read()
content2 = file.readline()
for i in content2:
    print(len(i.strip()))
#print(content)
file.close()
