"""

It is a program which revers the given list
-->1 with built function reverse()
-->2 string slicing
-->3 swap the 1 and last and the 2nd 2nd last and up to soon

"""
num=int(input("Enter the number of which you want to input"))
list=[]
for i in range(1, num+1): # for getting list nunmber from users
    print("Enter Number",i)
    n=int(input())
    list.append(n)
print(list)
r=list[:]  # here i store the copy of list here if i not store then it will not reverse the list
r.reverse()
print(f"reversed first list is {r}")

print(f"the second reverse list {list[::-1]}") # it is used to reverse see in string slicing

r1=list[:]

for i in range(len(list)//2): # here is used // it run the loop half if we not give this it will not reverse our list
                            #beacuse it will re arrange the list as it was input
    r1[i], r1[len(list) - i -1] = r1[len(list) - i -1] ,r1[i]
        # it will changge from 1st indx and the last index -i and - 1
print(f"third list is {r1}")



