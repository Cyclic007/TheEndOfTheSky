shop = {
  "1": ["Bow and Arrows (10)", "15"],
  "2": ["Refill Arrows (15)", "10"],
  "3": ["Stone Sword", "20"],
  "4": ["Steel Sword", "25"],
  "5": ["Forged Sword", "30"],
  "6": ["Rare Bow and Arrows", "35"]
}
def exit():
  stop(all)
def shop(type):
  print(shop)
  purchase = input("What would you like?")
  if purchase == 1:
    gold = gold - 15
    inventory["weapon"] = "Bow and Arrows"
    arrows = 15
    global arrows
def commands(command):
  if command == 'exit':
    exit()