def main():
    #get input as int
    mass = int(input("How much kilograms? "))
    #E=MC*2 (not in motion) 
    joules = mass * 300000000 **2
    #print answer
    print(f"{joules}")


main()