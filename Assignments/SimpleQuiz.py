
real_answer1 = "T"
submitted_answer1 = (input("What letter does _iktok start with?\n>"))

if real_answer1 == submitted_answer1:
        print("correct")

else:
        print("incorrect")
real_answer2 = "red" or "Red"
submitted_answer2 = (input("What color are strawberries?\n>"))

if real_answer2 == submitted_answer2:
        print("correct")

else:
        print("incorrect")
        
        
real_answer3 = "green" or "Green"
submitted_answer3 = (input("What color is Grass?\n>"))

if real_answer3 == submitted_answer3:
        print("correct")

else:
        print("incorrect")

real_answer4 = "2"
submitted_answer4 = (input("How many times does the clock hit 12 in a day??\n>"))

if real_answer4 == submitted_answer4:
        print("correct")

else:
        print("incorrect")

real_answer5 = "East"
submitted_answer5 = (input("From where does the sun rise?\n>"))

if real_answer5 == submitted_answer5:
        print("correct")

else:
        print("incorrect")
    
def calculate():
        score = 0

        if submitted_answer1 == "T":
            score = score + 1

        if submitted_answer2 == "Red" or "red":
                score = score + 1
        
        if submitted_answer3 == "Green" or "green":
                score = score + 1

        if submitted_answer4 == "2":
                score = score + 1

        if submitted_answer5 == "East":
                score = score + 1

        print("SCORE: " + str(score) + "/5")

calculate()