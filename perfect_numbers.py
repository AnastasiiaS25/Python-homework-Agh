for n in range(1, 10001):
    dividers_sum = 0
    for divider in range(1, n):
        if n % divider == 0:
            dividers_sum = dividers_sum + divider
            # dividers_sum += divider  # alternatywny skrócony zapis

    if dividers_sum == n:
        print(f"{n} jest liczbą doskonałą")
