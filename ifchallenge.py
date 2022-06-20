name = input("Please enter your name: ")
age = int(input("How old are you, {}? ".format(name)))

if(type(age == int)):
    if 18 <= age < 31:
        print("Welcone to the holiday, {}!".format(name))
    else:
        print("I'm sorry {}, your age is not within the required limits.".format(name))
else:
    print("I'm sorry, you need to provide a valid number.")