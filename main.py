from time import sleep
hp = 100
damage = 4
inventory = ['Wood Sword', 'Small Health Potion']
def fight(number):
  if number == 1:
    enemy1_hp = 10
    enemy1_damage = 1
    enemy2_hp = 10
    enemy1_damage = 1
    enemy3_hp = 10
    enemy1_damage = 1
    print('')
    if enemy1_hp <= 0 and enemy2_hp <= 0 and enemy3_hp <= 0:
      print('')
  elif number == 2:
    enemy1_hp = 20
    enemy2_hp = 25
    print('')
  elif number == 3:
    enemy1_hp = 40
    print('')
  elif number == 4:
    enemy1_hp = 65
    print('')
  elif number == 5:
    enemy1_hp = 90
    print('')
  else:
    print('Error!')
def commands(command):
  if command == 'exit':
    exit()
print('Bartender- Welcome to my tavern! You must have come a long way.')
sleep(1)
one = input(
    'Bartender- How about a drink? We have water and milk! 1-water 2-milk: ')
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
    'Person- I have not seen you around here. Are you new to these parts? ')
print(
    'Person- Well, if your new or not, I do not like attention. Stay off my back.'
)
sleep(1)
print('He walks back to his table.')
three = input('Do you follow him? y/n: ')
if three == 'y':
    print('You jump behind a table and creep closer.')
else:
    print('Bartender- Here is your drink!')
sleep(1)
print("The door bursts open and three bandits run in.")
print('Bandit 1- Everyone put your hands up!')
sleep(1)
print('Bandit 2- Search them')
print('The bandits walk in and shove over the patrens.')
sleep(1)
print('They walk right past you, pockets filled with gold.')
sleep(1)
four = input('Do you attack? y/n: ')
if four == 'y':
  fight(1)
elif four == 'n':
  print('You hide under the table, waiting for them to pass.')
  sleep(1)
  print('Bandit 2- Hey! I found one under here.')
  print('The bandit points to you. Time to fight!')
  fight(1)
else:
  print('Please follow instructions. You will attack. Happy now? ')
  fight(1)