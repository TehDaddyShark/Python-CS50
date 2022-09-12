def main():
    #get input
    x, y, z = (input("Expression: ")).split(" ")
    #split and assign to each variable
    # convert to float
    x = float(x)
    z = float(z)
    if y == "+":
        print(x + z)

    elif y == "-":
        print(x - z)
    
    elif y == "*":
        print(x * z)

    elif y == "/":
        print(x / z)

    else:
        print("Unknow function")

    
main()
