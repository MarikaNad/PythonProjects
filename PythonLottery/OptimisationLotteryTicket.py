import random

rand_lottery_list = []
n = 7

for number in range(n):
    rand_lottery_list.append(random.randint(1,11))

# lottery_list = [17, 66, 77, 54, 67, 74, 6]

lottery_lst_entered = []

print('Please enter 7 numbers: ')
while len(lottery_lst_entered) < 7:
    c = int(input())
    if 0 < c and c < 11:
        lottery_lst_entered.append(c)
    else:
        print("Number should be between 1 and 10 inclusively")


number_of_matches = 0

for number in rand_lottery_list:

    for number1 in lottery_lst_entered:
        if number == number1:
            number_of_matches = number_of_matches + 1


rewards = {3: "£20.0", 4: "£40", 5: "£100", 6: "£10000", 7: "£1000000"}

if number_of_matches in rewards:
    the_reward = rewards[number_of_matches]
    print('Congratulation, your ticket has {} matching numbers and you won {}!'.format(number_of_matches, the_reward))
else:
    print('Sorry , no luck this time')
