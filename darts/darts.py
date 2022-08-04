from math import sqrt

scores = [(1, 10),(5, 5),(10, 1)]

def score(x, y):
    distance = sqrt(x * x + y * y)
    for radius, score in scores:
        if distance <= radius:
            return score
    return 0

