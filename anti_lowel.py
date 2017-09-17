def anti_vowel(text):
    new_str = ''
    for char in text:
        for symbol in "aeiouAEIO":
            if char==symbol:
                char=""
        new_str += char
    return new_str
    




print anti_vowel("Hey You!")