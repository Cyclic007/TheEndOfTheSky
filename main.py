from time import sleep
print('Bartender- Welcome to my tavern! You must have come a long way.')
sleep(1)
one = input(
    'Bartender- How about a drink? We have water and milk! 1-water 2-milk')
if one == '1':
    print('Bartender- Ok! One water coming right up!')
elif one == '2':
    print("Bartender- Ok! One milk coming right up!")
else:
    print("Bartender- Sorry, we do not have that. I'll get you some water.")
sleep(1)
print('As you look around, you see a mysterous person in the background.')
print('He looks at you and walks over.')
sleep(1)
two = input(
    'Person- I have not seen you around here. Are you new to these parts?')
print(
    'Person- Well, if your new or not, I do not like attention. Stay off my back.'
)
sleep(1)
print('He walks back to his table.')
three = input('Do you follow him? y/n')
if three == 'y':
    print('You jump behind a table and creep closer.')
else:
    print('Bartender- Here is your drink!')
sleep(1)
print("The door bursts open and three bandits run in.")
print('Bandit 1- Everyone put your hands up!')
sleep(1)
print('Bandit 2- Search them')
