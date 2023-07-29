#Typing speed test

from time import *
import random as r


def mistakes(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error


def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_roundoff = round(time_delay,2)
    speed = len(userinput) / time_roundoff
    return round(speed)


test = ["Web designers are expected to have an awareness of usability and if their role involves creating mark up then they are also expected to be up to date with web accessibility guidelines.","The different areas of web design include web graphic design; interface design; authoring, including standardised code and proprietary software; user experience design; and search engine optimization."]
test1 = r.choice(test)
print("***** Typing Speed *****")
print(test1)
print()
print()
time_1 = time()
testinput = input("Enter: ")
time_2 = time()

print("Speed :",speed_time(time_1,time_2,testinput), "Word per second")
print("Error :",mistakes(test1,testinput))
