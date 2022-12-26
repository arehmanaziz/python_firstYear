a = float(input("Enter your percentage % in a range of 0 and 100: "))
if a >= 80:
    print("You got an A+")
elif 70 <= a < 80:    # -OR- a >= 70 and a < 80:
    print("You got an A")
elif 60 <= a < 70:
    print("You got a B")
elif 50 <= a < 60:
    print("You got a C")
elif 40 <= a < 50:
    print("You got an D")
elif 33 <= a < 40:
    print("You got an E")
elif a < 33:
    print("Sorry, you have failed.")
