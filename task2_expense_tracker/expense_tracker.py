def add_expense(expenses_list):
    print("\n--- Add New Expense ---")
    title = input("Enter expense title (e.g. Lunch): ").strip().title()

    while True:
        try:
            amount = float(input("Enter amount spent: "))
            if amount <= 0:
                print("Amount must be greater than zero. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for amount.")

    category = (
        input("Enter category (Food, Transport, Books, Bills): ")
        .strip()
        .title()
    )
    
    expense = {"title": title, "amount": amount, "category": category}
    expenses_list.append(expense)
    
    print(f"\nSuccess: Added '{title}' (${amount:.2f}) under [{category}].")


def view_all_expenses(expenses_list):
    print("\n" + "=" * 50)
    print("              All Recorded Expenses             ")
    print("=" * 50)

    if not expenses_list:
        print("No expenses recorded yet.")
        print("=" * 50)
        return

    print(f"{'#':<4} | {'Title':<18} | {'Category':<12} | {'Amount':<10}")
    print("-" * 50)

    for index, item in enumerate(expenses_list, start=1):
        print(
            f"{index:<4} | {item['title']:<18} | {item['category']:<12} | ${item['amount']:<10.2f}"
        )

    print("=" * 50)


def view_summary(expenses_list):
    print("\n" + "=" * 50)
    print("            Spending Summary & Analytics          ")
    print("=" * 50)

    if not expenses_list:
        print("No expenses recorded yet. Cannot generate summary.")
        print("=" * 50)
        return

    # 1. Total Spending
    total_spending = sum(item["amount"] for item in expenses_list)

    # 2. Spending Per Category (Dictionary Aggregation)
    category_totals = {}
    for item in expenses_list:
        cat = item["category"]
        amt = item["amount"]
        category_totals[cat] = category_totals.get(cat, 0.0) + amt

    # 3. Highest Expense Logged
    highest_expense = max(expenses_list, key=lambda x: x["amount"])

    # Print Summary Breakdown
    print(f"Total Overall Spending : ${total_spending:.2f}")
    print(
        f"Highest Single Expense : {highest_expense['title']} (${highest_expense['amount']:.2f})"
    )

    print("\n--- Spending Breakdown By Category ---")
    print(f"{'Category':<20} | {'Total Spent':<12} | {'% of Total':<10}")
    print("-" * 50)

    for cat, amt in category_totals.items():
        percentage = (amt / total_spending) * 100
        print(f"{cat:<20} | ${amt:<11.2f} | {percentage:<9.1f}%")

    print("=" * 50)


def main():
    expenses = []

    while True:
        print("\n" + "=" * 35)
        print("     Personal Expense Tracker     ")
        print("=" * 35)
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Spending Summary & Analytics")
        print("4. Exit")
        print("=" * 35)

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_all_expenses(expenses)
        elif choice == "3":
            view_summary(expenses)
        elif choice == "4":
            print("\nThank you for using Personal Expense Tracker. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select a valid option (1-4).")


if __name__ == "__main__":
    main()