# assigment operators
country = 'Nigeria'
age = 64
print(country, "is", age, "years old.")

# using conditional statements
if age > 18:
    print("adult")
else: 
    print("minor")

# using a for loop
numbers = [1,3,2,5,7,9]
for number in numbers:
    print(number)

# using a function
# defining a function using the 'def' keyword
def isAdult(age):
    if age > 18:
        print("Adult")
    else:
        print("Minor")

# calling the function 'isAdult'
# and pass the 'age' variable to the 'isAdult' function
isAdult(age)
age = 5
isAdult(age)