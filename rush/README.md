# Library & Gadget Lending System

## Purpose / วัตถุประสงค์
A terminal application that helps a small library or club manage books and gadgets:
who borrowed what, who must return it, and how much late fine is owed.

โปรแกรมบน Terminal สำหรับจัดการการยืม-คืนหนังสือและอุปกรณ์ พร้อมคิดค่าปรับเมื่อคืนเกินกำหนด

## Main Features
1. **Add Item** – add a book/gadget (duplicate IDs are rejected)
2. **View Items** – list every item with its status
3. **Borrow Item** – lend an item to a person
4. **Return Item** – return an item and calculate the late fine
5. **Search Items** – search by name/category, optionally only available items
6. **Summary Report** – totals, items per category, top-3 most borrowed, total fines
7. **Edit Item** - Edit ID, name , catagory

## Business Rules
- An item that is already borrowed cannot be borrowed again.
- One person may hold at most 3 items at once.
- Items kept longer than 7 days are fined 10 baht per overdue day.
- Item IDs must be unique.

## Data Processing
- Conditional search with filters (name / category / availability)
- Sorting by popularity (most borrowed first)
- Counting items per category (dictionary) and totals / fine accumulation

## How to Run
```
python3 main.py
```

## Files
- `main.py` – the whole program (every line commented in Thai / English / Burmese)
- `README.md` – this file
- `auteur` – the two Intra logins of the team
