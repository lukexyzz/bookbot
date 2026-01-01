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
