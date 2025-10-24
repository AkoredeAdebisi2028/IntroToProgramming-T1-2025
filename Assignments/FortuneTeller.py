import random
def mystic_fortune_teller():
    print("Toodles~! Welcome to my mystical little cave!")

    try:
        lucky_number = int(input("What's your lucky number? 0-400?\n> "))
    except:
        print("You must enter a number queen..")
        mystic_fortune_teller()
    try:
        years = float(input("How many years into the future?\n> "))
    except:
        print("Hey, Honey.. You have to enter a float..")
        mystic_fortune_teller()
    try:
     multiplier = float(input("Enter your magical multiplier\n> "))
    except:
        print("DIVA.. ENTER A NUMBER.")
        mystic_fortune_teller()
    
    lucky_number = random.randint(1, 5)
    score = (lucky_number * multiplier * years ) - (years + 1)
    if score > 80:
        print("You will have magnificent luck soon!")
    elif score > 50:
        print("A happy suprise is coming your way!")
    elif score > 30:
        print("Satisfying news will reach your ears soon!")
    elif score > 10:
        print("You will learn a new thing soon!")
    else:
        print("Uhm, you're lowkey cooked gang. Like queen.. I kinda don't know what to tell you..")
mystic_fortune_teller()

