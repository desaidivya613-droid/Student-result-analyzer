import tkinter as tk
from tkinter import messagebox

# Function to calculate grade
def calculate_result():
    try:
        name = entry_name.get()
        m1 = int(entry_m1.get())
        m2 = int(entry_m2.get())
        m3 = int(entry_m3.get())

        avg = (m1 + m2 + m3) / 3

        if avg >= 90:
            grade = 'A'
        elif avg >= 75:
            grade = 'B'
        elif avg >= 60:
            grade = 'C'
        else:
            grade = 'D'

        result_text.set(f"{name} | Avg: {avg:.2f} | Grade: {grade}")

    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Clear fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_m1.delete(0, tk.END)
    entry_m2.delete(0, tk.END)
    entry_m3.delete(0, tk.END)
    result_text.set("")

# Main window
root = tk.Tk()
root.title("Student Result Analyzer")
root.geometry("350x300")

# Labels & Entries
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Marks 1").pack()
entry_m1 = tk.Entry(root)
entry_m1.pack()

tk.Label(root, text="Marks 2").pack()
entry_m2 = tk.Entry(root)
entry_m2.pack()

tk.Label(root, text="Marks 3").pack()
entry_m3 = tk.Entry(root)
entry_m3.pack()

# Result display
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, fg="blue").pack(pady=10)

# Buttons
tk.Button(root, text="Calculate", command=calculate_result).pack(pady=5)
tk.Button(root, text="Clear", command=clear_fields).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

# Run app
root.mainloop()