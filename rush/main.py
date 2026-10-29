#!/usr/bin/env python3

LOAN_DAYS = 7
FEE_PER_DAY = 10
MAX_ITEMS_PER_PERSON = 3

# ============================================================
# HELPER FUNCTIONS / ฟังก์ชันช่วย / အကူဖန်ရှင်များ
# ============================================================

def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("Input cannot be empty. Please try again.")


def read_int(prompt, minimum):
    while True:
        text = input(prompt).strip()
        try:
            number = int(text)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if number < minimum:
            print(f"Number must be at least {minimum}.")
        else:
            return number


def make_item(item_id, name, category):
    return {"id": item_id, "name": name, "category": category,
            "available": True, "borrower": "", "times_borrowed": 0}


def find_item(items, item_id):
    for item in items:
        if item["id"].upper() == item_id.upper():
            return item
    return None


def count_borrowed(items, borrower):
    count = 0
    for item in items:
        if item["borrower"].lower() == borrower.lower():
            count += 1
    return count


def calculate_fee(days_kept):
    overdue = days_kept - LOAN_DAYS
    if overdue > 0:
        return overdue * FEE_PER_DAY
    return 0


def get_times(item):
    return item["times_borrowed"]


def normalize_category(text):
    shortcuts = {"b": "book", "g": "gadget", "o": "other"}
    text = text.strip().lower()
    return shortcuts.get(text, text)

# ============================================================
# MENU ACTIONS / ฟังก์ชันของแต่ละเมนู / မီနူးလုပ်ဆောင်ချက်များ
# ============================================================

def add_item(items):
    item_id = read_text("Item ID (e.g. B010): ").upper()
    if find_item(items, item_id) is not None:
        print("This ID already exists. Item not added.")
        return
    name = read_text("Item name: ")
    category = normalize_category(read_text("Category (b=book, g=gadget, o=other): "))
    items.append(make_item(item_id, name, category))
    print("Item added successfully!")


def edit_item(items):
    item_id = read_text("Item ID to edit: ")
    item = find_item(items, item_id)
    if item is None:
        print("Item not found.")
        return
    print("Press Enter to keep the current value.")

    new_id = input(f"ID [{item['id']}]: ").strip().upper()
    if new_id != "" and new_id != item["id"]:
        other = find_item(items, new_id)
        if other is not None and other is not item:
            print("This ID already exists. Edit cancelled.")
            return
        item["id"] = new_id

    new_name = input(f"Name [{item['name']}]: ").strip()
    if new_name != "":
        item["name"] = new_name

    new_category = normalize_category(input(f"Category (b/g/o) [{item['category']}]: "))
    if new_category != "":
        item["category"] = new_category

    print("Item updated successfully!")


def view_items(items):
    if len(items) == 0:
        print("No items yet.")
        return
    print(f"{'ID':<6}{'Name':<26}{'Category':<10}Status")
    for item in items:
        status = "Available" if item["available"] else "Borrowed by " + item["borrower"]
        print(f"{item['id']:<6}{item['name']:<26}{item['category']:<10}{status}")


def borrow_item(items):
    item_id = read_text("Item ID to borrow: ")
    item = find_item(items, item_id)
    if item is None:
        print("Item not found.")
    elif not item["available"]:
        print("Sorry, this item is already borrowed.")
    else:
        borrower = read_text("Borrower name: ")
        if count_borrowed(items, borrower) >= MAX_ITEMS_PER_PERSON:
            print(f"{borrower} already holds {MAX_ITEMS_PER_PERSON} items. Return one first.")
        else:
            item["available"] = False
            item["borrower"] = borrower
            item["times_borrowed"] += 1
            print(f"{borrower} borrowed '{item['name']}'. Return within {LOAN_DAYS} days.")


def return_item(items, stats):
    item_id = read_text("Item ID to return: ")
    item = find_item(items, item_id)
    if item is None:
        print("Item not found.")
    elif item["available"]:
        print("This item was not borrowed.")
    else:
        days_kept = read_int("Days the item was kept: ", 1)
        fee = calculate_fee(days_kept)
        item["available"] = True
        item["borrower"] = ""
        stats["total_fees"] += fee
        stats["returns"] += 1
        if fee > 0:
            print(f"Returned late! Fine: {fee} baht.")
        else:
            print("Returned on time. No fine.")


def search_items(items):
    keyword = read_text("Search keyword (name or category): ").lower()
    only_free = input("Only available items? (y/n): ").strip().lower() == "y"
    found = 0
    for item in items:
        matches = keyword in item["name"].lower() or keyword in item["category"].lower()
        if matches and (not only_free or item["available"]):
            print(f"  {item['id']} - {item['name']} [{item['category']}]")
            found += 1
    print(f"Matching records: {found}")


def show_summary(items, stats):
    if len(items) == 0:
        print("No data to summarize.")
        return
    on_loan = 0
    per_category = {}
    for item in items:
        if not item["available"]:
            on_loan += 1
        per_category[item["category"]] = per_category.get(item["category"], 0) + 1
    print("----- SUMMARY -----")
    print(f"Total items: {len(items)} | On loan: {on_loan} | Available: {len(items) - on_loan}")
    print("Per category:", per_category)
    ranked = sorted(items, key=get_times, reverse=True)
    print("Most borrowed (top 3):")
    for item in ranked[:3]:
        print(f"  {item['name']}: {item['times_borrowed']} times")
    print(f"Total fines: {stats['total_fees']} baht from {stats['returns']} returns")

# ============================================================
# MAIN PROGRAM / โปรแกรมหลัก / ပင်မပရိုဂရမ်
# ============================================================

def show_menu():
    print("\n===== LIBRARY & GADGET LENDING =====")
    print("1. Add Item\n2. View Items\n3. Borrow Item\n4. Return Item\n5. Search Items\n6. Summary Report\n7. Edit Item\n8. Exit")


def main():
    items = [
        make_item("B001", "Python Crash Course", "book"),
        make_item("B002", "Clean Code", "book"),
        make_item("G001", "Arduino Kit", "gadget"),
        make_item("G002", "Raspberry Pi 4", "gadget"),
    ]
    stats = {"total_fees": 0, "returns": 0}
    while True:
        show_menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            add_item(items)
        elif choice == "2":
            view_items(items)
        elif choice == "3":
            borrow_item(items)
        elif choice == "4":
            return_item(items, stats)
        elif choice == "5":
            search_items(items)
        elif choice == "6":
            show_summary(items, stats)
        elif choice == "7":
            edit_item(items)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


try:
    main()
except (KeyboardInterrupt, EOFError):
    print("\nGoodbye!")
