expenses = {}
total = 0

while True:
    category = input("Enter expense category (or 'done' to finish): ")

    if category.lower() == "done":
        break

    amount = float(input("Enter expense amount: ₹"))

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

    total += amount

print("\n========== EXPENSE SUMMARY ==========")

for category, amount in expenses.items():
    print(f"{category}: ₹{amount:.2f}")

print("-------------------------------------")
print(f"Total Spent: ₹{total:.2f}")
print("=====================================")