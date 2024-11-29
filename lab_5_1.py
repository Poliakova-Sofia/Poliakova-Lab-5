import tkinter as tk
from tkinter import messagebox
class PowerCheckerApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Checking the powers of N")
    self.root.geometry("500x300")
    self.root.configure(bg="pink")
    
    # entering the number N
    self.label_n = tk.Label(root, text=" Enter the number N (> 1):" , bg="pink", fg="black")
    self.label_n.pack()
    self.entry_n = tk.Entry(root, width=20)
    self.entry_n.pack()

    # entering a list of K numbers
    self.label_k = tk.Label(root, text=" Enter 10 positive numbers separated by a space:", bg="pink", fg="black")
    self.label_k.pack()
    self.entry_k = tk.Entry(root, width=30)
    self.entry_k.pack()

    # button to perform a check
    self.check_button = tk.Button(root, text="Check", bg="light blue", fg="black", command=self.check_powers)
    self.check_button.pack()

    # displaying the result
    self.result_label = tk.Label(root, text="", fg="black", bg="pink")
    self.result_label.pack()

  def check_powers(self):
     try:
       # reading the number N
       n = int(self.entry_n.get())
       if n <= 1:
           raise ValueError("The number N must be greater than 1!")

       # reading a list of K numbers
       k_values = list(map(int, self.entry_k.get().split()))
       if len(k_values) != 10:
           raise ValueError("It is necessary to enter exactly 10 numbers!")
       if any(k <= 0 for k in k_values):
           raise ValueError("All numbers in the list must be positive!")

       # checking each number from the list
       count = 0
       for k in k_values:
           if self.is_power_n(k, n):
               count += 1

       # outputting the result
       self.result_label.config(text=f"The number of powers of a number {n}: {count}")

     except ValueError as e:
       # display an error message
       messagebox.showerror("Error", str(e))

  @staticmethod
  def is_power_n(k, n):
      
      if k <= 0 or n <= 1:
          return False
      power = 1
      while power < k:
          power *= n
      return power == k

if __name__ == "__main__":
  root = tk.Tk()
  app = PowerCheckerApp(root)
  root.mainloop()
