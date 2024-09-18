print("\t bill calculator \n ")

pre = int(input("Enter previous reading :- "))
cur = int(input("Enter current reading :- "))

unit = (cur-pre)
total = 0

if unit>=500:
   total = (unit*50) + 1500

elif unit>=400:
   total = (unit*50) + 1000

elif unit>=300:
   total = (unit*50) + 750

elif unit>=200:
   total = (unit*50) + 500

elif unit>=100:
   total = (unit*50) + 250
   
elif unit>=60:
   total = (unit*50) + 100

else:
   total = (unit*50) + 50

print("monthly fee :- ",total)