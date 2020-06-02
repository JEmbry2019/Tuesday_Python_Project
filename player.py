import time

def main_loop(categories):
    ''' Run through game until board is cleared. '''

    # Introduction-
print('\n\n*****************\nThis is Jeopardy!\n*****************\n')
time.sleep(2)
print('The quiz game-show, where the answers are revealed and the contestants must guess the questions.\n')
time.sleep(4)
print('Note: Spelling counts in this version.\n')
time.sleep(3)
print("Let's play.\n")
time.sleep(1)
        
        # Asks and saves player's name
print("Please enter the contestant's name")
NAME = input("> ").title()
print()

print("Welcome {}!".format(NAME))
time.sleep(1)
print('Thanks for joining today.\n')
time.sleep(2)

#     # First set of instructions
#     print("Now, {}, take a look at the board and make your first selection.".format(NAME))
#     print("(You can enter 'exit' at any time to end game)")
#     update_board(categories[0], 0)
#     time.sleep(1)

#     # Player begins with score of zero
#     score = 0

#     # Will run until there are no more integers on the board
#     while check(categories):
#         category = category_select()
#         amount = amount_select(category)
#         pull_answer(category, amount)
#         score = compare(category, amount, score)
#         update_board(category, amount)
    
#     # End of game salutations
#     if score > 0:
#         print("Congratulations {}, you've won ${}.".format(NAME, score))
#         print("Don't spend it all in one place. Thanks for playing.")

#     elif score < 0:
#         print("Sorry, {}. Unfortunately you ended with -${} and will be walking away with nothing today.".format(NAME, abs(score)))
#         print("Thanks for playing.")

#     elif score == 0:
#         print("{}, your final total is ${}.".format(NAME, score))
#         print("No harm done. Thanks for playing.")

# # Begin game-
# main_loop(categories)