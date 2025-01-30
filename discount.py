amount = float(input("Enter the total amount spent: "))
if amount > 5000:
    discount = amount * 0.10
elif amount > 1000:
    discount = amount * 0.05
else:
    discount = 0
final_amount = amount - discount
print(f"Discount: {discount:.2f}")
print(f"Final amount to be paid: {final_amount:.2f}")
