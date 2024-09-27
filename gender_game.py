gender = input("What is your gender (M or F): ")
namef = input("First name: ")
namel = input("Last name: ")
age = int(input("Age: "))

print()

if age >20:
    if gender == 'M':
        print(f"Then I shall call you Mr. {namel}")
    elif gender == 'F':
        mstatus = input(f"Are you married, {namef} (y or n)?")
        if mstatus == 'y':
            print(f"Then I shall call you Mrs. {namel}.")
        elif mstatus == 'n':
            print(f"Then I shall call you Ms. {namel}.")
elif age < 20:
    print(f"Then I sahll call you {namef, namel}.")
else:
    print("Invalid Answer")