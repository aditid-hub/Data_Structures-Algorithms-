#The "Guess the Number" project is a classic and fun beginner-friendly game. The core idea is simple: the computer thinks of a secret number within a specific range (like 1 to 100), and you, the player, try to guess it.
"""
The Secret is Chosen: The program first secretly and randomly picks an integer.

The Guessing Begins: You are prompted to enter your first guess.

The Comparison: The program compares your guess to its secret number.

The Hint is Given:

If your guess is less than the secret number, it prints "Too low!"

If your guess is greater than the secret number, it prints "Too high!"

The Loop Repeats: The game loops back to step 2, asking for another guess and continuing to provide hints.

The Win: When you finally guess the correct number, the program congratulates you, reveals the number, and the game ends. 🎉

"""
import random

random_integer = random.randint(1, 100)  # Generates a random integer between 1 and 100 (inclusive)
print("random_integer between 1 and 100:", random_integer)


print("Welcome to the guessing challenge 🦋 \nIn this game, you have to guess the number with unlimited chances 🤩\nSo let's start the game🚀" )
number= int(input("Guess a number:"))




while number!=random_integer :
    if number < random_integer :
        print("your number is small, take a larger number🐬 ")
        number = int(input("Enter a larger number :"))

    elif number > random_integer :
        print("your number is large, take a smaller number🦈 ")
        number = int(input("Enter a smaller number :"))
    
    else :
        print("You got the number🐳 ")

        break
print("You got the number🐳 :",number)


