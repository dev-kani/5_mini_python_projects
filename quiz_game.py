print('Welcome to my computer game!')

playing = input('Do you wanna play?[yes/no] ')

if playing.lower() != 'yes':
    quit()

print("okay! let's play :)")
score = 0

# question #1 -----------------------------
answer = input(
    """ 
        What does CPU stand for?
        a. Central Processing Unit
        b. Clock Processing Unit
        c. Central Production Unity 
    """

)
if answer.lower() == 'a':
    print("Correct! It stands for 'Central Processing Unit' ")
    score += 1
else:
    print('Incorrect!')

# question #2 -----------------------------
answer = input(
    """ 
        What does GPU stand for?
        a. General Processing Unit
        b. Graphics Processing Unit
        c. Game Production Unity 
    """

)
if answer.lower() == 'b':
    print("Correct! It stands for 'Graphics Processing Unit' ")
    score += 1
else:
    print('Incorrect!')

# question #3 -----------------------------
answer = input(
    """ 
        What does RAM stand for?
        a. Random Memory Access
        b. Random Access Memory
        c. Ready And Made 
    """

)
if answer.lower() == 'b':
    print("Correct!' It stands for 'Random Access Memory' ")
    score += 1
else:
    print('Incorrect!')

# question #4 -----------------------------
answer = input(
    """ 
        What does UPS stand for?
        a. Uninterruptible Power Supply
        b. Uninterrupted Power Supply
        c. United Power System 
    """

)
if answer.lower() == 'a':
    print("Correct! It stands for 'Uninterruptible Power Supply' ")
    score += 1
else:
    print('Incorrect!')

if score == 1:
    print(f"You got only {score} question correct! You failed the test ")
else:
    print(f"You got {score} question correct! You passed! ")
    print(f'Your score is {score / 4 * 100}%')



