from string import ascii_lowercase

def is_pangram(sentence):
    sentence_set = set(sentence.lower())
    alpha_set = set(ascii_lowercase)
    return bool(alpha_set.difference(sentence_set) == set())