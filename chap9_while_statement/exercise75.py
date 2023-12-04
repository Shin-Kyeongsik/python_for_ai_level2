threshold_num = int(input("Enter a number: "))

cum_sum, i = 0, 0
while True:
    cum_sum += i
    i += 1
    print(f"{i} - {cum_sum}")
    if cum_sum > threshold_num:
        break
