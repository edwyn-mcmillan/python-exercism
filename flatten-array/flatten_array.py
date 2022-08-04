def flatten(iterable):
    result = list()
    for item in iterable:
        if item == None:
            continue
        if isinstance(item, list):
            result += flatten(item)
        else:
            result.append(item)
    return result
