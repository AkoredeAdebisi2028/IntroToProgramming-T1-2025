Hurricane_classifier = (input("What's the current wind speed in MPH?"))

if int(Hurricane_classifier) <= 96:
    print("This is a category 1 hurricane")
elif int(Hurricane_classifier) <= 111:
    print("This is a category 2 hurricane")
elif int(Hurricane_classifier) <= 130:
    print("This is a category 3 hurricane")
elif int(Hurricane_classifier) <= 157:
    print("This is a category 4 hurricane")
elif int(Hurricane_classifier) >= 157:
    print("This is a category 5 hurricane")
elif int(Hurricane_classifier) <= 74:
    print("This is a tropical storm")