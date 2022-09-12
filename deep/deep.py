def main():
    answer = input("Tell me the answer to everything ")
    
    match answer:
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")

main()