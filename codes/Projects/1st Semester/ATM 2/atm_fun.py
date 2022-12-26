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


#              -----------------USER------------------------


# -------------PIN---------------
def chngpin(username, pin):
    updatedlist = ""
    temporarylist = user_list()

    for row in temporarylist:
        if row[2] == username and row[3] == pin:
            updatedlist = row

            npin = 0
            zpin = 1
            while npin != zpin or npin == pin or len(npin) != 4:
                npin = input("Enter new pin: ")
                zpin = input("Re-Enter new pin: ")
                if npin != zpin:
                    print("New pins does not match")
                if npin == pin:
                    print("You are entering the old pin.")
                if len(npin) > 4:
                    print("Pin can't be greater than 4 digits")
                elif len(npin) < 4:
                    print("Pin can't be less than 4 digits")

            updatedlist[3] = npin
            pin = npin

    for index, row in enumerate(temporarylist):
        for field in row:
            if field == updatedlist[0]:
                temporarylist[index] = updatedlist

    f = open("user.txt", "w")
    for e in temporarylist:
        for e1 in e:
            if e1 == e[-1] and e1 == "":
                continue
            else:
                f.write(e1 + "\t")
        f.write("\n")
    f.close()
    print("Pin has been changed")
    return pin


# -----------DEBT-----------------

def debt(username, pin):
    updatedlist = ""
    temporarylist = user_list()

    for row in temporarylist:
        if row[2] == username and row[3] == pin:
            updatedlist = row

    print("Current Balance: ", updatedlist[4], "Rs.")
    print("Current Debt: ", updatedlist[5], "Rs.")

    crd = float(input("Enter the debt amount: "))
    if crd <= (float(updatedlist[4]) / 100 * 20) and (float(updatedlist[5]) < float(updatedlist[4]) / 100 * 5):
        bal = float(updatedlist[4]) + crd
        updatedlist[4] = str(bal)
        old_crd = float(updatedlist[5])
        new_crd = crd + old_crd
        updatedlist[5] = str(new_crd)
        print("Debt have been deposited in your account.")
        print("Net Balance: ", updatedlist[4], "Rs.")
        print("Net Debt: ", updatedlist[5], "Rs.")

    else:
        print("You are not eligible to get Debt")

    for index, row in enumerate(temporarylist):
        for field in row:
            if field == updatedlist[0]:
                temporarylist[index] = updatedlist

    f = open("user.txt", "w")
    for e in temporarylist:
        for e1 in e:
            if e1 == e[-1] and e1 == "":
                continue
            else:
                f.write(e1 + "\t")
        f.write("\n")
    f.close()


# ----------TRANSFER---------------

def transfer(username, pin):
    updatedlist = []
    temporarylist = user_list()

    for row in temporarylist:
        if row[2] == username and row[3] == pin:
            updatedlist.append(row)

    print("""
        OPTIONS
        1. Pay Your Debt
        2. Deposit to other account
        """)

    option = input("Your Choice: ")
    while option not in "12":
        print("Please select a valid option")
        option = input("Your Choice: ")

    print()
    print("Your Current Balance: ", updatedlist[0][4], "Rs.")
    if option == "1":
        print("Your Current Debt: ", updatedlist[0][5], "Rs.")
    print()

    print("""
        Select the amount you want to transfer (in Rs.):
        1. 5000
        2. 10000
        3. 20000
        4. Other Amount
        """)
    opt = input("Your Choice: ")
    while opt not in "1234":
        print("Please select a valid option")
        opt = input("Your Choice: ")

    amount = 0
    if opt == "1":
        amount = 5000
    elif opt == "2":
        amount = 10000
    elif opt == "3":
        amount = 20000
    elif opt == "4":
        amount = float(input("Enter the amount: "))

    a = 1
    if amount < float(updatedlist[0][4]):
        bal = float(updatedlist[0][4]) - float(amount)
        updatedlist[0][4] = str(bal)

        if option == "1":
            d = float(updatedlist[0][5]) - float(amount)
            if d < 0:
                bal += abs(d)
                d = 0
                updatedlist[0][4] = str(bal)

            updatedlist[0][5] = str(d)
            print("Your transaction is successful")
            print("Net Debt: ", str(d), "Rs.")
            print("Net Balance: ", updatedlist[0][4], "Rs.")

        elif option == "2":
            opt = input("In Same Bank -OR- Different Bank (S/D): ").lower()

            while opt != "s" and opt != "d":
                print("Please select a valid option")
                opt = input("In Same Bank -OR- Different Bank (S/D): ").lower()

            o_name = input("Account Holder Full Name: ")
            o_account_no = input("Enter the Account Number: ")

            a = 0
            if opt == "s":
                for rows in temporarylist:
                    if rows[1] == o_name and rows[0] == o_account_no:
                        updatedlist.append(rows)
                        a = 0
                        old_bal = updatedlist[1][4]
                        new_bal = float(old_bal) + float(amount)
                        updatedlist[1][4] = str(new_bal)
                        break

                    else:
                        a = 1

            elif opt == "d":
                a = 0
                pass

            else:
                print("Please select a valid option")

            if a == 0:
                print("Your transaction is successful")

            elif a == 1:
                print("Account haven't found")
                updatedlist[0][4] = str(float(updatedlist[0][4]) + float(amount))

            print("Net Balance: ", updatedlist[0][4], "Rs.")

        else:
            print("Please select a valid option")

    else:
        print("Insufficient Balance")

    for index, row in enumerate(temporarylist):
        for field in row:
            if field == updatedlist[0]:
                temporarylist[index] = updatedlist[0]
            if option == "2" and opt == "s" and a == 0:
                if field == updatedlist[1]:
                    temporarylist[index] = updatedlist[1]
                    print("Your transaction has been successful.")

    f = open("user.txt", "w")
    for e in temporarylist:
        for e1 in e:
            if e1 == e[-1] and e1 == "":
                continue
            else:
                f.write(e1 + "\t")
        f.write("\n")
    f.close()


# ----------BALANCE INQUIRY----------------

def balance(username, pin):
    updatedlist = ""
    reader = user_list()

    for row in reader:
        if row[2] == username and row[3] == pin:
            updatedlist = row

    bal = updatedlist[4]
    print("Net Balance: ", bal, "Rs.")


# ----------DEBT INQUIRY-------------

def debt_i(username, pin):
    updatedlist = ""
    reader = user_list()
    for row in reader:
        if row[2] == username and row[3] == pin:
            updatedlist = row

    d = updatedlist[5]
    print("Net Debt: ", d, "Rs.")


# -------DEPOSIT----------

def deposit(username, pin):
    updatedlist = ""
    temporarylist = user_list()

    for row in temporarylist:
        if row[2] == username and row[3] == pin:
            updatedlist = row

    print("""
    Select the amount you want to deposit (in Rs.):
    1. 5000
    2. 10000
    3. 20000
    4. Other Amount
    """)
    opt = int(input("Your Choice: "))
    amount = 0
    if opt == 1:
        amount = 5000
    elif opt == 2:
        amount = 10000
    elif opt == 3:
        amount = 20000
    elif opt == 4:
        amount = float(input("Enter the amount: "))

    bal = float(updatedlist[4]) + float(amount)
    updatedlist[4] = str(bal)

    print("Your Net Balance: ", updatedlist[4], "Rs.")

    for index, row in enumerate(temporarylist):
        for field in row:
            if field == updatedlist[0]:
                temporarylist[index] = updatedlist

    f = open("user.txt", "w")
    for e in temporarylist:
        for e1 in e:
            if e1 == e[-1] and e1 == "":
                continue
            else:
                f.write(e1 + "\t")
        f.write("\n")
    f.close()
    print("Your transaction has been successful.")


#                -------------------ADMIN----------------------


# -------ADD ADMIN-----------

def a_admin(username, pin):
    updatedlist = []
    temporarylist = admin_list()
    a = 0
    b = 0
    for row in temporarylist:
        if row[1] == username and row[2] == pin and (row[3] == "Manager"):

            n_name = input("Enter the Name of new Admin: ")
            n_username = input("Enter the Username of new Admin: ")
            while b == 0:
                for rows in temporarylist:
                    if rows[1] == n_username:
                        print("Username already taken. Please choose another Username.")
                        n_username = input("Enter the Username of new Admin: ")
                        b = 0
                        break
                    else:
                        b = 1
            n_pin = input("Enter the Pin Code of new Admin: ")
            n_post = "Admin"
            add_by = row[0]

            updatedlist.append(n_name)
            updatedlist.append(n_username)
            updatedlist.append(n_pin)
            updatedlist.append(n_post)
            updatedlist.append(add_by)
            a = 1
            break

    if a == 0:
        print("Sorry, only Manager is allowed to add other Admins.")
    elif a == 1:
        temporarylist.append(updatedlist)
        print("Admin has been added successfully.")

    f = open("admin.txt", "w")
    for e in temporarylist:
        for e1 in e:
            if e1 == e[-1] and e1 == "":
                continue
            else:
                f.write(e1 + "\t")
        f.write("\n")
    f.close()


# -------REMOVE ADMIN-----------

def r_admin(username, pin):
    temporarylist = admin_list()

    a = 0
    for row in temporarylist:
        if row[1] == username and row[2] == pin and row[3] == "Manager":
            z = 0
            for rows in temporarylist:
                if rows[1] == username and rows[2] == pin and rows[3] == "Manager":
                    while z == 0:
                        col_width = max(len(word) for row in temporarylist for word in row) + 2
                        for rows1 in temporarylist:
                            for i, content in enumerate(rows1):
                                if rows1[3] != "Manager":
                                    if i != 2:
                                        print("".join(rows1[i].ljust(col_width)), end="\t")
                            print()
                        z += 1

            n_name = input("Enter the Name of Admin: ")
            n_username = input("Enter the Username of Admin: ")

            for rows in temporarylist:
                if rows[0] == n_name and rows[1] == n_username:
                    temporarylist.remove(rows)
                    a = 2
                    break
                else:
                    a = 1
            break

    if a == 0:
        print("Sorry, only Manager is allowed to remove other Admins.")
    elif a == 1:
        print("Admin hasn't found")
    elif a == 2:
        print("Admin has been removed successfully.")

    f = open("admin.txt", "w")
    for e in temporarylist:
        for e1 in e:
            if e1 == e[-1] and e1 == "":
                continue
            else:
                f.write(e1 + "\t")
        f.write("\n")
    f.close()


# ---------ADMIN DATA-----------
def admin_data(username, pin):
    temporarylist = admin_list()

    a = 0
    for row in temporarylist:
        if row[1] == username and row[2] == pin and row[3] == "Manager":
            a = 1
            break

    col_width = max(len(word) for row in temporarylist for word in row) + 2
    for row in temporarylist:
        for i, content in enumerate(row):
            if i != 2 and a == 1:
                print("".join(row[i].ljust(col_width)), end="\t")
            elif i != 1 and i != 2:
                print("".join(row[i].ljust(col_width)), end="\t")
        print()


# ---------USER DATA-----------

def user_data():
    temporarylist = user_list()

    col_width = max(len(word) for row in temporarylist for word in row) + 2
    for row in temporarylist:
        for i, content in enumerate(row):
            if i != 2 and i != 3:
                print("".join(row[i].ljust(col_width)), end="\t")
        print()


# -------------PIN---------------

def changepin(username, pin):
    updatedlist = ""
    temporarylist = admin_list()

    for row in temporarylist:
        if row[1] == username and row[2] == pin:
            updatedlist = row
            npin = 0
            zpin = 1

            while npin != zpin or npin == pin or len(npin) != 4:
                npin = input("Enter new pin: ")
                zpin = input("Re-Enter new pin: ")
                if npin != zpin:
                    print("New pins does not match")
                if npin == pin:
                    print("You are entering the old pin.")
                if len(npin) > 4:
                    print("Pin can't be greater than 4 digits")
                elif len(npin) < 4:
                    print("Pin can't be less than 4 digits")

            updatedlist[2] = npin
            pin = npin

    for index, row in enumerate(temporarylist):
        for field in row:
            if field == updatedlist[0]:
                temporarylist[index] = updatedlist

    f = open("admin.txt", "w")
    for e in temporarylist:
        for e1 in e:
            if e1 == e[-1] and e1 == "":
                continue
            else:
                f.write(e1 + "\t")
        f.write("\n")
    f.close()
    print("Pin has been changed")

    return pin


# -------ADD USER-----------

def a_user(username, pin):
    updatedlist = []
    temporarylist = user_list()
    reader = admin_list()
    c = 0
    d = 0

    a = 0
    for row in reader:
        if row[1] == username and row[2] == pin:

            n_account = input("Enter the Account no. of new User: ")
            while d == 0:
                for rows in temporarylist:
                    if rows[0] == n_account:
                        print("Account no. already taken. Please choose another Account no.")
                        n_account = input("Enter the Username of new User: ")
                        d = 0
                        break
                    else:
                        d = 1
            n_name = input("Enter the Name of new User: ")
            n_username = input("Enter the Username of new User: ")
            while c == 0:
                for rows in temporarylist:
                    if rows[1] == n_username:
                        print("Username already taken. Please choose another Username.")
                        n_username = input("Enter the Username of new User: ")
                        c = 0
                        break
                    else:
                        c = 1
            n_pin = input("Enter the Pin Code of new User: ")
            n_balance = input("Enter the Balance of new User: ")
            n_debt = "0"
            add_by = row[0]

            updatedlist.append(n_account)
            updatedlist.append(n_name)
            updatedlist.append(n_username)
            updatedlist.append(n_pin)
            updatedlist.append(n_balance)
            updatedlist.append(n_debt)
            updatedlist.append(add_by)
            a = 1
            break

    if a == 1:
        temporarylist.append(updatedlist)
        print("User has been added successfully.")

    else:
        print("User couldn't added for some reason.")

    f = open("user.txt", "w")
    for e in temporarylist:
        for e1 in e:
            if e1 == e[-1] and e1 == "":
                continue
            else:
                f.write(e1 + "\t")
        f.write("\n")
    f.close()


# -------REMOVE USER-----------

def r_user():
    temporarylist = user_list()

    z = 0
    while z == 0:
        col_width = max(len(word) for row in temporarylist for word in row) + 2
        for rows1 in temporarylist:
            for i, content in enumerate(rows1):
                if i != 2 and i != 3:
                    print("".join(rows1[i].ljust(col_width)), end="\t")
            print()
        z += 1

    n_account = input("Enter the Account no. of User: ")
    n_name = input("Enter the Name of User: ")

    a = 1
    for rows in temporarylist:
        if rows[1] == n_name and rows[0] == n_account:
            temporarylist.remove(rows)
            a = 2
            break

    if a == 1:
        print("User hasn't found")
    elif a == 2:
        print("Account has been removed successfully.")

    f = open("user.txt", "w")
    for e in temporarylist:
        for e1 in e:
            if e1 == e[-1] and e1 == "":
                continue
            else:
                f.write(e1 + "\t")
        f.write("\n")
    f.close()


# -------BAN USER-----------

def ban_user():
    temporarylist = user_list()
    banlist = buser_list()

    z = 0
    while z == 0:
        col_width = max(len(word) for row in temporarylist for word in row) + 2  # padding
        for rows1 in temporarylist:
            for i, content in enumerate(rows1):
                if i != 2 and i != 3:
                    print("".join(rows1[i].ljust(col_width)), end="\t")
            print()
        z += 1

    n_account = input("Enter the Account no. of User: ")
    n_name = input("Enter the Name of User: ")

    a = 1
    for rows in temporarylist:
        if rows[1] == n_name and rows[0] == n_account:
            temporarylist.remove(rows)
            banlist.append(rows)
            a = 2
            break
        else:
            a = 1

    if a == 1:
        print("User hasn't found")
    elif a == 2:
        print("Account has been banned successfully.")

    f = open("user.txt", "w")
    for e in temporarylist:
        for e1 in e:
            if e1 == e[-1] and e1 == "":
                continue
            else:
                f.write(e1 + "\t")
        f.write("\n")
    f.close()

    f = open("bannedUser.txt", "w")
    for e in banlist:
        for e1 in e:
            if e1 == e[-1] and e1 == "":
                continue
            else:
                f.write(e1 + "\t")
        f.write("\n")
    f.close()


# -------UNBAN USER-----------

def unban_user():
    banlist = buser_list()
    temporarylist = user_list()

    z = 0
    while z == 0:
        col_width = max(len(word) for row in banlist for word in row) + 2  # padding
        for rows1 in banlist:
            for i, content in enumerate(rows1):
                if i != 2 and i != 3:
                    print("".join(rows1[i].ljust(col_width)), end="\t")
            print()
        z += 1

    n_account = input("Enter the Account no. of User: ")
    n_name = input("Enter the Name of User: ")

    a = 1
    for rows in banlist:
        if rows[1] == n_name and rows[0] == n_account:
            banlist.remove(rows)
            temporarylist.insert(int(rows[0]), rows)
            a = 2
            break

    if a == 1:
        print("User hasn't found")
    elif a == 2:
        print("Account has been unbanned successfully.")

    f = open("user.txt", "w")
    for e in temporarylist:
        for e1 in e:
            if e1 == e[-1] and e1 == "":
                continue
            else:
                f.write(e1 + "\t")
        f.write("\n")
    f.close()

    f = open("bannedUser.txt", "w")
    for e in banlist:
        for e1 in e:
            if e1 == e[-1] and e1 == "":
                continue
            else:
                f.write(e1 + "\t")
        f.write("\n")
    f.close()


# ------BANNED USER INFO------

def ban_user_data():
    temporarylist = buser_list()

    col_width = max(len(word) for row in temporarylist for word in row) + 2
    for row in temporarylist:
        for i, content in enumerate(row):
            if i != 2 and i != 3:
                print("".join(row[i].ljust(col_width)), end="\t")
        print()
