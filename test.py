def calculate_total(price, tax):
    result = price + (price * tax)
    print("Calculation done in MAIN branch")
    return result

total = calculate_total(100, 0.05)
print("Total from MAIN:", total)
