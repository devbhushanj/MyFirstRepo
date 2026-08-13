# Mini Supermarket Billing System

print("================================")
print("     MINI SUPER MARKET")
print("================================")

items = []
total = 0

while True:
    name = input("\nEnter item name (or 'done' to finish): ")

    if name.lower() == "done":
        break

    price = float(input("Enter price: ₹"))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    total += amount

    items.append([name, price, quantity, amount])

# Display Bill
print("\n================================")
print("           BILL")
print("================================")
print("Item\tPrice\tQty\tAmount")
print("--------------------------------")

for item in items:
    print(f"{item[0]}\t₹{item[1]:.2f}\t{item[2]}\t₹{item[3]:.2f}")

print("--------------------------------")
print(f"Total Amount: ₹{total:.2f}")

# Discount
if total >= 1000:
    discount = total * 0.10
    print(f"Discount (10%): ₹{discount:.2f}")
else:
    discount = 0
    print("Discount: ₹0.00")

final_amount = total - discount

print("--------------------------------")
print(f"Final Amount: ₹{final_amount:.2f}")
print("================================")
print("     THANK YOU! VISIT AGAIN")
print("================================")