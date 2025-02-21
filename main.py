def main():
    book_path = "books/frankenstein.txt"
    book_text = open_book(book_path)
    num_words = count_words(book_text)
    print(book_text)
    print(f"This book has {num_words} words.")
    
    #with open("books/frankenstein.txt") as f:
    #    file_contents = f.read()
    #    print(file_contents)
    #    print(count_words(file_contents))

def open_book(path):
    with open(path) as f:
        book_text = f.read()
        return book_text

def count_words(text):
    words = text.split()
    return len(words)

main()