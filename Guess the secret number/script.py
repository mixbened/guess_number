import random

# setze einen secret
secret = random.randint(0,30)
attempts = 0

# hole den aktuellen high score und zeige ihn an
with open("high_score.txt", "r") as score_file:
    high_score = int(score_file.read())
    print("Your current high score is: " + str(high_score))

# lass die abfrage solange laufen, bis richtig getippt wurde
while True:
    
    # frag den nutzer nach input
    guess = int(input("Guess a Secret Number between 0 and 30: "))

    # check range
    if 0 <= guess <= 30:
        # if in range check if correct and give hint
        if guess == secret:
            # add one to attempts
            attempts = attempts + 1
            print("You won. Attempts: " + str(attempts))
            # if score is lower than high score, save to file
            with open("high_score.txt", "w") as score_file:
                score_file.write(str(attempts))
            break
        elif guess > secret:
            print("Try a smaller number.")
            # add one to attempts
            attempts = attempts + 1
        else:
            print("Try a higher number.")
            # add one to attempts
            attempts = attempts + 1
    else:
        print("Out of range")
        continue
