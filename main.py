def get_book_text(book_filepath):
    with open(book_filepath) as f:
        book_content = f.read()
        return book_content

from stats import count_words

def main():
    book_content = get_book_text("books/frankenstein.txt")
    count_words(book_content)

main()