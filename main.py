#REMEMBER TO CHANGE YOUR FILEPATH AND ADD A FOLDER... 
#IN THIS CASE THE FOLDER IS CALLED "db"

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%c")

name = str(input("What's your name? "))
surname = str(input("What's your surname? "))
age = int(input("What's your age? "))
weight = float(input("What's your weight? "))
weightu = str(input("Kg's(K) or Lb's?(L) "))

if weightu == "L":
    weight = weight * 0.45
elif weightu == "K":
    weight = weight / 0.45

result = ("Your name: " + name, "Your Surname: " + surname, "Your Age: " + str(age), "Your weight " + str(weight))
result = str(result)
print (result)


with open('db/db.txt', 'at') as f:
    f.write('\nDB started | ')
    f.write(str(current_time))
    f.write ("\n" + "\n")
f = open("db/db.txt", "at") #CHANGE THIS
f.write(result)
f.close
f = open("db/db.txt") #CHANGE THIS
print(str(f))
