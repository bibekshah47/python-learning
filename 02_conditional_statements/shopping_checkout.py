# Problem: Online Shopping Checkout System
# Difficulty: Hard
# Lesson: Conditional Statements

purchase_amount = float(input("Enter total purchase amount: "))

if purchase_amount <= 0:
    print("Invalid purchase amount")

else:
    membership_status = input("Are you a member? (yes/no): ")
    coupon_code = input("Enter coupon code: ")

    discount_amount = 0
    coupon_discount = 0

    # Regular discount
    if purchase_amount >= 500:
        if membership_status == "yes":
            discount_amount = purchase_amount * 0.20
        else:
            discount_amount = purchase_amount * 0.10

    elif purchase_amount >= 200:
        if membership_status == "yes":
            discount_amount = purchase_amount * 0.15
        else:
            discount_amount = purchase_amount * 0.05

    else:
        if membership_status == "yes":
            discount_amount = purchase_amount * 0.05

    total_amount = purchase_amount - discount_amount

    # Coupon discount
    if coupon_code == "SAVE10" and purchase_amount >= 100:
        coupon_discount = total_amount * 0.10
        total_amount = total_amount - coupon_discount

    # Shipping charge
    if membership_status == "yes" or total_amount >= 100:
        shipping_charge = 0
    else:
        shipping_charge = 10

    # Sales tax and final amount
    sales_tax = total_amount * 0.08
    final_amount = total_amount + shipping_charge + sales_tax

    # Display bill
    print("Original purchase: $", round(purchase_amount, 2), sep="")
    print("Regular discount: $", round(discount_amount, 2), sep="")
    print("Coupon discount: $", round(coupon_discount, 2), sep="")
    print("Shipping charge: $", round(shipping_charge, 2), sep="")
    print("Sales tax: $", round(sales_tax, 2), sep="")
    print("Final bill: $", round(final_amount, 2), sep="")