import atm_fun


# ----USER LIST-----
def user_list():
    users = []
    m = []

    g = open("user.txt", "r")
    x1 = list(g)
    for c in x1:
        split1 = c.split("\n")
        split1.pop(-1)
        m.append(split1)

    for o1 in m:
        for l1 in o1:
            a1 = l1.split("\t")
            users.append(a1)
        users[-1].pop(-1)

    g.close()
    return users


# ----ADMIN LIST------
def admin_list():
    admin = []
    m = []

    g = open("admin.txt", "r")
    x1 = list(g)
    for c in x1:
        split1 = c.split("\n")
        split1.pop(-1)
        m.append(split1)

    for e in m:
        for x1 in e:
            a1 = x1.split("\t")
            admin.append(a1)
        admin[-1].pop(-1)

    g.close()
    return admin


# ---BAN LIST----
def buser_list():
    busers = []
    y = []

    b = open("bannedUser.txt", "r")
    c = list(b)
    for p in c:
        split1 = p.split("\n")
        split1.pop(-1)
        y.append(split1)

    for p in y:
        for q in p:
            y = q.split("\t")
            busers.append(y)

    b.close()
    return busers


a = 1
profile = 1
while profile != "admin" and profile != "user":
    profile = input("Do you want to login as ADMIN or USER: ").lower()

    # ---------USER------------

    if profile == "user":
        # ----ACCOUNT INFO--------

        # ----USER LIST-----
        name = input("Please Enter your Username: ")
        pin = input("Please enter your 4 digit pin: ")

        j = user_list()

        # --BAN LIST----

        k = buser_list()

        # ------ACCOUNT CHECKING-------
        out = 0
        for line in j:
            if name == line[2]:
                if pin == line[3]:
                    out = 1
                    break
                else:
                    i = 0
                    while i < 2:
                        print("Pin is incorrect")
                        pin = input("Please enter your 4 digit pin: ")
                        if pin == line[3]:
                            out = 1
                            break
                        i += 1
                        if i == 2:
                            print("Please try again later")
                            break
                    break
            else:
                out = 0

        for line1 in k:
            if name == line1[2]:
                if pin == line1[3]:
                    out = 2
                    break

        # ------TRANSACTIONS----------
        if out == 1:
            trans = "y"
            while trans == "y":

                option = "a"
                while option not in "1234567":
                    print("""
                    Please select an option:
                    1. Balance Inquiry
                    2. Deposit
                    3. Transfer
                    4. Change Pin
                    5. Debt
                    6. Debt Inquiry
                    7. Cancel
                        """)
                    option = input("Choice: ")

                    # ---------OPTION 1-------
                    if option == "1":
                        atm_fun.balance(name, pin)

                    # --------OPTION 2---------
                    elif option == "2":
                        atm_fun.deposit(name, pin)

                    # --------OPTION 3-------
                    elif option == "3":
                        atm_fun.transfer(name, pin)

                    # --------OPTION 4-------
                    elif option == "4":
                        pin = atm_fun.chngpin(name, pin)

                    # --------OPTION 5-------
                    elif option == "5":
                        atm_fun.debt(name, pin)

                    # --------OPTION 6-------
                    elif option == "6":
                        atm_fun.debt_i(name, pin)

                    # --------OPTION 7--------
                    elif option == "7":
                        break

                    else:
                        print("Please select a valid option")

                if option == "7":
                    break
                trans = input("Do you want to make another transaction? (Y/N): ").lower()
                while trans != "y" and trans != "n":
                    print("Please select a valid option")
                    trans = input("Do you want to make another transaction? (Y/N): ").lower()


        elif out == 0:
            print("Account haven't found.")

        elif out == 2:
            print("Your account has been banned by an Admin.")


    # --------------ADMIN------------------

    elif profile == "admin":

        # -----ACCOUNT INFO---------

        j = admin_list()

        email = input("Please enter your Username: ")
        pin = input("Please enter your Pin: ")

        # -------ACCOUNT CHECKING------
        out = 0
        for line in j:
            if email == line[1]:
                if pin == line[2]:
                    out = 1
                    break
                else:
                    i = 0
                    while i < 2:
                        print("Pin is incorrect")
                        pin = input("Please enter your 4 digit pin: ")
                        if pin == line[2]:
                            out = 1
                            break
                        i += 1
                        if i == 2:
                            print("Please try again later")
                            break
                    break
            else:
                out = 0

        # -------WORK-----------
        if out == 1:
            trans = "y"
            while trans == "y":
                option = "a"
                o = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
                while option not in o:
                    print("""
                    Please select an option:
                    1. Add an Admin
                    2. Remove an Admin
                    3. Add a User
                    4. Remove a User
                    5. Check Admins Info
                    6. Check Users Info
                    7. Change Pin
                    8. Ban a User
                    9. Unban a User
                   10. Banned Users Info
                   11. Cancel
                        """)
                    option = input("Choice: ")

                    # ---------OPTION 1-------
                    if option == "1":
                        atm_fun.a_admin(email, pin)

                    # ---------OPTION 2-------
                    elif option == "2":
                        atm_fun.r_admin(email, pin)

                    # ---------OPTION 3--------
                    elif option == "3":
                        atm_fun.a_user(email, pin)

                    # ---------OPTION 4--------
                    elif option == "4":
                        atm_fun.r_user()

                    # ---------OPTION 5-------
                    elif option == "5":
                        atm_fun.admin_data(email, pin)

                    # ---------OPTION 6-------
                    elif option == "6":
                        atm_fun.user_data()

                    # --------OPTION 7--------
                    elif option == "7":
                        atm_fun.changepin(email, pin)

                    # --------OPTION 8--------
                    elif option == "8":
                        atm_fun.ban_user()

                    # -------OPTION 9--------
                    elif option == "9":
                        atm_fun.unban_user()

                    # -------OPTION 10--------
                    elif option == "10":
                        atm_fun.ban_user_data()

                    elif option == "11":
                        break

                    else:
                        print("Please select a valid option")

                if option == "11":
                    break
                trans = input("Do you want to do something else? (Y/N): ").lower()
                while trans not in "yn":
                    print("Please select a valid option")
                    trans = input("Do you want to do something else? (Y/N): ").lower()


        elif out == 0:
            print("Admin ID not found")

    else:
        print("Please specify your account")
