num = int(input("Enter a number: "))

divisor = 2
while True:
    if num % divisor == 0:
        print(f"First non-one divisor: {divisor}")
        break
    divisor += 1