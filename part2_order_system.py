menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


# ---------------- TASK 1: EXPLORE MENU ----------------

print("\n===== MENU =====")

# Get unique categories
categories = set()
for item in menu:
    categories.add(menu[item]["category"])

# Loop through each category
for category in categories:
    print(f"\n===== {category} =====")

    # Loop through menu items
    for item, details in menu.items():
        if details["category"] == category:
            price = details["price"]
            availability = "Available" if details["available"] else "Unavailable"

            print(f"{item}  ₹{price:.2f}  [{availability}]")

# ---------------- SUMMARY ----------------

# Total items
total_items = len(menu)

# Available items
available_items = sum(1 for item in menu if menu[item]["available"])

# Most expensive item
most_expensive = max(menu.items(), key=lambda x: x[1]["price"])
most_exp_name = most_expensive[0]
most_exp_price = most_expensive[1]["price"]

# Items under ₹150
under_150 = []
for item, details in menu.items():
    if details["price"] < 150:
        under_150.append((item, details["price"]))

print("\n----- SUMMARY -----")
print(f"Total items: {total_items}")
print(f"Available items: {available_items}")
print(f"Most expensive: {most_exp_name} (₹{most_exp_price})")

print("\nItems under ₹150:")
for item, price in under_150:
    print(f"{item} (₹{price})")


# ---------------- TASK 2: CART OPERATIONS ----------------

cart = []

# Function to display cart
def show_cart():
    print("\nCurrent Cart:")
    if not cart:
        print("Cart is empty")
    else:
        for item in cart:
            print(f"{item['item']} x{item['quantity']} (₹{item['price']})")

# Add item function
def add_item(item_name, quantity):
    if item_name not in menu:
        print(f"{item_name} does not exist in menu.")
        return

    if not menu[item_name]["available"]:
        print(f"{item_name} is currently unavailable.")
        return

    # Check if already in cart
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(f"Updated {item_name} quantity to {item['quantity']}")
            return

    # Add new item
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": menu[item_name]["price"]
    })
    print(f"Added {item_name} x{quantity}")

# Remove item function
def remove_item(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"Removed {item_name} from cart")
            return
    print(f"{item_name} not found in cart")

# Update quantity function
def update_quantity(item_name, quantity):
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] = quantity
            print(f"{item_name} quantity updated to {quantity}")
            return
    print(f"{item_name} not found in cart")


# ---------------- SIMULATION ----------------

print("\n===== CART SIMULATION =====")

add_item("Paneer Tikka", 2)
show_cart()

add_item("Gulab Jamun", 1)
show_cart()

add_item("Paneer Tikka", 1)  # should update to 3
show_cart()

add_item("Mystery Burger", 1)  # does not exist
show_cart()

add_item("Chicken Wings", 1)  # unavailable
show_cart()

remove_item("Gulab Jamun")
show_cart()


# ---------------- FINAL BILL ----------------

print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    item_total = item["quantity"] * item["price"]
    subtotal += item_total
    print(f"{item['item']} x{item['quantity']}  ₹{item_total:.2f}")

print("-----------------------------------")

gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal: ₹{subtotal:.2f}")
print(f"GST (5%): ₹{gst:.2f}")
print(f"Total Payable: ₹{total:.2f}")
print("===================================")
