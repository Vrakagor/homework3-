def main():
    number = int(input("Введіть 5-ти значне число: "))

    digit1, remainder = divmod(number, 10000)
    digit2, remainder = divmod(remainder, 1000)
    digit3, remainder = divmod(remainder, 100)
    digit4, digit5 = divmod(remainder, 10)


    print(digit5, end = "")
    print(digit4, end = "")
    print(digit3, end = "")
    print(digit2, end = "")
    print(digit1, end = "")

if __name__ == "__main__":
    main()
