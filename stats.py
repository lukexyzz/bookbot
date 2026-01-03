
def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    counts = {}
    for i in text.lower():
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    return counts   

def sort_on(items):
    return items["num"]


def chars_dict_to_sorted_list(char_dict):
    dict_list = []
    for char, count in char_dict.items():
        dict_list.append({
            "char": char,
            "num": count,
        })
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


