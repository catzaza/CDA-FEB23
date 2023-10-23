# first we ask user to enter thier desired meal items cost
item_cost = float(input("Enter item cost: $"))
# calc the tip 18%
tip_precent = 18
tip_amount = (tip_precent / 100) * item_cost
# then we ahve to calc sales tax
tax_precent = 7
tax_amount = (tax_precent / 100) * item_cost
# now we can calc the total amounts
total_sum = item_cost + tip_amount + tax_amount
# then print results
print(f"Cost of the food: ${item_cost:.2f}")
print(f"Tip (18%): ${tip_amount:.2f}")
print(f"Sales Tax (7%): ${tax_amount:.2f}")
print(f"Total Amount: ${total_sum:.2f}")
