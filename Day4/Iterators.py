class Vector:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.number = 1
        return self
    
    def __next__(self):
        if self.max == self.number:
            raise StopIteration
        else:
            number = self.number
            self.number += 1
            return number
    
num = Vector(4)
i = iter(num)
print(" # Calling next() one by one: ")
print(next(i))
print(next(i))
print(next(i))

# Call next method in a loop
print("# Calling next() in a loop")
for i in num:
    print(i)

print(num)
    