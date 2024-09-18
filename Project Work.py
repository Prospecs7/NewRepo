'''
PYTHON FINAL PROJECT
SOLOMON IFEANYI PROSPER
'''

totalScore = 0
spca = 2

def Quiz():
    print('Welcome to Torbita Quiz Game')
    print('1. Start Quiz')
    print('2. Quit Quiz')
    while True:
        action = input('Welcome, Choose an option: ')
        if action.isdigit():
            action = int(action)
            if action == 1:
                chooseSubject()
                break  
            elif action == 2:
                print('Goodbye!')
                break
            else:
                print('Invalid input. Please enter 1 or 2.')
        else:
            print('Invalid input. Please enter a number.')            
        
def chooseSubject():
    print('Choose a Subject:')
    print('1. English')
    print('2. Maths')
    print('3. Government')
    
    while True:
        subject = input('Enter the subject number: ')

        if subject.isdigit():
            subject = int(subject)

            if subject == 1:
                english(totalScore, spca)
                break
            elif subject == 2:
                maths(totalScore, spca)
                break  
            elif subject == 3:
                government(totalScore, spca)
                break
            else:
                print('Invalid input. Please enter 1, 2, or 3.')
        else:
            print('Invalid input. Please enter a number.')
        
def english(totalScore, spca):
    ans1 = ['seventy']
    Q1 = input('Question 1: Write 70 in words: ').strip().lower()
    if Q1 in ans1:
        score = spca
        totalScore += score
        print(f'Correct: {score}')
        print(f'Total Score is {totalScore}')
    else:
        score = 0
        print(f'Incorrect. {score}')
        print(f'Total Score is {totalScore}')

    ans2 = ['hot']
    Q2 = input('Question 2: What is the opposite of cold: ').strip().lower()
    if Q2 in ans2:
        score = spca
        totalScore += score
        print(f'Correct: {score}')
        print(f'Total Score is {totalScore}')
    else:
        score = 0
        print(f'Incorrect. {score}')
        print(f'Total Score is {totalScore}')

    ans3 = ['small']
    Q3 = input('Question 3: What is the opposite of big: ').strip().lower()
    if Q3 in ans3:
        score = spca
        totalScore += score
        print(f'Correct: {score}')
        print(f'Total Score is {totalScore}')
    else:
        score = 0
        print(f'Incorrect. {score}')
        print(f'Total Score is {totalScore}')

    endquiz(totalScore)

def maths(totalScore, spca):

    ans1 = 81
    try:
        Q1 = int(input('Question 1: What is 9 multiplied by 9?: '))
        if Q1 == ans1:
            score = spca
            totalScore += score
            print(f'Correct: {score}')
            print(f'Total Score is {totalScore}')
        else:
            score = 0
            print(f'Incorrect. {score}')
            print(f'Total Score is {totalScore}')

    except ValueError:
        print('Invalid Input. Please enter a number.')
        return maths(totalScore, spca)

    ans2 = 9
    try:
        Q2 = int(input('Question 2: What is the square root of 81?: '))
        if Q2 == ans2:
            score = spca
            totalScore += score
            print(f'Correct: {score}')
            print(f'Total Score is {totalScore}')
        else:
            score = 0
            print(f'Incorrect. {score}')
            print(f'Total Score is {totalScore}')

    except ValueError:
        print('Invalid Input. Please enter a number.')
        return maths(totalScore, spca)


    ans3 = 12
    try:
        Q3 = int(input('Question 3: What is 6 multiplied by 2?: '))
        if Q3 == ans3:
            score = spca
            totalScore += score
            print(f'Correct: {score}')
            print(f'Total Score is {totalScore}')
        else:
            score = 0
            print(f'Incorrect. {score}')
            print(f'Total Score is {totalScore}')

    except ValueError:
        print('Invalid Input. Please enter a number.')
        return maths(totalScore, spca)

    endquiz(totalScore)

def government(totalScore, spca):
    ans1 = ['abuja', 'fct']
    Q1 = input('Question 1: What is the Capital City of Nigeria? ').strip().lower()
    if Q1 in ans1:
        score = spca
        totalScore += score
        print(f'Correct: {score}')
        print(f'Total Score is {totalScore}')
    else:
        score = 0
        print(f'Incorrect. {score}')
        print(f'Total Score is {totalScore}')

    ans2 = 36
    try:
        Q2 = int(input('Question 2: Nigeria has how many states?(Please enter a number) '))
        if Q2 == ans2:
            score = spca
            totalScore += score
            print(f'Correct: {score}')
            print(f'Total Score is {totalScore}')
        else:
            score = 0
            print(f'Incorrect. {score}')
            print(f'Total Score is {totalScore}')
    except ValueError:
        print('Invalid Input. Please enter a number.')
        return government(totalScore, spca)
    
        
    ans3 = 774
    try:
        Q3 = int(input('Question 3: How many LGAs are in Nigeria?(Please enter a number) '))
        if Q3 == ans3:
            score = spca
            totalScore += score
            print(f'Correct: {score}')
            print(f'Total Score is {totalScore}')
        else:
            score = 0
            print(f'Incorrect. {score}')
            print(f'Total Score is {totalScore}')
    except ValueError:
        print('Invalid Input. Please enter a number.')
        return government(totalScore, spca)


    endquiz(totalScore)


def endquiz(totalScore):
    print("Congrats, You've reached the end of the Quiz")
    print(f'Your Final Score is: {totalScore}')
    while True:
        print('Would you like to play again?')
        print('1. Yes')
        print('2. No')
        another = input('Choose: ')

        if another.isdigit():
            action = int(another)
            if action == 1:
                chooseSubject()
            elif action == 2:
                print('Goodbye!')
                break
            else:
                print('Invalid input. Please enter 1 or 2.')
        else:
            print('Invalid input. Please enter a number.')


    if another == 1:
        Quiz()
    elif another == 2:
        print('Goodbye')
    else:
        print('Invalid Input. Please enter 1 or 2.')
        endquiz(totalScore)
        print('Thank you')

Quiz()






        
    

     

    
        
            
    
    
    
        
    
   
