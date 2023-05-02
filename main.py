print("🌟MokeBeast Generator🌟")

moke = {}

def prettyPrint():
  print()
  for key, value in moke.items():
    print(key, end=": ")
    for subkey, subvalue in value.items():
      print(subkey, subvalue, end=" | ")
    print()

while True:
  name = input("\nInput your beast's name > ").strip().title()
  type = input("\nInput your beast's type > ").strip().title()
  move = input("\nInput your beast's special move > ").strip().title()
  hp = input("\nInput your beast's staring HP > ").strip().title()
  mp = input("\nInput your beast's staring MP > ").strip().title()
  
  moke[name] = {"Type":type, "Move":move, "HP":hp, "MP":mp}
  
  #if moke["Type"] == "Water":
    #print("\033[44m", end="")
  #elif moke["Type"] == "Fire":
    #print("\033[31m", end="")
  #elif moke["Type"] == "Air":
    #print("\033[37m", end="")
  #elif moke["Type"] == "Earth":
    #print("\033[32m", end="")
  #elif moke["Type"] == "Spirit":
    #print("\033[45m", end="")

  prettyPrint()
  
  proceed = input("Again? y/n > ").lower()
  if proceed == "y":
    continue
  elif proceed == "n":
    break
  

#figure out how to make the color of the letter

#figure out to align the ":"