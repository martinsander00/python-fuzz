import random

def increase_integer(input_str):
    try:
        num = int(input_str)
        incremented = str(num + 1)
        return incremented
    except ValueError:
        return input_str

def reverse_string(input_str):
    return input_str[::-1]

def mutate(input_str):
    # Define probabilities for each function
    probability_increase = 0.8  # % chance to increase integer
    probability_reverse = 0.2   # % chance to reverse string

    # Generate a random number between 0 and 1
    rand_num = random.random()

    # Apply mutations based on probabilities
    if rand_num < probability_increase:
        input_str = increase_integer(input_str)
    elif rand_num < probability_increase + probability_reverse:
        input_str = reverse_string(input_str)

    return input_str