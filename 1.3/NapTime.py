# Nap Time
# if the time input is past 3:00 pm (15:00 M) AND the boss is gone 
# OR if the break room is clear
# OR if your twin can cover you
# you can take a nap at work.

print("It's another afternoon at work and you feel a little tired.")
print("Maybe you can sneak in one of your famous work naps! Lets see...")

time = input("What was the last hour that passed (1-12)? ")
boss = input("Is your boss still there (y/n)? ")
room = input("Is the breakroom clear (y/n)? ")
twin = input("Will your twin cover you (y/n)? ")

time = int(time)

if (time > 2) and boss == "n":
    print("It is past 3:00 and your boss isn't there so no one can stop you.")
elif room == "y" or twin == "y":
    print("You are free to nap as you please!")
else:
    print("Doesn't look like you can nap at all today")
