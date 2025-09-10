def apply_discount(price, discount_percent):
    return price - (price * discount_percent / 100)


def add_gst(price, gst_percent=18):
    return price + (price * gst_percent / 100)


def generate_invoice(cart, discount_percent=0, gst_percent=18):
    print("------ INVOICE ------")
    subtotal = 0
    for product, price in cart.items():
        print(f"{product:<15}: ₹{price}")
        subtotal += price
    
    print("---------------------")
    print(f"Subtotal: ₹{subtotal}")

    discounted_price = apply_discount(subtotal, discount_percent)
    if discount_percent > 0:
        print(f"After {discount_percent}% discount: ₹{discounted_price:.2f}")

    final_price = add_gst(discounted_price, gst_percent)
    print(f"After {gst_percent}% GST: ₹{final_price:.2f}")
    print("---------------------")
    print("Thank you for shopping with us!")










