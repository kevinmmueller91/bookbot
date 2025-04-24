def get_words(book_text):
    word_list = book_text.split()
    num_words = len(word_list)
    return num_words

def get_char_occurrence(book_text):
    lower_book_text = book_text.lower()
    char_count = {}
    for char in lower_book_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def dict_nums(dictionary):
    return dictionary["num"]

def sort_list(dictionary):
    sorted_list = []
    for char in dictionary:
        sorted_list.append({"char": char, "num": dictionary[char]})
        sorted_list.sort(reverse=True, key=dict_nums)
    return sorted_list