import random


with open('words.txt', 'r') as f:
    bad_char = [".","'", "-", "1", "2", "3", "4", "5", "6", "7","8", "9"]
    words1 = f.read().splitlines()
    valid_words = [x for x in words1 if all(j not in x for j in bad_char)]
    words = []
    [words.append(x) for x in valid_words if len(x) < 9]
    word = random.choice(words)
    
    
                   

