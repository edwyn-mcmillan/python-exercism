def sum_of_multiples(limit, multiples):
    total = set()
    for multiple in multiples:
        for num in range(limit):
            if multiple == 0:
                break
            if num % multiple == 0:
                total.add(num)
    return sum(total)
