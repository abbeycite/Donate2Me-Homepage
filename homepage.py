def show_homepage():
    print("")
    print("        === DonateMe HomePage ===         ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register       |")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations |")
    print("------------------------------------------")
    print("|              5.    Exit                |")
    print("------------------------------------------")

def donate(username):
    donation_amt = float(input("Enter amount to donate:"))
    print("Thank you for your donation " + username)
    donation = username + " has donated " + str(donation_amt)
    return donation
def show_donations(donations):
    print("\n--- All Donations ---")
    if len(donations) == 0:
        print("Currently, there are no donations." )
    else:
        for x in donations:
            print(x)
