"""
It is a program which gives funny name

"""





from random import shuffle # for shffling
from random import sample # sampling shuffle
def function_shuffling(ele): # this is a function which is used to shuflle with this is used for shuflling
    ele=list(ele) # store the valu of list in ele
    shuffle(ele) # shufle the list
    return ''.join(ele) # return and join


if __name__ == '__main__':

    name=int(input("Enter the how much names ou want"))
    list1=[]
    for i in range(name):
        n1=str(input("Enter the name"))
        list1.append(n1)
    print("original list",list1)

res=[function_shuffling(ele) for ele in list1] # for shuffling ele is use like i or j ot anyhthing we use here as element

print("SHuffled list is",res)

# second way

res1=[''.join(sample(ele1,len(ele1))) for ele1 in list1] # this is sample way

print("Second shffeld ",res1)