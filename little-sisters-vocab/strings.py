    # [:n] starts the slice at the beginning of the list, ends at index n
    # [n:] extends the slice from the first index n, to the end of the list
    # [:] copies the entire list
    # .rstrip() removes white space from text


def add_prefix_un(word):
    return 'un' + word


def make_word_groups(vocab_words):
    pre = vocab_words[0]
    return pre + ' :: ' + ' :: '.join(pre + w for w in vocab_words[1:])


def remove_suffix_ness(word):
    root = word[:-4]
    if root[-1] == 'i':
        return root[:-1] + 'y'
         
    return root


def adjective_to_verb(sentence, index):
    return sentence.split()[index].rstrip(' .') + 'en'
