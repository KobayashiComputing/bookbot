def word_count(book_contents):
    words = book_contents.split()
    return len(words)

def char_count(book_contents):
    letter_counts = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
        "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
    }
    lowercase_contents = book_contents.lower()
    for letter in lowercase_contents:
        if letter in letter_counts:
            current_count = letter_counts[letter]
            letter_counts[letter] = current_count + 1
    
    return dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))

def get_list(char_dict):
    retVal = []
    for d in char_dict:
        retVal.append({"char": d, "count": char_dict[d]})
    return retVal