#init
#functions
def headlineShrek():
    a = input("please enter a charchter from shrek:")
    return("is "+ a +" coming for your job?")
def headlineProblems():
    b = input("please enter a fruit or vegatable, plural:")
    c = input("enter a country:")
    d = input("name a life problem:")
    return("do " + b +" from " + c + " lead to " + d + "?")
def headlinePeople():
    e = input("enter a number between 1-8")
    f = input("type young or old")
    return ("is " + e + " " + f + " people in a room together a curse?")
def headlineCars():
    g = input("name a car brand:")
    h = input("name a small town")
    i = input("name a illness:")
    return("do " + g + " in " + h + " cause indigestion in people suffering from a " + i + "?")
def headlineDebate():
    j = input("name a current presidential candidate:")
    k = input("name a different presidential candidate:")
    l = input("name a sport:")
    m = input("name a month of the year:")
    return("did " + j + " challenge " + k + " to a " + l + " match in " + m + "?")
def headlineGenerator():
    while True:
        print("have your heard these headlines")
        print(" select an option \n1. shrek \n2. problems \n3. people \n4. cars \n5. debate \n6. quit")
        selection = int(input("option:"))
        if selection == 1:
            print(headlineShrek())
        elif selection == 2:
            print(headlineProblems())
        elif selection == 3:
            print(headlinePeople())
        elif selection == 4:
            print(headlineCars())
        elif selection == 5:
            print(headlineDebate())
        elif selection == 6:
            break
headlineGenerator()
