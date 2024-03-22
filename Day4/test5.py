def sort_words():
    input_string = input("Enter a comma-separated sequence of words: ")
    words = [word.strip() for word in input_string.split(',')]
    sorted_words = sorted(words)
    output_string = ','.join(sorted_words)
    print("Sorted words:", output_string)

# Test the function
sort_words()
