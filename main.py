def main():
    book_path = "books/frankenstein.txt"
    book_text = open_book(book_path)
    num_words = count_words(book_text)
    char_frequency = calc_char_frequency(book_text)
    print(book_text)
    print(f"This book has {num_words} words.")
    print(char_frequency)

def open_book(path):
    with open(path) as f:
        book_text = f.read()
        return book_text

def count_words(text):
    words = text.split()
    return len(words)

def calc_char_frequency(text):
    dict = {}
    for char in text.lower():
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

main()