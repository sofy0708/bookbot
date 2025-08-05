def get_book_text(book_filepath):
    with open(book_filepath) as f:
        book_content = f.read()
    return book_content

def main():
    book_content = get_book_text("books/frankenstein.txt")
    print(book_content)
    
main()
