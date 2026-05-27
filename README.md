# 🧮 Calculator

A sleek, dark-themed scientific calculator built with Python and Tkinter.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational)


---

## ✨ Features

- **Basic arithmetic** — addition, subtraction, multiplication, division
- **Scientific functions** — sin, cos, tan, log, square root
- **Constants** — π (pi) and Euler's number (e)
- **Angle mode toggle** — switch between Degrees and Radians
- **Degree ↔ Radian conversion** — convert values on the fly
- **Sign toggle** — flip between positive and negative
- **Backspace** — delete the last character
- **Clean dark UI** — black background with blue accents

---

## 📸 Preview

```
┌─────────────────────────────┐
│ DEG                         │
│                       0     │
│                by Aditya    │
├──────┬──────┬──────┬────────┤
│  AC  │  <x  │ +/-  │ °→rad  │
│  7   │  8   │  9   │  sin   │
│  4   │  5   │  6   │  cos   │
│  1   │  2   │  3   │  tan   │
│  0   │  .   │  π   │  log   │
└──────┴──────┴──────┴────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Tkinter (included with most Python installations)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Adityadahuja/calculator.git
   cd calculator
   ```

2. **Run the calculator**
   ```bash
   python calculator.py
   ```

> **Note:** Tkinter is bundled with standard Python on Windows and macOS. On Linux, install it with:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## 🖱️ Usage

| Button | Action |
|--------|--------|
| `AC` | Clear all input |
| `<x` | Backspace (delete last character) |
| `+/-` | Toggle positive/negative |
| `°→rad` | Convert current value from degrees to radians |
| `DEG` label | Shows current angle mode (click toggles DEG ↔ RAD) |
| `sin` / `cos` / `tan` | Trigonometric functions (respects angle mode) |
| `√` | Square root of current value |
| `log` | Base-10 logarithm of current value |
| `π` | Insert the value of pi |
| `=` | Evaluate the expression |

---

## 🗂️ Project Structure

```
calculator/
└── calculator.py   # Main application file
```

---

## 🛠️ Built With

- [Python](https://www.python.org/) — core language
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — GUI framework
- [math](https://docs.python.org/3/library/math.html) — mathematical functions

---

## 👤 Author

**Aditya Dahuja** — [github.com/Adityadahuja](https://github.com/Adityadahuja)

---


