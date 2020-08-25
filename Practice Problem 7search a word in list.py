"""
A program which search the word in list
"""

import re

str=str(input("Search the word "))
list=[""
    "rehman" ,"Rehman" "Ali Sagar","jutt","fasalabad","ali"
    "sheikh","chamn","jutt ali","jutt putt"
    "ra"
    ,"RA Jutt" , "khcuh b"
]



# there are two ways first list comprehenion

li=[i for i in list if str in i]

print("You search result is")
print(li)
print("time take in seconds")

# the second is regular exprssion

li1=[x for x in list if re.search(str,x)]


print("Second search result is")
print(li1,)

