# expense_tracker.py
# Simple CSV-based Expense Tracker (beginner friendly)

import csv
from datetime import date, datetime
from collections import defaultdict

CSV_FILE = "expenses.csv"

# ----- helpers -----
def parse_date(s: str) -> str:
    s = s.strip()
    if not s:
        return date.today().isoformat()
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            continue
    raise ValueError("Use YYYY-MM-DD or DD-MM-YYYY (or leave blank for today).")

def read_all_rows():
    try:
        with open(CSV_FILE, newline="", encoding="utf-8") as f:
            return list(csv.reader(f))
    except FileNotFoundError:
        return []

# ----- operations -----
def add_expense():
    try:
        ds = input("Date (YYYY-MM-DD) [blank = today]: ").strip()
        ds = parse_date(ds)
    except ValueError as e:
        print("Invalid date:", e)
        return
    category = input("Category (Food, Travel, Bills...): ").strip() or "Uncategorized"
    amt_s = input("Amount (numbers only): ").strip()
    try:
        amt = float(amt_s)
    except ValueError:
        print("Invalid amount.")
        return
    desc = input("Description (optional): ").strip()
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([ds, category, f"{amt:.2f}", desc])
    print("✅ Expense saved.")

def view_expenses():
    rows = read_all_rows()
    if not rows:
        print("No expenses yet.")
        return
    print(f"{'No':<3} {'Date':<10} {'Category':<12} {'Amount':>8}  Description")
    print("-"*55)
    for i, r in enumerate(rows, 1):
        d, c, a, desc = r[0], r[1], float(r[2]), (r[3] if len(r)>3 else "")
        print(f"{i:<3} {d:<10} {c[:12]:<12} {a:8.2f}  {desc}")

def total_spent():
    rows = read_all_rows()
    total = sum(float(r[2]) for r in rows) if rows else 0.0
    print(f"Total spent so far: {total:.2f}")

def category_summary():
    rows = read_all_rows()
    if not rows:
        print("No expenses yet.")
        return
    t = defaultdict(float)
    for r in rows:
        t[r[1]] += float(r[2])
    print("Category totals:")
    for cat, amt in sorted(t.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:12}  {amt:8.2f}")

# ----- CLI -----
def menu():
    print("\nSimple Expense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Total spent")
    print("4. Category summary")
    print("0. Exit")

def main():
    while True:
        menu()
        ch = input("Choice: ").strip()
        if ch == "1":
            add_expense()
        elif ch == "2":
            view_expenses()
        elif ch == "3":
            total_spent()
        elif ch == "4":
            category_summary()
        elif ch == "0":
            print("Bye 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


