def equilateral(sides):
    a, b, c = sorted(sides)
    return a != 0 and a == c

def isosceles(sides):
    a, b, c = sorted(sides)
    return a != 0 and c < a + b and b in (a, c)

def scalene(sides):
    a, b, c = sorted(sides)
    return a != b != c and c < a + b
