"""
It is a problem in which we get the age or birth year from user
and tell them when they become 100 years old and also an option at
the in which year become in years old

"""

age1=int(input("Enter Your Age or Birth year"))
if age1>1900 and age1<2020:
    print("You enterd your birth year")
    if age1>2000:
        age=2100-age1
        print(f"You become 100 years old at {age}")
    else:
        age=2000-age1
        print(f"You will become 100 years in {age} years ")

elif age1>1 and age1<120:
    print("You Enterd your age")
    if age1>100:
        print("You are much old")
    elif age1<100:
        age=100-age1
        print(f"You Become 100 years old in {age} years")
if age1>=2020:
    print("You Are not born Yet")
elif age1 > 150  and age1<=1900:
    print("You or not alive")

print("Press c to get your age in particular year")
particle=input()
if particle == "c":
    print("Enter the year which you want to know about ")
    year=int(input())
    if year > 1900 and year < 2100:
        year=year-age1
        print(f"Your age   will be {year}  ")
    else:
        print("You enterd wrong age")
else:
    print(" i exit the program")
    exit()

