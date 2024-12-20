# Task 1 Buggy Code

attendees = int(input("Enter number of attendees: "))
venue = print("large hall") if attendees >= 100 else print("conference room")



# Task 2 56

if attendees >= 50:
    sound = input("Would you like to add a microphone and speaker?: ") 
    response = print("Microphone and stand will be added.") if sound == "yes" else print("Audio will be tuned to your liking.")

# Task 3 
food = input("Vegan Preference?: ")

if food == "yes":
    print("Veggie Delight Caterers has great services!")
else:
    print("Gourment Meals Caterers has great services!")