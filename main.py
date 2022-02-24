from time import sleep
import os
hp = 100
damage = 4
inventory = ['Wood Sword', 'Small Health Potion']
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
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
sleep(1.5)
one = input(
    'Bartender- How about a drink? We have water and milk! 1-water 2-milk: ')
if one == '1':
  cls()
  print('Bartender- Ok! One water coming right up!')
elif one == '2':
  cls()
  print("Bartender- Ok! One milk coming right up!")
elif one != '1' and one != '2':
  while one != '1' and one != '2':
    cls()
    one = input(
    'Bartender- We do not have that. Would you like something else to drink? We have water and milk! 1-water 2-milk: ')
    if one == '1' or one == '2':
      break
sleep(1.5)
cls()
print('As you look around, you see a mysterous person in the background.')
print('He looks at you and walks over.')
sleep(1.5)
two = input(
    'Person- I have not seen you around here. Are you new to these parts?[y/n] ')
if two == 'y':
  cls()
  print("First off, welcome. Second, for the record I loath attention. Stay off my back")
if two == 'n':
  cls()
  print("Huh, thats interesting... Also if you didnt know already, I loath attention, so stay off my back.")
sleep(1.5)
print('He walks back to his table.')
three = input('Do you follow him? y/n: ')
if three == 'y':
    cls()
    print('You jump behind a table and creep closer.')
else:
    cls()
    print('Bartender- Here is your drink!')
sleep(1.5)
print("The door bursts open and three bandits run in.")
print('Bandit 1- Everyone put your hands up!')
sleep(1.5)
print('Bandit 2- Search them')
print('The bandits walk in and shove over the patrens.')
sleep(1.5)
print('They walk right past you, pockets filled with gold.')
sleep(1.5)
four = input('Do you attack? y/n: ')
if four == 'y':
  fight(1)
elif four == 'n':
  cls()
  print('You hide under the table, waiting for them to pass.')
  sleep(1.5)
  print('Bandit 2- Hey! I found one hiding under here.')
  print('The bandit points to you. Time to fight!')
  fight(1)
else:
  print('Please follow instructions. You will attack. Happy now? ')
  fight(1)