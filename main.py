import sys
from stats import get_num_words, count_characters, sort_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents  

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    num_words = get_num_words(file_contents)
    character_count = count_characters(file_contents)
    sorted_characters = sort_characters(character_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"Found {num_words} total words")
    print()

    for char_data in sorted_characters:
        if char_data["char"].isalpha():
          print(f"{char_data['char']}: {char_data['num']}")

    print("--- End report ---")
main()