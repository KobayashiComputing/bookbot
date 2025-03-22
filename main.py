import sys
from stats import word_count, char_count, get_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_stats(file_contents):
    # print(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(word_count(file_contents), "words found in the document\n")
    # print(char_count(file_contents))
    char_freq = char_count(file_contents)
    for char in char_freq:
        print(f"The '{char}' character was found {char_freq[char]} times")
    print("--- End report ---")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # book_text = get_book_text("books/frankenstein.txt")
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    # print(char_count(book_text))
    # print(get_list(char_count(book_text)))
    counts_list = get_list(char_count(book_text))
    for c in counts_list:
        print(f"{c['char']}: {c['count']}")
    print("============= END ===============\n")


main()