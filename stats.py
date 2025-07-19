def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_char_dict(doc):
    doc = doc.lower()
    char_dict = dict()
    for char in doc:
        try: char_dict[char] += 1
        except: char_dict[char] = 1
    
    return char_dict

def count_words(doc):
    return len(doc.split())

def get_sorted_list(char_dict):
    lst = []
    for char, num in char_dict.items():
        new_dict = {"char":char, "num":num}
        lst.append(new_dict)
    lst.sort(key=lambda dct: dct["num"], reverse = True)

    return lst

def format_sorted_list(lst):
    s = ""
    for dct in lst:
        char, num = dct["char"], dct["num"]
        if char.isalpha():
            s += f"\n{char}: {num}"
    return s