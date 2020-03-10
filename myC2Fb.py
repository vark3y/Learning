temperatures=[10,-20,-289,100]
def c_to_f(c):
    with open("temp.txt","a+") as file:
        if c >= -273.5:
            f=c*9/5+32
            file.seek(0)
            file.write(str(f)+"\n")
for t in temperatures:
    c_to_f(t)

#or
#temperatures=[10,-20,-289,100]
#def writer(temperatures, filepath):
#     with open(filepath, 'w') as file:
#         for c in temperatures:
#             if c>-273.15:
#                 f=c*9/5+32
#                 file.write(str(f)+"\n")
#
# writer(temperatures, "temps.txt")

# or
# temperatures=[10,-20,-289,100]
#
# def writer(temperatures):
#     with open("temps.txt", 'w') as file:
#         for c in temperatures:
#             if c>-273.15:
#                 f=c*9/5+32
#                 file.write(str(f)+"\n")
#
# writer(temperatures)
