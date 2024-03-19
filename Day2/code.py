string = input("Enter the text: ")
def even_len_words(string):
    list_of_words = string.split(" ")
    for word in list_of_words:
        if len(word)%2 == 0:
            print(word)
print(even_len_words(string))