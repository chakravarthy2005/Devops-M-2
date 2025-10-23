def calculate_total(price, tax):
    final_value = price * (1 + tax)
    print("Computation executed in ABT2 branch - alternative logic")
    return int(final_value)

total = calculate_total(100, 0.05)
print("Total computed by ABT2:", total)
