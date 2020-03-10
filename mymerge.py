import datetime
import glob2

finalfile=[]
filenames=glob2.glob("*.txt")
for i in filenames:
    file=open(i)
    content=file.readline()
    file.close()
    finalfile.append(content)

filename=datetime.datetime.now()
with open(filename.strftime("%d-%B-%Y %I-%M %p")+".py",'w+') as file:
    for i in finalfile:
        file.write(i+"\n")

# for i in finalfile:
#     print(i)
