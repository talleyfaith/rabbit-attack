# Rabbit Attack!

def confirm(question):
    while True:
        ans = input(question + " (y/n)")
        if ans[0].lower() == "y":
            return True
        elif ans[0].lower() == "n":
            return False
        else:
            print("Sorry that's not a valid answer. Please try again.") 

playing = True

while playing:

    num_knights = 5
    rabbit_is_alive = True

    print("Look, a cute little bunny rabbit.")

    while rabbit_is_alive and num_knights > 0:
        answer = confirm("Shall we use the holy hand grenade?")

        if answer == True:
            use_grenade = True
        else:
            use_grenade = False

        if use_grenade:
            print("1... 2... 5... No, 3!")
            print("Boom!")
            rabbit_is_alive = False
        else:
            num_knights -= 1
            print("Oh, no! The rabbit just killed one of the knights!")
            print("Only " + str(num_knights) + " remain.")
        
    if num_knights > 0:
        print("The killer rabbit has been defeated. You win!")
    else:
        print("All of the knights are dead. You lose.")
        
    answer = confirm("Would you like to play again?")

    if answer == True:
        playing = True
    else:
        playing = False

print("Goodbye. Thanks for playing!")
        
