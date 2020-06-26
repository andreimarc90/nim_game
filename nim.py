def main():
    stones = 20 #setting stone number to 20
    player = 2
    print("There are", stones, "stones left") #here we display the number of stones
    while stones != 0:
        if player == 2:   #Making sure player 1 is first
            player = 1
        else:
            player = 2    #then we finish the turns cycle: 1-2-1-2-1-2 etc.
        remove = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
        while stones < remove: #we make sure that the player can't remove 2 stones when there is 1 left
            print("You took more stones then available. Try again.")
            remove = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))

        while remove <= 0 or remove > 2: # we make sure the input is always 1 or 2
            remove = int(input("Please enter 1 or 2: "))
        print("")

        stones -= remove #we remove user input from the stones stack


        if stones == 0:
            """Here we make sure that the last player to take a stone is NOT the winner
            If player 2 took the last 2 stones, he will lose.
            If he takes 1, then player 1 loses"""
            if player == 1:
                player = 2
            else:
                player = 1
            print("Player " + str(player) + " wins!")
        else:
            print("There are", stones, "stones left")

if __name__ == '__main__':
    main()
