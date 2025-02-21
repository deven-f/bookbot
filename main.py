def main():
    book_path = "books/frankenstein.txt"
    book_text = open_book(book_path)
    num_words = count_words(book_text)
    char_frequency = calc_char_frequency(book_text)
    # print(book_text)
    # print(f"This book has {num_words} words.")
    # print(char_frequency)
    # print(list(char_frequency.items()).sort(reverse=True, key=sort_on))
    #print(list(char_frequency.items()))
    #print(sort_chars_by_freq(char_frequency))
    #print(sort_chars_by_freq(char_frequency))
    create_report(sort_chars_by_freq(char_frequency), book_path, num_words)

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

def sort_chars_by_freq(dictionary):
    lst = []
    for key, value in dictionary.items():
        if key.isalpha():
            lst.append({"letter": key, "num": value})
    
    lst.sort(reverse=True, key=sort_on)
    return lst

def sort_on(dict):
    return dict["num"]

def create_report(sorted_list, book_path, num_words):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in this document \n \n")
    for i in sorted_list:
        char_data = list(i.values())
        print(f"The '{char_data[0]}' character was found {char_data[1]} times")
    print("--- End report ---")


main()