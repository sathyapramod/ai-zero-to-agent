bill = float(input("Enter the bill amount: ₹ "))
tip_percent = float(input("Enter the tip percentage: "))

tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount

print(f"\nBill:   ₹{bill:.2f}")
print(f"Tip:    ₹{tip_amount:.2f} ({tip_percent}%)")
print(f"Total:  ₹{total:.2f}")
