
#                                 ============  step 1  ============

#T0D0-1.1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#T0D0-1.2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#T0D0-1.3 - Check if the letter the user guessed (guess) is one of the leters in the chosen word.


#                                 ============  step 2  ============

#T0D0-2.1: - Create an empty List called display. For each letter in the randWord, add a "_" to 'display. So if the randWord was "apple", display should be ["_","_","_","_","_"] with 5 "_" representing each letter to guess.
#T0D0-2.2: - Loop through each position in the randWord; If the letter at that position matches 'guess' then reveal that letter in the display at that position.
            # e.g. If the user guessed "p" and the chosen word was "apple", then display should be	["_","p","p","_","_"]
#T0D0-2.3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".


#                                 ============  step 3  ============

#T0D0-3.1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the randWord and 'display' has no more blanks.	Then you can tell the user they've won.


#                                 ============  step 4  ============

#T0D0-4.1: - Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.

#T0D0-4.2: - If guess is not a letter in the randWord, then reduce 'lives' by 1. If lives goes down to 0 then the game should stop and it should print "You lose."
#Join all the elements in the list and turn it into a String.  print(f"{' '.join(display)}")

#T0D0-4.3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.


#                                 ============  step 5  ============

#T0D0-5.1: - Update the word list to use the 'word_list' from hangman_words.py #Delete this line: word_list = ["ardvark", "baboon", "camel"]
#T0D0-5.2: - Import the logo from hangman_art.py and print it at the start of the game.
#T0D0-5.3: - Import the stages from hangman_art.py and make this error go away. print(stages [lives])



import random
import hangman_words
import hangman_art
import os

print(hangman_art.logo)

randWord = random.choice(hangman_words.word_list)
disPlay = []
for ch in randWord :
    disPlay.append("_")

print(disPlay)

#Testing code
print(f'Pssst, the solution is { randWord }.')


end_game = False
lives = 6

while not end_game :
    askChr = input("\n\t\tGuess a letter : ").lower()

    for i in range(0, len(randWord)) :
        if randWord[i] == askChr:
            disPlay[i] = randWord[i]
        else:
            disPlay[i] = disPlay[i]
            
    if not (askChr in randWord): 
        lives = lives - 1
    
    os.system('cls')
    print(hangman_art.stages[lives])
    print(disPlay) 

    if lives == 0:
        end_game = True
        print("\n\t\t\tYou lose !!\n")
    elif not ("_" in disPlay):      
        end_game = True
        print("\n\t\t\tYou Win !!")
        print(f"\n\t\t\t{''.join(disPlay)}\n")


# python main.py

# # ========== clear screen ============
# import os
# import time
# # for windows
# # os.system('cls')
# os.system("ls")
# time.sleep(2)
# # Ubuntu version 10.10
# os.system('clear')