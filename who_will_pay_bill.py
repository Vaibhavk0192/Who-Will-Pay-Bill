import random

names = input("Give Everbody names seperated by comma \n")
names_list = names.split(", ")
result=random.choice(names_list)
print(result+" is going to pay bill!")
