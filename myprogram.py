def age_in_weeks(age):
    new_age = int(age)*52
    print(new_age, "weeks")

age = int(input("Enter your age: "))

if age < 121:
    age_in_weeks(age)
else:
    #print ("You can't possibly be that old")
    truth = input("You can't possibly be that old. Is that true? yes or no? ")

    if truth == "yes":
        age_in_weeks(age)
    else:
        print("I knew it")


#age_in_weeks(age)
