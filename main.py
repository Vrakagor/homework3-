def main():
    number = int(input("Введіть 5-ти значне число: "))

    digit1, remainder = divmod(number, 10000)
    digit2, remainder = divmod(remainder, 1000)
    digit3, remainder = divmod(remainder, 100)
    digit4, digit5 = divmod(remainder, 10)


    print(digit5, digit4, digit3, digit2, digit1)

if __name__ == "__main__":
    main()
