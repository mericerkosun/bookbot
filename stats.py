def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def number_of_words(text):
    text_array = text.split()
    counter = 0

    for i in text_array:
        counter += 1

    return f"Found {counter} total words"

def number_of_chars(text):
    char_dict = {}

    for i in text:
        lower_i = i.lower()
        if lower_i not in char_dict:
            char_dict[lower_i] = 1
        else:
            char_dict[lower_i] += 1

    return char_dict

def sort_on(items):
    return items["num"]

def report(char_counts):

    list_of_dicts = []

    for i in char_counts:
        temp_dict = {"char":i,"num":char_counts[i]}
        list_of_dicts.append(temp_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts