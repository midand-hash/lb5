denominations = [500, 100, 50, 10, 5, 2, 1]

S = int(input("Enter the amount to pay (S): "))

bills_count = {}

for denomination in denominations:
    count = S // denomination  # Сколько купюр данного номинала нужно
    if count > 0:
        bills_count[denomination] = count
    S %= denomination  # Остаток суммы

print("The customer will give the following bills:")
for denomination, count in bills_count.items():
    print(f"{denomination} RUB: {count}")
