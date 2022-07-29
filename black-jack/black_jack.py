def value_of_card(card):
    if card in 'JQK':
        return 10
    if card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value == card_two_value:
        return (card_one, card_two)
    if card_one_value > card_two_value:
        return card_one
    else:
        return card_two


def value_of_ace(card_one, card_two):
    if card_one != 'A' and card_two != 'A':
        current_score = value_of_card(card_one) + value_of_card(card_two)
    else:
        return 1

    if current_score + 11 <= 21:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    current_score = check_card_value(card_one) + check_card_value(card_two)
    return bool(current_score == 21)


def check_card_value(card):
    if card in 'JQK':
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)


def can_split_pairs(card_one, card_two):
    return bool(check_card_value(card_one) == check_card_value(card_two))


def can_double_down(card_one, card_two):
    current_score = value_of_card(card_one) + value_of_card(card_two)
    return bool(current_score >= 9 and current_score <= 11)