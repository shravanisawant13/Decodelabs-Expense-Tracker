# Decodelabs-Expense-Tracker
# 💰 Expense Tracker

A simple **command-line Expense Tracker application built using Python**.
This project allows users to enter expenses under different categories and automatically calculates category-wise expenses and the total amount spent.

## 🚀 Features

* 🏷️ Add expenses by category
* 💵 Enter expense amounts
* 📊 Display category-wise expense totals
* 🧮 Calculate total spending
* 🔄 Add multiple expenses
* ⛔ Type `done` to finish the input
* 💻 Simple command-line interface

## 🛠️ Technologies Used

* **Python 3**
* Python Dictionaries
* `while` Loop
* `if-else` Statements
* `input()` and `print()`
* `float()` for expense amounts
* Dictionary methods
* Basic arithmetic operations

## 📂 Project Structure

```text
Expense-Tracker/
│
├── Expense_Tracker.py
├── README.md
├── screenshot1.png
└── screenshot2.png
```

## ▶️ How to Run

### 1. Install Python

Make sure **Python 3** is installed on your computer.

### 2. Clone the Repository

```bash
git clone <your-github-repository-link>
```

### 3. Open the Project Folder

```bash
cd Expense-Tracker
```

### 4. Run the Program

```bash
python Expense_Tracker.py
```

## 💻 How the Program Works

The program starts with an empty dictionary called `expenses` and a `total` variable to store the overall spending.

### 1️⃣ Enter Expense Category

The program asks the user to enter an expense category.

```text
Enter expense category (or 'done' to finish): food
```

Users can enter categories such as:

```text
food
travel
clothes
books
```

### 2️⃣ Enter Expense Amount

After entering a category, the program asks for the expense amount.

```text
Enter expense amount: ₹120
```

The amount is converted into a number using `float()`.

### 3️⃣ Store Expenses by Category

If the category already exists, the new amount is added to its existing value. Otherwise, a new category is created in the dictionary.

For example:

```text
food: ₹120.00
travel: ₹2000.00
clothes: ₹700.00
books: ₹270.00
```

### 4️⃣ Calculate Total Spending

Each expense amount is added to the `total` variable to calculate the overall spending.

Example:

```text
Total Spent: ₹3090.00
```

### 5️⃣ Finish and Display Summary

When the user enters `done`, the program stops accepting new expenses and displays the expense summary.

The summary displays each category and its amount, followed by the total amount spent.

## 📊 Sample Output

```text
========== EXPENSE SUMMARY ==========
food: ₹120.00
travel: ₹2000.00
clothes: ₹700.00
books: ₹270.00
-------------------------------------
Total Spent: ₹3090.00
=====================================
```

## 🔄 Program Flow

```text
          START
            ↓
    Enter Expense Category
            ↓
       Is it "done"?
        ↙         ↘
      YES          NO
       ↓            ↓
Show Expense    Enter Amount
  Summary            ↓
       ↓       Store Category
      END            ↓
              Update Total
                    ↓
          Enter Next Expense
                    ↓
                  Repeat
```

## 📸 Screenshots

### 💻 Entering Expenses

The screenshot below shows the program running in VS Code and accepting different expense categories and amounts.

![Expense Tracker Input](screenshot1.png)

### 📊 Expense Summary

The screenshot below shows the final category-wise expense summary and total spending.

![Expense Tracker Summary](screenshot2.png)

## 📚 Learning Outcomes

By developing this project, I learned:

* How to use Python dictionaries
* How to store expenses using categories
* How to take user input
* How to use `while` loops
* How to use conditional statements
* How to perform calculations in Python
* How to calculate category-wise totals
* How to create a simple command-line application

## 🔮 Future Improvements

The Expense Tracker can be improved by adding:

* 📅 Date for each expense
* 💾 Save expenses permanently in a file
* 📈 Monthly expense reports
* 📊 Expense charts and graphs
* 🔍 Search expenses
* ✏️ Edit or delete expenses
* 💰 Set a monthly budget
* 🖥️ Create a graphical user interface

## 👩‍💻 Author

**Shravani**

---

⭐ **If you find this project useful, consider giving the repository a star!**
