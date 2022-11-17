#!/usr/bin/env python3

condition= True
while condition:

    marvelchars= {
    "Starlord":
      {"real name": "peter quill",
      "powers": "dance moves",
      "archenemy": "Thanos"},

    "Mystique":
      {"real name": "raven darkholme",
      "powers": "shape shifter",
      "archenemy": "Professor X"},

    "Hulk":
      {"real name": "bruce banner",
      "powers": "super strength",
      "archenemy": "adrenaline"}
             }


    char_name= input("Which character do you want to know about? (Starlord, Mystique, Hulk)").capitalize()

    char_stat= input("What statistic do you want to know about? (real name, powers, archenemy)").lower()

    value= marvelchars[char_name][char_stat].title()

    print(f"{char_name}'s {char_stat} is: {value}") 

    check= input("Do you want to keep looking for more information? (y/n)").lower()
    if check == "y":
        condition= True
    else:
        condition = False
