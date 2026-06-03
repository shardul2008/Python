''''import math
import random
import datetime
import calendar

print(math.sqrt(16))
print(math.ceil(12.455))
print(math.pow(5,3))
print(math.floor(23.546))
print(math.factorial(5))

print(random.randint(1000,9999))                           
cities =["Kolhapur","Pune","Mumbai","Nashik"]              
print("Random city:",random.choice(cities))                

print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.datetime.now().time())

print(calendar.month(2026,6)) '''

import os
''''print("",os.getcwd)
print("",os.listdir())
#print(os.mkdir("Shardul"))
print(os.rmdir("9am"))
#print(os.makedirs("intern/aidc/9am"))
os.rename("demo.html","new.html")'''
filelist = os.listdir()
for file in filelist:
    print(file)





