def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #remove $ from the input and return a float
    d = float(d.lstrip("$"))
    return d
    


def percent_to_float(p):
    #remove % from the input and return a float
    p = float(p.rstrip("%"))
    return p / 100 #needed to / by 100 other wise you will be tipping ALOT


main()