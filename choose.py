a = input("Which file?")
if a == "main":
  import main.py
elif a == "gui":
  import gui.py
elif a == "commands":
  import commands.py
elif a == "admin":
  print ("There is no admin, you fool!")