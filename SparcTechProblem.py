#this is a test script for a math problem just out of curiousity 

""" If a player chooses to reduce, they must write a positive factor of the most recently written
number. If they choose to augment, they must write a number that is both 1) a positive
multiple of the most recently written number, and 2) a positive factor of the number they
themselves most recently wrote. """

#used to get the current number during a player's turn
def get_current_num(choice, past_num, p1_num, p2_num):

    #checks to see if the int is positive
    current_num = int(input("Number? "))
    while current_num <= 0:
        print("Must be a positive integer")
        current_num = int(input("Number? "))

    #code to check if the number is reduced or augmented properly

    #Reduce: they must write a positive factor of the most recently written number.
    if choice == 1: 
        if past_num % current_num == 0:
            print("That number reduces. Next player's turn.")
        else: 
            print("That number does not reduce. Try again")
            return get_current_num(choice, past_num, p1_num, p2_num) #Recurse until number is valid

    #Augment: write a number that is both 1) a positive multiple of the most recently written number, and 2) a positive factor of the number they themselves most recently wrote.
    elif choice == 2:
        which_player = int(input("What player are you? (1 or 2) "))
        
        #code to check if number is a positive factor of P1's most recently written number
        if which_player == 1: 
            if current_num % past_num == 0 and p1_num % current_num == 0: 
                print("That number augments. Next player's turn.")
            else: 
                print("That number does not augment. Try again")
                return get_current_num(choice, past_num, p1_num, p2_num)
        elif which_player == 2:
            if current_num % past_num == 0 and p2_num % current_num == 0: 
                print("That number augments. Next player's turn.")
            else: 
                print("That number does not augment. Try again")
                return get_current_num(choice, past_num, p1_num, p2_num)
        else: 
            print("That is not a valid player number. Try again. ")
            which_player = int(input("What player are you? (1 or 2) "))

    return current_num

def main(): 
    #get the starting integer "N"
    N = int(input("Starting number 'N'?: "))
    while N <= 0: 
        print("Must be a positive integer")
        N = int(input("Starting number 'N'?: "))

    #code for the first turn as player 2 is forced to reduce 
    print("The first turn forces player 2 to reduce. Write a positive factor of the most recently written number. ")
    choice = 1 #make reduce "1" and augment 2
    p2_num = int(input("What is your first number? "))
    current_num = p2_num 
    counter = 1
    p1_num = N

    while True:
        #ask player2 if they want to reduce or augment
        print("Reduce: Write a positive factor of the most recently written number. \nAugment: write a number that is both 1) a positive multiple of the most recently written number, and 2) a positive factor of the number you most recently wrote. ")
        choice = int(input("Player: Reduce (1) or Augment (2)? "))
            
        current_num = get_current_num(choice, current_num, p1_num, p2_num)

        #checks to see if the int is equal to 1
        if current_num == 1:
            print("You have submitted '1', you lose.")
            quit()

        #updates the previous number placeholder
        counter += 1
        if counter % 2 == 0: 
            p2_num = current_num
        else:
            p1_num = current_num

if __name__ == "__main__":
    main()