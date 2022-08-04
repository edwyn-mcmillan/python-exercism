def is_isogram(string):
    string = string.replace(' ', '').replace('-', '').lower()
    return bool(len(set(string)) == len(string))
