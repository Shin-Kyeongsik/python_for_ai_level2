threshold_num = int(input("Enter a number: "))

cum_sum = 0
i = 0
while cum_sum <= threshold_num:
    cum_sum += i
    i += 1
    print(f"{i} - {cum_sum}")
