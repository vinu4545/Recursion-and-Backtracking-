# 🔁 Recursion and Backtracking

## 📌 Overview

This repository contains a curated collection of coding problems solved using **Recursion** and **Backtracking** techniques. The goal of this project is to strengthen problem-solving skills by breaking problems into smaller subproblems and exploring all valid possibilities systematically.

These techniques are widely used in **DSA**, **competitive programming**, and **technical interviews**.

---

## 🧠 What You Will Learn

* How recursion works internally (base case & recursive case)
* How backtracking explores and reverts decisions
* Writing clean and efficient recursive solutions
* Visualizing recursive calls using recursion trees

---

## 🗂️ Topics Covered

* Basic Recursion Problems
* Backtracking Fundamentals
* Subsets & Combinations
* Permutations
* Combination Sum
* N-Queens Problem
* Sudoku Solver
* Palindrome Partitioning

---

## 🌳 Example: Recursion Tree (Combination Sum)

### Problem

Given an array of candidates and a target, find all unique combinations where the chosen numbers sum to the target.

### Example Input

```
candidates = [2, 3]
target = 7
```

### Recursion Tree Visualization

```
combinationSum(7)
│
├── take 2 → remaining = 5
│   ├── take 2 → remaining = 3
│   │   ├── take 2 → remaining = 1 ❌
│   │   └── take 3 → remaining = 0 ✅ [2,2,3]
│   └── take 3 → remaining = 2
│       └── take 2 → remaining = 0 ✅ [2,3,2]
│
└── take 3 → remaining = 4
    └── take 2 → remaining = 2
        └── take 2 → remaining = 0 ✅ [3,2,2]
```

✔ The tree shows **decision making**, **branching**, and **backtracking** clearly.

---

## 🔙 Backtracking Flow (Generic)

```
Choose → Explore → Unchoose
```

Steps:

1. Choose an option
2. Recurse to explore further
3. Backtrack (undo the choice)

---

## 📁 Project Structure

```
Recursion-and-Backtracking/
│
├── recursion/
│   ├── factorial.py
│   ├── fibonacci.py
│   └── power.py
│
├── backtracking/
│   ├── combination_sum.py
│   ├── permutations.py
│   ├── subsets.py
│   ├── n_queens.py
│   └── sudoku_solver.py
│
└── README.md
```

---

## ⚙️ How to Use

1. Clone the repository

```
git clone https://github.com/vinu4545/recursion-and-backtracking-
```

2. Navigate to any problem file
3. Run using your preferred language environment

---

## 🎯 Who This Repository Is For

* Beginners learning recursion
* Students preparing for exams
* DSA & interview preparation

---

## 🚀 Future Enhancements

* Add visual diagrams for all problems
* Add time & space complexity analysis
* Add step-by-step dry runs

---

## 🤝 Contributions

Contributions are welcome! Feel free to fork the repository and add new problems or optimize existing solutions.

---

## ⭐ If You Like This Repo

Give it a ⭐ to support and stay motivated!

Happy Coding 😊
