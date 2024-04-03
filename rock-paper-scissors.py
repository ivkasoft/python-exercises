import random
scoreComp=0
scoreUser=0
while True:
    if scoreUser==3 or scoreComp==3:
        break
    
    userInput=int(input('Enter number: [1-rock, paper-2, scissors-3]: '))
    compInput=random.randint(1,3)
    print(f"The computer choice: {compInput}")
    if userInput==1 and compInput==3:
        scoreUser+=1
    elif userInput==3 and compInput==1:
        scoreComp+=1
    elif userInput==compInput:
        pass
    elif userInput>compInput:
        scoreUser+=1
    elif userInput<compInput:
        scoreComp+=1
    print(f"Score:\nComp={scoreComp}\nUser={scoreUser}")
winner=None
if scoreComp>scoreUser:
    winner="computer"
else:
    winner="user"
print(f'The winner is the {winner}')
