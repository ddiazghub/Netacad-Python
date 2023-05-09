from random import randint

def main() -> None:
    print("Guess the number")
    number: int = randint(0, 10000)
    tries: int = 0

    while True:
        invalue: int = int(input())
        tries += 1

        if number == invalue:
            print("You win!")
            print(f"Total tries: {tries}")
            return
        
        print("Bigger") if invalue < number else print("Smaller")


if __name__ == "__main__":
    main()