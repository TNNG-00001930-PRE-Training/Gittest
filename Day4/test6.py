def remove_duplicates_and_sort():
    input_string = input("Enter a whitespace-separated sequence of words: ")
    words = input_string.split()
    unique_words = sorted(set(words))
    output_string = ' '.join(unique_words)
    print("Sorted words after removing duplicates:", output_string)

# Test the function
remove_duplicates_and_sort()
