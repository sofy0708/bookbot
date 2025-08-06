def get_book_text(book_filepath):
    with open(book_filepath) as f:
        book_content = f.read()
        return book_content

def count_words(book_content):
    words = book_content.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def main():
    book_content = get_book_text("books/frankenstein.txt")
    count_words(book_content)

main()