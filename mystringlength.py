def str_lenth(string):
    try:
        float(string)
        print("Sorry, integers don't have length")
    except ValueError:
        print (len(string), "characters")
        #return len(string)

string = input("Enter any string: ")
str_lenth(string)
#print (type(string))
