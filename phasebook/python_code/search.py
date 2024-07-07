# File: search.py

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
    
    return results
