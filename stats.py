# A file that contains functions for analyzing the text

def count_words(book_content):
    words = book_content.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")