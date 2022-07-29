def get_rounds(number):
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return bool(number in rounds)


def card_average(hand):
    hand_total = 0
    card_count = 0
    for card in hand:
        hand_total += card
        card_count += 1
    return hand_total / card_count


def approx_average_is_average(hand):
    average = card_average(hand)
    approx_average = (hand[0] + hand[-1]) / 2
    return bool(average == approx_average or average == hand[len(hand) // 2])


def average_even_is_average_odd(hand):
    even = []
    odd = []
    for i in range(0, len(hand)):
        if i % 2 == 0:
            even.append(hand[i])
        else: 
            odd.append(hand[i])
    return bool(card_average(even) == card_average(odd))


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
        return hand
    return hand