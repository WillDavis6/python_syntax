words = ["hello", "hey", "goodbye", "yo", "yes"]
starters = ["y", "h"]
def print_upper_words(list_of_words, must_contain_letter):
    for word in list_of_words:
        upper_word = word.upper()
        for letters in must_contain_letter:
            if word[0] == letters:
                print(upper_word)

print_upper_words(words, starters)