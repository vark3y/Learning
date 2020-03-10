"""This script has a function that converts celsius into farenheit, and provides error messages if required"""
def cel_to_far(cel):
    """This function converts C to F degrees"""
    while cel != "100":
        cel = input("Enter degree of Celsius: " )
        try:
            if float(cel)<-273.15:
                print("Sorry, the lowest possible temperature that physical matter can reach is -273.15C")
            else:
                far = (float(cel)*9/5) + 32
                with open("temp.txt","a+") as file:
                    file.write("\n"+str(far))
                print (far, "degrees farenheit")
                #return (far)
        except ValueError:
            print("You've entered alphabets and/or special characters")


cel_to_far("")
#print (cel_to_far(cel), "degrees farenheit")

#temperatures=[10,-20,-289,100]
#for x in temperatures:
#    cel_to_far(x)
