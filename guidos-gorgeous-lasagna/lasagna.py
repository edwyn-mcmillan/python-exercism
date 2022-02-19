EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_time):
    """Returns time left remaining"""
    return EXPECTED_BAKE_TIME - elapsed_time

def preparation_time_in_minutes(layer_num):
    """2 minutes of preparation for each layer"""
    return layer_num * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Returns the current amount of time spent preparing the lasagna"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
