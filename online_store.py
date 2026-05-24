# Question 2 — Online Store Discount System

purchase = float(input("Enter total purchase amount: "))
member = input("Are you a loyalty member? (yes/no): ")

discount = 0

if purchase < 1000:
    discount = 0

elif purchase <= 4999:
    discount = 5

elif purchase <= 14999:
    discount = 10

else:
    discount = 20

discount_amount = (purchase * discount) / 100
final_amount = purchase - discount_amount

if member.lower() == "yes":
    extra_discount = (final_amount * 5) / 100
    final_amount = final_amount - extra_discount

print("Final payable amount: NPR", final_amount)
