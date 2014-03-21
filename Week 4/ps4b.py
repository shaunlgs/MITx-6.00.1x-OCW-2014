from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0

    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = "None"
    
    # For each word in the wordList
    for i in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(i, hand, i):
            # Find out how much making that word is worth
            wordScore = getWordScore(i, n)
            # If the score for that word is higher than your best score
            if wordScore > bestScore:
                # Update your best score, and best word accordingly
                bestScore = wordScore
                bestWord = i
    # return the best word you found.
    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    total = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand):
        # Display the hand
        print("Current Hand:"), 
        displayHand(hand)
        # Tell how many points the word earned, and the updated total score, in one line followed by a blank line
        word = compChooseWord(hand, wordList, n)
        # if there is no best word, break
        if word == "None":
            break
        score = getWordScore(word, n)
        total += score
        print("\"" + word + "\"" + " earned " + str(score) + " points. Total: " + str(total) + " points.")
        print
        # Update the hand
        hand = updateHand(hand, word)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print("Total score: " + str(total))
    print
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # variable to keep track if this is the first game the user played
    firstGame = True
    while True:
        # ask user to input 'n' or 'r' or 'e'.
        print("Enter n to deal a new hand, r to replay the last hand, or e to end game:"),
        userInput = raw_input()
        # if input is 'r'
        if userInput == 'r':
            # if this is first game
            if firstGame == True:
                # print warning
                print("You have not played a hand yet. Please play a new hand first!")
            # if this is not first game
            elif firstGame == False:
                while True:
                    # asks if user wants computer to play
                    print("Enter u to have yourself play, c to have the computer play:"),
                    userCompInput = raw_input()
                    if userCompInput == 'u' or userCompInput == 'c':
                        break
                    print("Invalid command.")
                # if user wants to play
                if userCompInput == 'u':
                    print
                    # start game
                    playHand(hand, wordList, HAND_SIZE)
                    print
                # if user wants computer to play
                elif userCompInput == 'c':
                    print
                    # computer play
                    compPlayHand(hand, wordList, HAND_SIZE)
                    print
                # if user input is other
                else:
                    print("Invalid command.")
        # if input is 'e'
        elif userInput == 'e':
            # exit
            break
        # if input is 'n'
        elif userInput == 'n':
            while True:
                # asks if user wants computer to play
                print("Enter u to have yourself play, c to have the computer play:"),
                userCompInput = raw_input()
                if userCompInput == 'u' or userCompInput == 'c':
                    break
                print("Invalid command.")
            # if user wants to play
            if userCompInput == 'u':
                firstGame = False
                # deal hand
                hand = dealHand(HAND_SIZE)
                print
                # start game
                playHand(hand, wordList, HAND_SIZE)
                print
            # if user wants computer to play
            elif userCompInput == 'c':
                firstGame = False
                # deal hand
                hand = dealHand(HAND_SIZE)
                print
                # computer play
                compPlayHand(hand, wordList, HAND_SIZE)             
        # if input is other 
        else:
            print("Invalid command.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


