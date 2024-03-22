#Calculator
#1. The calculator should be a command-line application.
#2. It should support basic arithmetic operations: addition, subtraction, multiplication, and division.
#3. The user should be able to input two numbers and the desired operation.
#4. The program should perform the requested operation on the two numbers and display the result.
#5. Proper input validation should be implemented to handle non-numeric inputs or divide-by-zero cases.
#6. The program should provide a menu or prompt to allow the user to perform multiple calculations or exit the program.

class Calculator:
    def __init__(self):
        self.operations = {
            '+' : self.addition,
            '-' : self.subtraction,
            '*' : self.multiplication,
            '/' : self.division
        }

    def addition(self, num1, num2):
        return num1 + num2
    
    def subtraction(self, num1, num2):
        return num1 - num2
    
    def multiplication(self, num1, num2):
        return num1 * num2
    
    def division(self, num1, num2):
        if num2 == 0:
            return 'Error! Division by zero.'
        return num1/num2
    def performOperation(self):
        while True:
            try:
                num1 = float(input('Enter the first number: '))
                num2 = float(input('Enter the second number: '))
                operation = input('Enter the operation you want to do (+, -, *, /): ')

                if operation not in self.operations:
                    print("Please Enter valid operator (for eg. +,-,*,/)")
                    continue
                result = self.operations[operation](num1, num2)
                print(f"Result: {result}")

            except ValueError:
                print("Invalid input! please input numerical value")

            except Exception as e:
                print("An error occured!", e)

            choice = input("Do you want another operation yes/no?: ")
            if choice.lower() == 'no':
                print('Exiting the calculator!')
                break
            


c = Calculator()
c.performOperation()