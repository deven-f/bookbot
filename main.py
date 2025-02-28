import sys
from stats import count_words, calc_char_frequency, sort_chars_by_freq

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    book_path = sys.argv[1]
    book_text = open_book(book_path)
    num_words = count_words(book_text)
    char_frequency = calc_char_frequency(book_text)   
     
    create_report(sort_chars_by_freq(char_frequency), book_path, num_words)

def open_book(path):
    with open(path) as f:
        book_text = f.read()
        return book_text

def create_report(sorted_list, book_path, num_words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        char_data = list(i.values())
        print(f"{char_data[0]}: {char_data[1]}")
    print("============= END ===============")


main()