from stats import *
import sys

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("-------- Character Count -------", end = "")
    char_dict = get_char_dict(text)
    sorted_list = get_sorted_list(char_dict)
    print(format_sorted_list(sorted_list))

    print("============= END ===============")

main()