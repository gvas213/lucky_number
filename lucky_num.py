import random

comp_numbers = []
user_list = []
comp_list = []
match_list = []

while len(user_list) <=4:
    user_num = input("enter a number 1-70")
    user_list.append(user_num)

for x in range (1, 6):
    comp_num = str(random.randint(1, 70))
    comp_list.append(comp_num)

for i in comp_list:
    for j in user_list:
        if i in j:
            match_list.append(j)

print(match_list)
correct = (len(match_list))
comp_list = ', '.join(comp_list)
user_list = ', '.join(user_list)

print(f"the numbers you chose were {user_list}")
print(f"the numbers you chose were {comp_list}")
print(f"you guessed {correct} correct")

if correct == 1:
    points = "1"
elif correct == 2:
    points = "4"






    