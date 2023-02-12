#this is a test script for a math problem just out of curiousity 

""" If a player chooses to reduce, they must write a positive factor of the most recently written
number. If they choose to augment, they must write a number that is both 1) a positive
multiple of the most recently written number, and 2) a positive factor of the number they
themselves most recently wrote. """

#get the starting integer "N"
N = int(input("Starting number 'N'?: "))
while N <= 0: 
    print("Must be a positive integer")
    N = int(input("Starting number 'N'?: "))

#store player 1 and player 2's current numbers
p1_num = N
p2_num = 0
#used to assign current number 
counter = 1
past_num = p1_num
current_num = 0

print(current_num, p1_num, p2_num, counter, past_num)
#used to get the current number during a player's turn
def get_current_num():
    #ask player2 if they want to reduce or augment
    print("Reduce: Write a positive factor of the most recently written number. \nAugment: write a number that is both 1) a positive multiple of the most recently written number, and 2) a positive factor of the number you most recently wrote. ")
    choice = int(input("P2: Reduce (1) or Augment (2)? "))

    #past_num = current_num

    #checks to see if the int is positive
    current_num = int(input("Number? "))
    while current_num <= 0:
        print("Must be a positive integer")
        current_num = int(input("Number? "))

    #checks to see if the int is equal to 1
    if current_num == 1:
        print("You have submitted '1', you lose.")
    
    #updates the previous number placeholder
    counter = counter + 1
    if counter % 2 == 0: 
        p2_num = past_num
    else:
        p1_num = past_num

#code to check if the number is reduced or augmented properly
def check_choice(choice):
    #Reduce: they must write a positive factor of the most recently written number.
    if choice == 1: 
        if past_num % current_num == 0:
            print("okay")
        else: 
            print("That number does not reduce. Try again")
            get_current_num()

    #Augment: write a number that is both 1) a positive multiple of the most recently written number, and 2) a positive factor of the number they themselves most recently wrote.
    elif choice == 1:
        if current_num % past_num == 0:
            print(p1_num)
            print(p2_num)
        else: 
            print("That number does not augment. Try again")
            get_current_num()

    #updates past_num to current_num for next turn 
    past_num = current_num

#code for the first turn as player 2 is forced to reduce 
print("The first turn forces player 2 to reduce. Write a positive factor of the most recently written number. ")
choice = 1 #make reduce "1" and augment 2
p2_num = int(input("What is your first number? "))
current_num = p2_num 
print(current_num)
counter = counter + 1

while p1_num != 1 and p2_num != 1: 
    get_current_num()
    check_choice()
        
