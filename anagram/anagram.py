def find_anagrams(word, candidates):
    return [contender for contender in candidates if is_anagram(word, contender)]

def is_anagram(word, contender):
    w = word.casefold()
    c = contender.casefold()
    return bool(sorted(w) == sorted(c) and c != w)