from stats import count_words, calc_char_frequency, sort_chars_by_freq

def main():
    book_path = "books/frankenstein.txt"
    book_text = open_book(book_path)
    num_words = count_words(book_text)
    char_frequency = calc_char_frequency(book_text)
    # print(book_text)
    #print(f"{num_words} words found in the document")
    #print(char_frequency)
    # print(list(char_frequency.items()).sort(reverse=True, key=sort_on))
    #print(list(char_frequency.items()))
    #print(sort_chars_by_freq(char_frequency))
    #print(sort_chars_by_freq(char_frequency))
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
        #print(f"The '{char_data[0]}' character was found {char_data[1]} times")
    print("============= END ===============")


main()