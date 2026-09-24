import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output.config(text="Result: " + str(result))
    except:
        output.config(text="Invalid Expression")

window = tk.Tk()
window.title("Calculator")
window.geometry("350x300")

tk.Label(window, text="GUI Calculator",
         font=("Arial", 18)).pack(pady=20)

entry = tk.Entry(window, font=("Arial", 16), width=20)
entry.pack(pady=10)

tk.Button(window, text="Calculate",
          command=calculate).pack(pady=10)

output = tk.Label(window, text="Result:",
                  font=("Arial", 14))
output.pack(pady=20)

window.mainloop()