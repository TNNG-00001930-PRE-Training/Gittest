def find_even_numbers():
    even_numbers = []
    for num in range(1000, 3001):
        all_even = True
        for digit in str(num):
            if int(digit) % 2 != 0:
                all_even = False
                break
        if all_even:
            even_numbers.append(str(num))
    print("Numbers with all even digits between 1000 and 3000 (inclusive):")
    print(','.join(even_numbers))

# Test the function
find_even_numbers()
