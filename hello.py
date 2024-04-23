def greetUser(fName, sName, gender):
    if gender == 'Male' or gender == 'male' or gender == 'M' or gender == 'm':
        print("Welcome {} of the house {}, the first of his name".format(fName, sName))
        print("We are happy to have you on board")
    elif gender == 'Female' or gender == 'female' or gender == 'F' or gender == 'f':
        print("Welcome {} of the house {}, the first of her name".format(fName, sName))
        print("We are happy to have you on board")
    elif gender == 'Shim' or gender == 'shim':
        return print("Please enter a valid gender. Don't be like Bobrisky")
    else:
        return print("Please enter a valid gender.")
    

print("Please enter your First Name")
firstName = input().title()
print("Please enter your Last Name")
lastName = input().title()
print("Please enter your gender (Male/Female)")
gender = input()

greetUser(firstName, lastName, gender)