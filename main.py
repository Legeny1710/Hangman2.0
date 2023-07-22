import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



                                                                    
                                                                    

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
print("WELCOME TO HANGMAN!")

wordList = ["hello", "pyhton", "macbook", "apple"]

#Choosing the random word
chosenWord = random.choice(wordList)

print("Lets start!")
print("...")
print("Here is your word!")

#Displaying the chosen word
display = []
for i in range(0, len(chosenWord)):
  display.append("_")

print(display)


NumOfGuesses = 7
print(f'You have {NumOfGuesses} guesses!')

guess = input("Guess a letter: ").lower()

UsedWordList = []

letterGuessed = False
index = 0

while NumOfGuesses != 0:
  letterGuessed = False
  
  # Checking if the guess is in the chosen word
  for i in range(0, len(chosenWord)):
    if chosenWord[i] == guess:
      letterGuessed = True
      index = i
      display[index] = guess
    

  
  
  #Checks if the user guessed the same letter
  if guess in UsedWordList:
      print("You already have guessed this letter, try again!")
  else:
    NumOfGuesses -= 1
    UsedWordList.append(guess)

  if letterGuessed == False and chosenWord != guess:
    print(stages[NumOfGuesses-1])
    print("Oops, Try Again!")
  elif letterGuessed == True:
    print(stages[NumOfGuesses])
    print("Well Done! Good Guess!")
    
  
  displayWord = ""
  for i in display:
    displayWord += i

  
  if chosenWord == displayWord:
    print("You Win!")
    break

  if chosenWord == guess and letterGuessed == False:
    print("You Win!")
    break

  
  print(display)
  print(f'You have {NumOfGuesses} guesses!')
  print("Letters that have been used: ", UsedWordList)
  guess = input("Guess a letter: ").lower()


  
if NumOfGuesses == 0:
  print("Sorry but You LOST!")

