import random
import string

def generate(length, include_special_symbols, keyword=None):
    characters = string.ascii_letters + string.digits
    if include_special_symbols:
        characters += "!@#$%^&*()-_+=<>,.?/:;{}[]|\\~"
    
    if keyword:
        keyword_length = len(keyword)
        if keyword_length >= length:
            return keyword[:length]
        else:
            remaining_length = length - keyword_length
            start_position = random.randint(0, remaining_length)
            end_position = start_position + keyword_length
            prefix = ''.join(random.choice(characters) for _ in range(start_position))
            suffix = ''.join(random.choice(characters) for _ in range(end_position, length))
            return prefix + keyword + suffix
    else:
        return ''.join(random.choice(characters) for _ in range(length))
'''
#TestCase
l = 10
s = True
k = "_HIHS_"
x = generate(l, s, k)
print()
print(x)
print()
'''