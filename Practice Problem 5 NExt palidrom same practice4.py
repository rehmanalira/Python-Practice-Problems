"""
It is program whcih checks number is palidrunn self but number should be > 10
palidrum which we write opposit or any time it will be the write

"""
def paliderem(num): # function which checks the number palidr
    if num >10:
        num=num +1  # add 1 to given input and then go to functio is_palidrum
        while not is_paledrm(num):
            num=num+1
        return num
    else:
        return number_li[i]

def is_paledrm(num): # here it checks the number if it is return the value if not the go to statment of whille not

    return str(num) == str(num)[::-1]

if __name__ == '__main__':

    num=int(input("Enter THe numbers"))
    number_li=[] # to store the value

    for i in range(num):
        a=int(input(f"Enter the {i} number:"))
        number_li.append(a)
    print(number_li)
    for i in range(num):
        print(f" the number {number_li[i]} has next paledrum {paliderem(number_li[i])} ")

