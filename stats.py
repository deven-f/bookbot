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