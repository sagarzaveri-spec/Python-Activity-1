'''
age=19
if age>=18:
    print("Driving License is acceptable")

password='coding'
if password=='coding':
    print("Successful login")
else:
    print("Access denied")
'''

'''
#Nested if else statement - when there are dependances
attendance_percenatge=int(input("Attenedance Percentage: "))
medical_report=input("Do you have a medical report? Type Y or N: ").upper()
if medical_report=='Y':
    print("You are eligibile to give the exam.")
else:
    if attendance_percenatge>=70:
        print("You are eleigible for the exam.")
    else:
        print("You are not elibgible for the exam.")
'''

'''
#Calculation of BMI (Weight / Height2)
weight=float(input("Weight in kg: "))
height=float(input("Height in meters: "))
BMI=weight/(height*height)
if BMI<18.5:
    print(f"Your BMI is {BMI}. You are underweight")
elif BMI>=18.5 and BMI <25:
    print(f"Yor BMI is {BMI}. You are healthy")
elif BMI>=25 and BMI <30:
    print(f"Yor BMI is {BMI}. You are overweight")
elif BMI>=30 and BMI <35:
    print(f"Yor BMI is {BMI}. You are obese-1")
elif BMI>=35 and BMI <40:
    print(f"Yor BMI is {BMI}. You are obese-2")
else:
    print(f"Yor BMI is {BMI}. You are obese-3")
'''

'''
CGPA=float(input("CGPA: "))

if CGPA==10:
    print("O Grade")
elif CGPA<10 and CGPA>=9:
    print("A+ Grade")
elif CGPA<9 and CGPA>=7.5:
    print("A Grade")
else:
    print("Practice more")
'''

'''
import random
OTP=random.randint(100000,999999)
print(f"Generated OPT is {OTP}")
user_value=int(input("Enter OTP: "))
if user_value==OTP:
    print("OTP Matched")
else:
    print("Wrong OTP")
'''

'''
import datetime
import calendar

current_time=datetime.datetime.now()
print("Time now at greenwich meridian is:",end="")
print(current_time)

print("\n",calendar.calendar(2026))
'''

#timedelta represents hours, minutes, and seconds - used for countdowns
from datetime import datetime, timedelta
import time
OTP_Time=datetime.now()
expiry_time=OTP_Time+timedelta(minutes=1)
print("OTP Generated. It will expire in 30 seconds...")
time.sleep(5) #it will wait 5 seconds to start the countdown
user_time=datetime.now()
if user_time<=expiry_time:
    remaining=expiry_time-user_time
    print("OTP remaining time is ",remaining)
else:
    print("OTP Expired")