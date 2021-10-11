def login(database, username, password):
    if username in database.keys() and password == database[username]:
        print("Welcome here!!!," + "you are logged in as " + username)
        return username
    elif username in database.keys() and password != database[username]:
        print("Login failed...mismatched password credentials")
        return " "
    else:
        print("Login failed...Username was not found in the database: Please Register")
        return " "

def register(database, username):
    if username in database.keys():
        print("Username already been registered.")
        return " "
    else:
        print("username, " + username + " has been registered")
        return " "
