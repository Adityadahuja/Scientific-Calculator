import tkinter as tk
import math

root = tk.Tk()
root.title("Calculator • by Aditya Dahuja")
root.geometry("400x600")
root.configure(bg="#000000")
root.resizable(False, False)

expression = ""
angle_mode = "DEG"
equation = tk.StringVar()
equation.set("0")
mode_text = tk.StringVar()
mode_text.set("DEG")

def calculate(expr):
    expr = expr.replace('π', str(math.pi)).replace('e', str(math.e)).replace('^', '**')
    return str(eval(expr))

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        expression = calculate(expression)
        equation.set(expression)
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("0")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression if expression else "0")

def toggle_mode():
    global angle_mode
    angle_mode = "RAD" if angle_mode == "DEG" else "DEG"
    mode_text.set(angle_mode)

def trig(func):
    global expression
    try:
        val = float(calculate(expression))
        if angle_mode == "DEG":
            val = math.radians(val)
        expression = str(getattr(math, func)(val))
        equation.set(expression)
    except:
        equation.set("error")
        expression = ""

def sqrt_op():
    global expression
    try:
        expression = str(math.sqrt(float(calculate(expression))))
        equation.set(expression)
    except:
        equation.set("error")
        expression = ""

def deg_rad():
    global expression
    try:
        val = float(calculate(expression))
        expression = str(math.radians(val))
        equation.set(expression)
    except:
        equation.set("error")
        expression = ""

def rad_deg():
    global expression
    try:
        val = float(calculate(expression))
        expression = str(math.degrees(val))
        equation.set(expression)
    except:
        equation.set("error")
        expression = ""

def log_op():
    global expression
    try:
        val = float(calculate(expression))
        expression = str(math.log10(val))
        equation.set(expression)
    except:
        equation.set("error")
        expression = ""

def toggle_sign():
    global expression
    if expression and expression[0] != '-':
        expression = '-' + expression
    elif expression.startswith('-'):
        expression = expression[1:]
    equation.set(expression if expression else "0")

top_frame = tk.Frame(root, bg="#000000")
top_frame.pack(fill="both", expand=True, padx=15, pady=20)

mode_label = tk.Label(top_frame, textvariable=mode_text, font=("Arial", 10, "bold"), bg="#000000", fg="#4a9eff")
mode_label.pack(anchor="nw", pady=5)

display_entry = tk.Label(top_frame, textvariable=equation, font=("Arial", 36, "bold"), bg="#000000", fg="#ffffff", anchor="e")
display_entry.pack(fill="both", expand=True, padx=10, pady=10)

sig = tk.Label(top_frame, text="by Aditya Dahuja", font=("Arial", 8), bg="#000000", fg="#666666")
sig.pack(anchor="se", pady=5)

btn_frame = tk.Frame(root, bg="#000000")
btn_frame.pack(fill="both", expand=True, padx=15, pady=(0, 20))

for i in range(5):
    btn_frame.grid_columnconfigure(i, weight=1)
for i in range(6):
    btn_frame.grid_rowconfigure(i, weight=1)

buttons = [
    ("AC", 0, 0, clear, "#4a4a4a"),
    ("<x", 0, 1, backspace, "#4a4a4a"),
    ("+/-", 0, 2, toggle_sign, "#4a4a4a"),
    ("°→rad", 0, 3, deg_rad, "#4a4a4a"),
    ("+", 0, 4, lambda: press("+"), "#4a9eff"),
    
    ("7", 1, 0, lambda: press("7"), "#2a2a2a"),
    ("8", 1, 1, lambda: press("8"), "#2a2a2a"),
    ("9", 1, 2, lambda: press("9"), "#2a2a2a"),
    ("sin", 1, 3, lambda: trig("sin"), "#4a4a4a"),
    ("×", 1, 4, lambda: press("*"), "#4a9eff"),
    
    ("4", 2, 0, lambda: press("4"), "#2a2a2a"),
    ("5", 2, 1, lambda: press("5"), "#2a2a2a"),
    ("6", 2, 2, lambda: press("6"), "#2a2a2a"),
    ("cos", 2, 3, lambda: trig("cos"), "#4a4a4a"),
    ("−", 2, 4, lambda: press("-"), "#4a9eff"),
    
    ("1", 3, 0, lambda: press("1"), "#2a2a2a"),
    ("2", 3, 1, lambda: press("2"), "#2a2a2a"),
    ("3", 3, 2, lambda: press("3"), "#2a2a2a"),
    ("tan", 3, 3, lambda: trig("tan"), "#4a4a4a"),
    ("√", 3, 4, sqrt_op, "#4a9eff"),
    
    ("0", 4, 0, lambda: press("0"), "#2a2a2a"),
    (".", 4, 1, lambda: press("."), "#2a2a2a"),
    ("π", 4, 2, lambda: press("π"), "#4a4a4a"),
    ("log", 4, 3, log_op, "#4a4a4a"),
    ("=", 4, 4, equal, "#4a9eff"),
]

for text, r, c, cmd, color in buttons:
    btn = tk.Button(btn_frame, text=text, font=("Arial", 14, "bold"), bg=color, fg="white", 
                    bd=0, activebackground=color, command=cmd, highlightthickness=0)
    btn.grid(row=r, column=c, sticky="nsew", padx=6, pady=8)

if __name__ == "__main__":
    root.mainloop()
