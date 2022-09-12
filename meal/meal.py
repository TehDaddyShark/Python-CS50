def main():
    #Get input
    time = input("What's the time? ")
    time = convert(time)
    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(':')
    #hours = float(hours) dont need this if i pass hours into float on L14
    #minutes = float(minutes)
    minutes = (float(minutes) / 60)
    time = float(hours) + minutes 
    return time
    

if __name__ == "__main__":
    main()