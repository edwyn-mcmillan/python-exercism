class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        digit_list = list(self.card_num[::-1].replace(" ", ""))
        for char in digit_list:
            if not char.isdigit():
                return False
            if len(digit_list) <= 1:
                return False

        digit_list = list(map(int, digit_list))
        for i in range(1, len(digit_list), 2):
            digit_list[i] = digit_list[i] * 2
            if digit_list[i] > 9:
                digit_list[i] = digit_list[i] - 9
    
        return bool(sum(digit_list) % 10 == 0)