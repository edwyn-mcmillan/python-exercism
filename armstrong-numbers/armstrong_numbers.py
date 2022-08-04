def is_armstrong_number(number):
    digits = len(str(number))
    return bool(sum([int(d)**digits for d in str(number)]) == number)

