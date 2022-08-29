def commands(binary_str):
    action = ["jump", "close your eyes", "double blink", "wink"]
    result = list()
    for num in range(4, 0, -1):
        if binary_str[num] == "1":
            result.append(action[num - 1])
    if binary_str[0] == "1":
        result.reverse()
    return result