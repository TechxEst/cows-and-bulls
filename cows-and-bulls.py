import random
import string

def cows_and_bulls():                                                                               
    cows = 0                                                            # initiate count of cows
    bulls = 0                                                           # initiate count of bulls
    num_guesses = 0                                                     # initiate count of guesses
    num_length = 4                                                      # length of random number

    random_num = random.sample(list(string.digits), 4)                  # create a random number of 4 digits from all digits
    guess = list(input("enter a 4 digit number:"))                      # ask user to guess

    while guess != random_num:                                          # while they aren't the same                                    
        checkpoint = 0                                                  # initiate the checkpoint
        while checkpoint < num_length-1:                                # while the checkpoint is < length of random number
            for digit in guess:                                         # for each digit in the guess
                if digit not in random_num:                             # if it's not in random number
                    guess[checkpoint] = "x"                             # change the guess digit to an x
                    checkpoint += 1                                     # increase the checkpoint position by 1
                    continue                                            # continue to the next digit
                                                                        # elif guess digit and random number digit are the same
                elif guess[guess.index(digit)] == random_num[checkpoint]:
                    cows += 1                                           # add 1 to cows
                    guess[checkpoint] = "x"                             # change the guess digit to an x
                    checkpoint += 1                                     # increase the checkpoint position by 1
                
                elif digit in random_num:                               # elif guess digit is in the random number
                    bulls += 1                                          # add 1 to bulls
                    guess[checkpoint] = "x"                             # change the guess digit to an x
                    checkpoint += 1                                     # increase the checkpoint position by 1

                pass

        num_guesses += 1                                                # increase number of guesses by 1
        print("{} cows, {} bulls".format(cows, bulls))                  # print the number of cows and bulls
        cows = 0                                                        # reset cows
        bulls = 0                                                       # reset bulls
        guess = list(input("enter a 4 digit number:"))                  # ask for another number
        if num_guesses > 10:                                            # if guesses gets over 10
            give_up = input("if you want to give up type yes")          # offer a way out of the mysery
            if give_up == "yes":                                        # if yes
                print("the number was {}".format("".join(random_num)))  # print out the random number
                break
            else:
                pass                                                    # keep going
    else:                                                               # when guess and random number are the same 
        print("you got it in {} guesses".format(num_guesses))           # print the number of guesses they got it in

cows_and_bulls()