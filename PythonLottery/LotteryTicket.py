
import random

rand_lottery_list = []
n = 7

for number in range(n):
    rand_lottery_list.append(random.randint(1, 100))

lottery_lst_entered = []

print('Please enter 7 numbers: ')
for i in range(0,7):
    c = int(input())
    lottery_lst_entered.append(c)

m_list = []
for number in rand_lottery_list:
    for number1 in lottery_lst_entered:
        if number == number1:
            m_list.append(number)

number_of_matches = len(m_list)

rewards = {3: "£20.0", 4: "£40", 5: "£100", 6: "£10000", 7: "£1000000"}

if number_of_matches in rewards:
    the_reward = rewards[number_of_matches]
    print('Congratulation, your ticket has {} matching numbers and you won {}!'.format(number_of_matches, the_reward))
else:
    print('Sorry, no luck this time! Try again Later.')



#code replaced with dictionary
# if number_of_matches == 3:
#     print('Congratulation, your ticket has {} matching numbers and you won £20!'.format(number_of_matches))
# elif number_of_matches == 4:
#     print('Congratulation, your ticket has {} matching numbers and you won £40!'.format(number_of_matches))
# elif number_of_matches == 5:
#     print('Congratulation, your ticket has {} matching numbers and you won £100!'.format(number_of_matches))
# elif number_of_matches == 6:
#     print('Congratulation, your ticket has {} matching numbers and you won £10000!'.format(number_of_matches))
# elif number_of_matches == 7:
#     print('Congratulation, your ticket has {} matching numbers and you won £1000000'.format(number_of_matches))
# else:
#     print('Sorry , no luck this time')
#
# print(number_of_matches)



# print(rand_lottery_list)

