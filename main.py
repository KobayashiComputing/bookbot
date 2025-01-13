def word_count(book_contents):
    words = book_contents.split()

    return len(words)


with open("books/frankenstein.txt") as f:
    file_contents = f.read()

# print(file_contents)
print(word_count(file_contents))
