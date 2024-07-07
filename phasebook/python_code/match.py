# File: match.py

def is_match(fave_numbers_1, fave_numbers_2):
    # Optimized matching logic here
    return set(fave_numbers_2).issubset(set(fave_numbers_1))
