class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in upper case:", self.input_string.upper())

def test_string_manipulator():
    manipulator = StringManipulator()
    manipulator.getString()
    manipulator.printString()

# Test the class methods
test_string_manipulator()
