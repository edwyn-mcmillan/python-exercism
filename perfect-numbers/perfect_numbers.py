def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors = list()
    for item in range(1, number):
        if number % item == 0:
            factors.append(item)
            
    if sum(factors) == number:
        return "perfect"
    if sum(factors) > number:
        return "abundant"
    if sum(factors) < number:
        return "deficient"