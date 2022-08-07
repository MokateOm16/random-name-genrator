# Name    :- Om Mokate
# Program :- choice random  name in you entered  
#Date     :- 2 Aug 2022


# way 1 -->


import random 
friends_names = input("Enter names your friends with space \U0001F917 = ") # enter friends names
print(f"yours friends names is = {friends_names}")  #print name you enter like this

name = friends_names.split()     # enter name is seprated in list  formed
print(f"yours friends names in List  = {name}")   #print name seprated in list form       ex.  --->  ['om','rohan','saurbh','shweta','riya']

Random_name = (random.choice(name))     # converted list choice random name 
print(f"{Random_name} will pay hotel bill \U0001F600 !!!")  # print random name 


"""
# way 2 --> 

import random

list1 = ["om","shweta","rohan","saurabh","riya"]  # create
Random_name = random.choice(list1)  #choice random name in list
print(f"{Random_name} will pay hotel bill \U0001F600!!!")  # print this name
 """
