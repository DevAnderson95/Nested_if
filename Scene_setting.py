# Tasks 2 & 3

place = input("Choose a place: forest or cave?: ")


if place == "forest":
   print(place)
   action = input("climb a tree or cross a river?") 
   if action == "climb a tree":
        print("You found a bird's nest!")
   elif action == "cross a river":
        print("You found a boat!")
   else:
        pass
        print("INVALID ENTRY!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Lead the way navigator!")
    elif action == "proceed in the dark":
        print("Watch out for creepy crawlers!")
    else:
        pass
        print("INVALID ENTRY!")
else:
    print("INVALID ENTRY!")
