def capitalize_title(title):
    temp = title.split()
    return ' '.join(w.capitalize() for w in temp)


def check_sentence_ending(sentence):
    return bool(sentence.endswith('.'))


def clean_up_spacing(sentence):
    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    return sentence.replace(old_word, new_word)
