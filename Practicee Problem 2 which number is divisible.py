"""
It is a program which tells that which number
is divisble of which number

"""
n=int(input("Enter the number of apples"))
mn=int(input("Enter the minimum number or start of number"))
mx=int(input("Enter the maximum number or ends of number"))
if mn==mx:
    print("You enter the mn and mx equal")

elif n%2==0:
    for i in range(mn, mx+1):
        if n % i == 0:
            print(i, f"is divisible of {n}")
elif n%2!=0:
    for i in range(mn,mx+1):
        if n % i ==0:
            print(i, f"is divisible of {n}")
