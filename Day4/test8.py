def count_upper_lower(sentence):
    upper_count = 0
    lower_count = 0

    for char in sentence:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print("UPPER CASE:", upper_count)
    print("LOWER CASE:", lower_count)

# Test the function
sentence = input("Enter a sentence: ")
count_upper_lower(sentence)
