num = int(input("Enter a number: "))

IS_PRIME = True
for divisor in range(2, num):
    if num % divisor == 0:
        IS_PRIME = False

if IS_PRIME:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")