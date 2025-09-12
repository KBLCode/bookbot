def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_count = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in character_count:
            character_count[lowercase_char] += 1
        else:
            character_count[lowercase_char] = 1
    return character_count


def get_num(dict_item):
    return dict_item["num"]

def sort_characters(character_count):
    sorted = []
    for char, num in character_count.items():
        sorted.append({"char": char, "num": num})
    
    sorted.sort(key=get_num, reverse=True)
    return sorted