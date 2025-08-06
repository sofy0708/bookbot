import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_filepath):
    with open(book_filepath) as f:
        book_content = f.read()
        return book_content

from stats import count_words

from stats import count_characters

from stats import sort_characters

def main():
    print("============ BOOKBOT ============")

    book_path = sys.argv[1]

    book_content = get_book_text(book_path)

    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")

    num_words = count_words(book_content)

    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    num_per_characters = count_characters(book_content)

    sorted_characters = sort_characters(num_per_characters)

    for dictionary in sorted_characters:
        if dictionary["char"].isalpha() == True:
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    
    print("============= END ===============")
    


main()