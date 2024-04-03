def besenica(userInput,tries):
    while True: 
        if tries>0:     
            guess=input('Enter a letter: ')
            if guess in userInput:
                for i in range(len(userInput)):
                    if userInput[i]==guess:
                        currentList[i]=guess
                print(currentList)
                print(f"Left tries: {tries}")
            elif guess not in userInput:
                print(f'{guess} is not in the word!')   
                print(f"Left tries: {tries}")
        else:
            print(f'Your tries finished.\nThe word was {uInput}\nBetter luck next time :)')
            break
        if currentList == userInput:
            print(f"You won!!! From the {tries} try ")
            break
        tries-=1

uInput=input("Enter a word to be guessed: ")
userInput=list(uInput)
tries=6
currentList=['_' for _ in userInput]
besenica(userInput,tries)
