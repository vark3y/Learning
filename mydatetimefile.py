import datetime
"""f"""
filename=datetime.datetime.now()

def create_file():
    with open(filename.strftime("%d-%B-%Y %I-%M %p")+".py",'w+') as file:
        file.write('')
create_file()
