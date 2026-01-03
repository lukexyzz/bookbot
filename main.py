
import sys
from stats import get_num_words, character_count, chars_dict_to_sorted_list


def main():

    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = sys.argv[1]
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    characters = character_count(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    sorted_chars = chars_dict_to_sorted_list(characters)

    for item in sorted_chars:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    


def get_book_text(path):
    with open(path) as f:
        return f.read()




main()