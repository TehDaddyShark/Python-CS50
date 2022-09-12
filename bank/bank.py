def main():
    #get input and format better
    greet = input("Greeting: ").lower()
    #check input
    if 'hello' in greet:
        print("$0")
    #hard to figure this part out, apperently every character in a str has a index number
    #EX. Hello.... H = 0 or -10.... E = 1 or - 9 
    # useing '[]' you can index over the str just input the number you want to check 
    # '0' is first '-1' is last
    elif 'h' in greet[0]:
        print("$20")
    else:
        print("$100")
#i don't think I can optmize better right now
main()