# Task 1 Buggy Code

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees >= 100 else print("conference room")

print(venue)

# Task 2 56

sound = input("Would you like to add a microphone and speaker?: ") if attendees >= 50 else print(input("How about a big screen?: "))  