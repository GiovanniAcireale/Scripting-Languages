# Nap Time 2.0
# added random to simulate odds
# turned the original program into a betting game
# each input dictates different chance increases

import random

def prob(chance):
    x = random.randint(0, 100)
    if x < chance:
        win = True
    else:
        win = False
    return win

def questions():
    while True:
        hour = int(input("What hour is it on the clock? "))
        if hour > 12 or hour < 1:
            print("Not a valid number! (Enter a number between 1 and 12) ")
            continue
        else:
            str(hour)
            break

    while True:
        minute = int(input("What minute? "))
        if minute > 59 or minute < 0:
            print("Not a valid number! (Enter a number between 0 and 59) ")
            continue

        else:
            str(minute)
            break
        
    while True:
        pm = input("'am' or 'pm'?  ")
        if pm not in ["am", "pm"]:
            print("Not a valid input! (Enter 'am' or 'pm') ")
            continue
        else:
            break
        
    while True:
        boss = input("Has your boss left yet (y/n)? ")
        if boss not in ['y', 'n']:
            print("Not a valid input! (Enter 'y' or 'n') ")
            continue
        else:
            break
    
    while True:
        room = input("Is the breakroom clear (y/n)? ")
        if room not in ['y', 'n']:
            print("Not a valid input! (Enter 'y' or 'n') ")
            continue
        else:
            break
    
    while True:
        twin = input("Will your twin cover you (y/n)? ")
        if twin not in ['y', 'n']:
            print("Not a valid input! (Enter 'y' or 'n') ")
            continue
        else:
            break
    
    return hour, minute, pm, boss, room, twin

def pointCalc():
    oghour, ogmin, inpm, noboss, inroom, twin2 = questions()
    
    if ogmin >= 0 and ogmin < 10:
        print(f'\nThe time is {oghour}:0{ogmin}{inpm}\n')
    else:    
        print(f'\nThe time is {oghour}:{ogmin}{inpm}\n')

    # the users input will have different odds of 
    # succeeding and they will stack with each other 
    odds = 0
    # after 3pm
    a = 20
    # boss left
    b = 40
    # breakroom clear
    c = 30
    # twin 
    # win = true
    if twin2 == "n":
        if (oghour > 2) and inpm == "pm":
            print("It's after 3:00pm", end = '')
            odds += a
            #print(f' +{odds}%')
            if noboss == "y":
                print(" and your boss left already", end = '')
                odds += b
                #print(f' +{odds}%')
                if inroom == "y":
                    print(" AND the break room is clear!")
                    odds += c
                    #print(f' +{odds}%')
                else:
                    odds += 0
            else:
                print(" but your boss is still here.")
                odds += 0
            success = prob(odds)
        elif inroom == "y":
            odds += c
            #print(f'+{odds}%')
            print("You notice the breakroom is clear.")
            while True:
                try:
                    riskit = input("Want to risk a nap in there (y/n)? ")
                except ValueError or riskit != ("y", "n"):
                    print("Not a valid input! (Enter 'y' or 'n') ")
                    continue
                else:
                    break
            if riskit == "y" and noboss == "y":
                odds += b
                #print(f'+{odds}%')
                print("you try and nap in the breakroom.")
                success = prob(odds)
            elif riskit == "y":
                odds += 0
                print("you try and nap in the breakroom.")
                success = prob(odds)
            else:
                print("Looks like you'll have to tough it out today.")
                return
        else:
            print("No shot at napping today it seems.")
            return
    else:
        print("Luckily your identical twin is willing to cover you at the desk.")
        print("You are free to nap as you please!")
        success = True
    if success == True:
        print("\nYou successfully napped on the job!")
    elif success == False and noboss == "n":
        print("\nYou got caught by your boss! He fired you.")
    else:
        print("\nYou got caught and later fired.")
        
    #print(f' total +{odds}%')
    return

def nextDay():
    print("\n* * * * * * * * * * * * * * * * * * *")
    if input("Press 'y' to play again: ") == "y":
        print("* * * * * * * * * * * * * * * * * * *\n")
        return True
    else:
        return False
    
print("It's another afternoon at work and you feel a little tired.")
print("Maybe you can sneak in one of your famous work naps! Lets see...")
pointCalc()
while nextDay():
    pointCalc()
print("\n* * * * * * * * * * * * * * * * * * *")

print("Goodbye!\n")
