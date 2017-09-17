hrs = input("Enter Hours:")
h = input("Enter Pay: ")

hrs = float(hrs)
h = float(h)

if hrs <= 40:
    print("{}".format(hrs * h))

elif hrs > 40:
    print("{}".format((40 * h) + ((hrs - 40) * (h * 1.5))))