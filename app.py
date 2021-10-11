from donations_pkg.homepage import show_homepage, donate, show_donations
#from donations_pkg.user import login,register
from donations_pkg.user import login
from donations_pkg.user import register

database = {"admin": "password123"}
donations = []
authorized_user = " "
#while True:
show_homepage()
if authorized_user == " ":
    print("You must be logged in to donate.")
    username = input("Enter username to login:")
    password = input("Enter password to login:")
else:
    print("Logged in as:", authorized_user)

chooseoption = int(input("choose an option:"))
if chooseoption == 1:
    username = input("Enter your Username:")
    password = input("Enter your Password:")
    #print("TODO: Write Login Functionality")
    authorized_user = login(database, username, password)
elif chooseoption == 2:
    username = input("Enter your Username:")
    password = input("Enter your Password:")
    #print("TODO: Write Register Functionality")
    authorized_user = register(database, username)
    if authorized_user != " ":
        database[username] = password
elif chooseoption == 3:
    #print("TODO: Write Donate Functionality")
    username = input("Enter your Username:")
    password = input("Enter your Password:")
    authorized_user = donate(username)
    if authorized_user == " ":
        print("You are not logged in")
    else:
        donation = donate(authorized_user)
        donations.append(donation)
elif chooseoption == 4:
    show_donations(donations)
    #print("TODO: Write Show Donations Functionality")
elif chooseoption == 5:
    print("You asked to Exit; GOODBYE!!!")
    quit()

