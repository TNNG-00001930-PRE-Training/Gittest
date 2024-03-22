class StringConcatenator:
    def __init__(self):
        self.concatenated_string = "Hi "

    def add_string(self, new_string):
        self.concatenated_string += new_string
        return self.concatenated_string
s = StringConcatenator()
print(s.add_string("Mozammil"))