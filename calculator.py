import tkinter as tk

def on_click(event):
    global current_text
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(current_text.get())
            current_text.set(result)
        except Exception as e:
            current_text.set("Error")
    elif text == "C":
        current_text.set("")
    else:
        current_text.set(current_text.get() + text)

root = tk.Tk()
root.title("Simple Calculator")

current_text = tk.StringVar()
entry = tk.Entry(root, textvariable=current_text, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    ('7', 1, 0, 1, 1), ('8', 1, 1, 1, 1), ('9', 1, 2, 1, 1), ('/', 1, 3, 1, 1),
    ('4', 2, 0, 1, 1), ('5', 2, 1, 1, 1), ('6', 2, 2, 1, 1), ('*', 2, 3, 1, 1),
    ('1', 3, 0, 1, 1), ('2', 3, 1, 1, 1), ('3', 3, 2, 1, 1), ('-', 3, 3, 1, 1),
    ('0', 4, 0, 1, 1), ('.', 4, 1, 1, 1), ('C', 4, 2, 1, 1), ('+', 4, 3, 1, 1),
    ('=', 5, 0, 1, 4)
]


for (text, row, column, rowspan, columnspan) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), relief="groove")
    button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
    button.bind("<Button-1>", on_click)

root.mainloop()
