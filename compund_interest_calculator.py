'''principle = float(input("Enter your initial principle: "))
while principle <= 0 :
    print("Invalid input. Enter initial principle: ")
    principle = float(input("Enter your initial principle: "))

rate = float(input("Enter your interest rate: "))
while rate <= 0:
    print("Invalid input! Enter your interest rate: ")
    rate = float(input("Enter your interest rate: "))

time_elapsed= int(input("Enter amount of time elapsed in years: "))
while time_elapsed <= 0:
    print("Invalid input! Enter amount of time elapsed in years: ")
    time_elapsed= int(input("Enter amount of time elapsed in years: "))
total = principle * pow((1 + rate / 100), time_elapsed)
print(f"Balance after {time_elapsed} year(s) is {total:.2f} ksh")'''
# using while loops, try and except and conditional statements
while True:
    principle = float(input("Enter principle: "))
    try:
        if principle <= 0:
            print("Invalid input! Enter principle: ")
        else:
            break
    except ValueError:
        print("Invalid input! Enter numeric values")

while True:
    rate = float(input("Enter your interest rate: "))
    try:
        if rate <= 0:
            print("Invalid input! Enter your interest rate: ")
        else:
            break
    except ValueError:
        print("Invalid input Enter numeric values: ")

while True:
    time_elapsed = int(input("Enter amount of time in years: "))
    try:
        if time_elapsed <= 0:
            print("Invalid input! Enter amount of time in years")
        else:
            break
    except ValueError:
        print("Invalid input! Enter numeric values: ")
total = principle * pow((1 + rate / 100), time_elapsed)
print(f"Balance after {time_elapsed} year(s) is {total:.2f} ksh")
