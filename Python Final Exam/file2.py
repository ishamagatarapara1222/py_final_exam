
# Inventory List Analyzer - Store Stock Review
# Python Final Exam 

print("==============================================")
print("       INVENTORY LIST ANALYZER")
print("==============================================")

items = []

print("\nWelcome to Inventory List Analyzer!")

# Taking inventory details from the user
while True:
    name = input("\nEnter item name: ").strip()

    if name == "":
        print("Item name cannot be empty. Please try again.")
        continue

    category = input("Enter category: ").strip().lower()

    if category == "":
        print("Category cannot be empty. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity < 0:
            print("Quantity cannot be negative.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    # Store item details in a dictionary
    item = {
        "name": name.title(),
        "category": category,
        "quantity": quantity
    }

    items.append(item)

    choice = input("\nDo you want to add more items? (y/n): ").strip().lower()

    if choice != "y":
        break


# Displaying the inventory summary
if len(items) == 0:
    print("\nNo inventory items were entered.")

else:
    quantities = [item["quantity"] for item in items]

    total_items = len(items)
    total_quantity = sum(quantities)
    average_quantity = total_quantity / total_items

    
    highest_item = max(items, key=lambda item: item["quantity"])
    lowest_item = min(items, key=lambda item: item["quantity"])

    # unique categories
    categories = set()

    for item in items:
        categories.add(item["category"])

    print("\n=================================")
    print("\n======INVENTORY SUMMARY==========")
    print("\n=================================")

    print("\nTotal Different Items:", total_items)
    print("Total Quantity in Stock:", total_quantity)
    print("Average Quantity per Item:", round(average_quantity, 2))

    print("\nMost Stocked Item:",
          highest_item["name"], "-", highest_item["quantity"], "units")

    print("Least Stocked Item:",
          lowest_item["name"], "-", lowest_item["quantity"], "units")

    # Display unique categories in alphabetical order
    print("\nUnique Categories in Inventory:")

    for category in sorted(categories):
        print("-", category)

    # Sort items by quantity from highest to lowest
    sorted_items = sorted(
        items,
        key=lambda item: item["quantity"],
        reverse=True
    )

    print("\nItems Sorted by Quantity (High to Low):")

    for number, item in enumerate(sorted_items, start=1):
        print(
            str(number) + ".",
            item["name"], "-",
            item["quantity"], "units"
        )

    # Display categories in alphabetical order
    print("\nCategories in Alphabetical Order:")

    for number, category in enumerate(sorted(categories), start=1):
        print(str(number) + ".", category)

    print("\n================================")
    print("          END OF REPORT")
    print("\n================================")
