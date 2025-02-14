x1 = float(input("Enter the price of one roll of wallpaper (x1): "))
x2 = float(input("Enter the price of one can of paint (x2): "))
total_cost = 8 * x1 + 2 * x2

if 200 <= total_cost <= 500:
    discount = 0.03  # 3%
elif 500 < total_cost <= 800:
    discount = 0.05  # 5%
elif 800 < total_cost <= 1000:
    discount = 0.07  # 7%
elif total_cost > 1000:
    discount = 0.09  # 9%
else:
    discount = 0.0  # Нет скидки

final_cost = total_cost * (1 - discount)

print(f"The total cost is: {final_cost:.2f} rubles")
