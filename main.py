def get_book_text(book_filepath):
    with open(book_filepath) as f:
        book_content = f.read()
        return book_content

from stats import count_words

from stats import count_characters

def main():
    book_content = get_book_text("books/frankenstein.txt")

    num_words = count_words(book_content)
    print(f"{num_words} words found in the document")
    
    num_per_characters = count_characters(book_content)
    print(num_per_characters)

main()