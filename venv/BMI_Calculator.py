
####Wish/ Greet the user based on time
def wishUser(name):
    from datetime import datetime
    ts = datetime.now()
    hr = float(ts.strftime("%H.%M"))
#    print(f'hour is {hr}')
    if hr >= 0 and hr < 12:
        return (f"Good Morning {uName}")
        #print (f"Good Morning {uName}")
    elif hr >= 12 and hr < 16:
        return (f"Good Afternoon {uName}")
        #print (f"Good Afternoon {uName}")
    elif hr > 16 and hr < 19:
        return (f"Good Evening {uName}")
        #print  (f"Good Evening {uName}")

    else:
        return (f"Good Night {uName}")
        #print (f"Good Night {uName}")

def BMI_FM(Height, Weight):
    bmi_val= ((Weight)/(Height*Height))
    print(f"Your BMI is : {bmi_val} --Female")
    if bmi_val < 18.5:
        return (f"{format(round(Height,2), '.2f')}    |   {format(round(Weight,2), '.2f')}   |         {format(round(bmi_val,2), '.2f')}          |    Underweight")
    elif bmi_val >= 18.5 and bmi_val < 25:
        return (f"{format(round(Height,2), '.2f')}    |   {format(round(Weight,2), '.2f')}   |         {format(round(bmi_val,2), '.2f')}          |    NormalWeight")
    elif bmi_val >=25 and bmi_val < 30:
        return (f"{format(round(Height,2), '.2f')}    |   {format(round(Weight,2), '.2f')}   |         {format(round(bmi_val,2), '.2f')}          |    Overweight")
    elif bmi_val > 30:
        return (f"{format(round(Height,2), '.2f')}    |   {format(round(Weight,2), '.2f')}   |         {format(round(bmi_val,2), '.2f')}          |    Obese")

def BMI_M(Height, Weight):
    bmi_val= ((Weight)/(Height*Height))
    print(f"Your BMI is : {bmi_val} -- Male")
    if bmi_val < 18.4:
        return (f"{format(round(Height,2), '.2f')}    |   {format(round(Weight,2), '.2f')}   |         {format(round(bmi_val,2), '.2f')}          |    Malnutrition risk")
    elif bmi_val >= 18.5 and bmi_val < 25:
        return (f"{format(round(Height,2), '.2f')}    |   {format(round(Weight,2), '.2f')}   |         {format(round(bmi_val,2), '.2f')}          |    NormalWeight ---- Low risk")
    elif bmi_val >=25 and bmi_val < 30:
        return (f"{format(round(Height,2), '.2f')}    |   {format(round(Weight,2), '.2f')}   |         {format(round(bmi_val, 2), '.2f')}          |    Overweight ---- Enchanced risk")
    elif bmi_val > 30:
        return (f"{format(round(Height,2), '.2f')}    |   {format(round(Weight,2), '.2f')}   |         {format(round(bmi_val,2), '.2f')}          |    Obese ---- High Risk")


print(f'Please enter your Details....')
uName = input("Enter your name")
uGender = input("Enter your Gender M (or) F").lstrip()[0]
uHeight = float(input("Enter Height in Meters"))
uWeight = float(input("Enter Weight in Kilograms"))

#print(wishUser(uName))
print(wishUser(uName))

def dec():
    if uGender=="M" or uGender=="m":
        return(BMI_M(uHeight, uWeight))
    elif uGender=="F" or uGender=="f":
        return(BMI_FM(uHeight, uWeight))

res = dec()


####APPENDING TO A FILE
import os

from datetime import datetime

now = datetime.now() # current date and time
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
time = now.strftime("%H:%M:%S")
print(f"year      month     day       time")
print(f"{year}      {month}     {day}       {time}")
f = open("C:/Users/venka/PycharmProjects/pythonProject/venv/Input/weightLogInPython.txt", "a")
f.write(f"\n{year}  |   {month}   |   {day}   |   {time}  |  {uGender}    |   {res}")

print(f"GBM.... Added printFToConfirmCommit in NewBranch branch")