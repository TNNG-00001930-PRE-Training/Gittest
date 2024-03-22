'''2. Guess the Number

1. The program should generate a random number within a specified range (e.g., 1-100).
2.The user should be prompted to guess the number.
3.After each guess, the program should provide feedback to the user if the guess is too high or too low.
4.The user should have a limited number of attempts (e.g., 7 or 10).
5.If the user guesses the correct number, the program should display a congratulatory message.
6. If the user runs out of attempts, the program should reveal the correct number and display a "better luck next time" message.
7. The program should allow the user to play again or exit after each game.'''

import random

class GuessTheNumber:
    def __init__(self, min=1, max=100, max_attempts=7):
        self.min = min
        self.max = max
        self.max_attempts = max_attempts
        self.secret_number = 0
        self.attempts = 0
    
    def generate_secret_number(self):
        self.secret_number = random.randint(self.min, self.max)
        

    def playgame(self):
