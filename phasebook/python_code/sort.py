# File: sort.py

# Define USERS data (mocked data for testing)
USERS = [
    {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"},
    {"id": "2", "name": "Jane Doe", "age": 30, "occupation": "Engineer"},
    {"id": "3", "name": "Joe Doe", "age": 25, "occupation": "Designer"},
    {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"},
    {"id": "5", "name": "Jane Smith", "age": 31, "occupation": "Manager"},
    {"id": "6", "name": "Joe Smith", "age": 24, "occupation": "Designer"}
]

# Function to search and sort users based on criteria
def search_users(users, id=None, name=None, age=None, occupation=None):
    results = []

    for user in users:
        match = True
        
        if id and user['id'] != id:
            match = False
        
        if name and name.lower() not in user['name'].lower():
            match = False
        
        if age is not None:
            user_age = user['age']
            if not (int(age) - 1 <= user_age <= int(age) + 1):
                match = False
        
        if occupation and occupation.lower() not in user['occupation'].lower():
            match = False
        
        if match:
            results.append(user)
    
    # Sort results based on priority: id > name > age > occupation
    results.sort(key=lambda x: (
        x['id'] != id,  # Sort by id match first (True/False)
        x['name'].lower() == name.lower(),  # Then by name match (True/False)
        abs(x['age'] - int(age)) if age is not None else float('inf'),  # Then by age proximity
        x['occupation'].lower().find(occupation.lower()) != -1 if occupation else False  # Then by occupation match
    ), reverse=True)
    
    return results

# Example usage of search_users function with adjusted criteria
if __name__ == "__main__":
    search_results = search_users(USERS, id="5", name="Jane", age="31", occupation="Manager")
    print(search_results)


