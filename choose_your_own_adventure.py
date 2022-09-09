name = input('Type your name: ')
print(f"Welcome {name} to this adventure!")

answer = input(
        """
        You are on a dirt road, 
        it has come to an end and 
        you can go left or right.
        Which way would you like ro go?
        left or right [l/r]
        """).lower()

if answer == 'l':
    answer = input(
        """
        You come to a river,
        you can walk around it or 
        swim across? [w/s]  
        """)
    if answer == 's':
        print("Oops! You were eaten by an alligator!")
    elif answer == 'w':
        print(
            """
            You walk a lot, you were dehydrated, 
            you lose the game.
            """
        )
    else:
        print('Not a valid option. You lose')
elif answer == 'r':
    answer = input(
        """
        You came to a bridge, it looks wobbly,
        do you want to cross it or 
        head back? [c/b]
        """)
    if answer == 'c':
        print("""
            Oops! You came to the road and hit by a car. 
            you lose the game.
            """)
    elif answer == 'b':
        answer = input(
            """
            You cross the bridge and meet a man.
            Do you talk to them? [y/n]
            """
        )
        if answer == 'y':
            print("You were offered a lot of money, You won the game.")
        elif answer == 'n':
            print(
                """
                You are tired and no money to buy food. 
                You lose the game.
                """)
        else:
            print('Not a valid option. You lose')
    else:
        print('Not a valid option. You lose')

else:
    print('Not a valid option. You lose')

print("Thank you for playing!")
