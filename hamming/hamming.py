def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')
    errors = (a != b for a, b in zip(strand_a, strand_b))
    return sum(errors)