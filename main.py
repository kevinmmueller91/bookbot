from stats import get_words
from stats import get_char_occurrence
from stats import sort_list
import sys

def get_book_text(filepath): 
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
def print_report(filepath, words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    words = get_words(book)
    print(f"{words} words found in the document.")
    char_counts = get_char_occurrence(book)
    sorted_list = sort_list(char_counts)
    print_report(filepath, words, sorted_list)

main()