import tkinter as tk
from tkinter import messagebox
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class FunctionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("lab4_2-320-3-Poliakova-Sofiia")
        self.root.geometry("800x600")  

        # initialization of parameters
        self.T = 0.05
        self.N = 100
        self.K = 3
        self.Z = 0.25
        self.U = 0.1

        # graph
        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # creation of interface elements
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(side=tk.LEFT, padx=10, pady=10)

        # entering parameters
        label_T = tk.Label(frame, text="T (time step):")
        label_T.grid(row=0, column=0)
        self.entry_T = tk.Entry(frame)
        self.entry_T.insert(0, str(self.T))
        self.entry_T.grid(row=0, column=1)

        label_N = tk.Label(frame, text="N (number of points):")
        label_N.grid(row=1, column=0)
        self.entry_N = tk.Entry(frame)
        self.entry_N.insert(0, str(self.N))
        self.entry_N.grid(row=1, column=1)

        label_K = tk.Label(frame, text="K (constant):")
        label_K.grid(row=2, column=0)
        self.entry_K = tk.Entry(frame)
        self.entry_K.insert(0, str(self.K))
        self.entry_K.grid(row=2, column=1)

        label_Z = tk.Label(frame, text="Z (damping factor):")
        label_Z.grid(row=3, column=0)
        self.entry_Z = tk.Entry(frame)
        self.entry_Z.insert(0, str(self.Z))
        self.entry_Z.grid(row=3, column=1)

        label_U = tk.Label(frame, text="U (input):")
        label_U.grid(row=4, column=0)
        self.entry_U = tk.Entry(frame)
        self.entry_U.insert(0, str(self.U))
        self.entry_U.grid(row=4, column=1)

        # button to update parameters
        button_update = tk.Button(frame, text="Update and Plot", command=self.update_params)
        button_update.grid(row=5, column=0, columnspan=2, pady=10)

    def update_params(self):
        try:
            # update settings
            self.T = float(self.entry_T.get())
            self.N = int(self.entry_N.get())
            self.K = int(self.entry_K.get())
            self.Z = float(self.entry_Z.get())
            self.U = float(self.entry_U.get())

            # calculation of values
            k_values, y_values = self.calculate_values(self.T, self.N, self.K, self.Z, self.U)
            self.save_data_to_file(k_values, y_values, 'output.txt')
            self.plot_data(k_values, y_values, f"Function for Variant {self.K}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input values. Please check the values entered.")

    def calculate_values(self, T, N, K, Z, U):
        T0 = 2 * T / N
        k_values = np.linspace(0, N * T0, N)
        y_values = np.zeros(N)

        # using the formula for y[k]
        for k in range(2, N):
            y_values[k] = 2 * (1 - (Z * T0) / T) * y_values[k - 1] + ((2 * Z * T0) / T - 1 - (T0**2 / T**2)) * y_values[k - 2] + ((K * T0**2) / T**2) * U
        return k_values, y_values

    def save_data_to_file(self, k_values, y_values, filename):
        with open(filename, 'w') as f:
            for k, y in zip(k_values, y_values):
                f.write(f"{k} # {y}\n")
        messagebox.showinfo("Info", f"Data saved to {filename}")

    def plot_data(self, k_values, y_values, title):
        self.ax.clear()  
        self.ax.plot(k_values, y_values, label='Function')
        self.ax.set_title(title)
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Function Value')
        self.ax.grid(True)
        self.ax.legend()
        self.canvas.draw()  

root = tk.Tk()
app = FunctionApp(root)
root.mainloop()
