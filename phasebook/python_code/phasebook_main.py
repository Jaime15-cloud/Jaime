# File: phasebook_main.py

from update_pip import update_pip
from match import is_match
from search import search_users

# Mocked data for testing search functionality
USERS = [
    {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"},
    {"id": "2", "name": "Jane Doe", "age": 30, "occupation": "Engineer"},
    {"id": "3", "name": "Joe Doe", "age": 25, "occupation": "Designer"},
    {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"},
    {"id": "5", "name": "Jane Smith", "age": 31, "occupation": "Manager"},
    {"id": "6", "name": "Joe Smith", "age": 24, "occupation": "Designer"}
]

if __name__ == "__main__":
    # Update pip
    update_pip()

    # Example usage of is_match function
    fave_numbers_1 = [1, 2, 3, 4, 5]
    fave_numbers_2 = [2, 3]
    print(is_match(fave_numbers_1, fave_numbers_2))

    # Example usage of search_users function
    search_results = search_users(USERS, id="2", name="John")
    print(search_results)

    search_results = search_users(USERS, age="28")
    print(search_results)

    search_results = search_users(USERS, id="5", name="Joe", age="30", occupation="Arc")
    print(search_results)
