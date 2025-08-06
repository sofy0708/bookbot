# A file that contains functions for analyzing the text

def count_words(book_content):
    words = book_content.split()
    num_words = len(words)
    return num_words
    
def count_characters(book_content):
    lowercase_content = book_content.lower()
    num_per_characters = {}
    for char in lowercase_content:
        num_per_characters[char] = num_per_characters.get(char, 0) + 1
    return num_per_characters

