# 🍽️ Restaurant Menu & Order Management System

This project is part of a Python assignment focused on **data structures** — specifically dictionaries, lists, and nested data handling.

It simulates a simple restaurant system including menu display, cart operations, inventory tracking, and sales analysis.

---

## 📁 Project Structure


---

## 🧠 Concepts Used

- Dictionaries (nested)
- Lists of dictionaries
- Loops (for, while)
- Conditional statements
- Functions
- Deep copy (`copy.deepcopy`)
- Basic data analysis logic

---

## ✅ Tasks Implemented

### 🔹 Task 1: Explore the Menu
- Displayed menu grouped by category (Starters, Mains, Desserts)
- Showed price and availability of each item
- Computed:
  - Total items
  - Available items
  - Most expensive item
  - Items priced under ₹150

---

### 🔹 Task 2: Cart Operations
- Created a cart as a list of dictionaries
- Implemented:
  - Add item (with validation)
  - Remove item
  - Update quantity
- Handled:
  - Non-existent items
  - Unavailable items
  - Duplicate items (updated quantity instead)
- Simulated a full user flow
- Generated final bill with:
  - Subtotal
  - GST (5%)
  - Total payable amount

---

### 🔹 Task 3: Inventory Tracker
- Used `deepcopy` to create a backup of inventory
- Demonstrated that backup remains unchanged after modification
- Restored inventory to original state
- Simulated order fulfillment:
  - Deducted stock based on cart
  - Prevented stock from going below zero
- Printed reorder alerts for low stock items

---

### 🔹 Task 4: Sales Log Analysis
- Calculated total revenue per day
- Identified best-selling day
- Found most ordered item
- Added a new day's sales data
- Recomputed updated statistics
- Printed a numbered list of all orders across dates

---

## ▶️ How to Run

1. Make sure Python is installed
2. Run the script:

```bash
python part2_order_system.py
