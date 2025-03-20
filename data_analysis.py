import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Analysis App")
        self.root.geometry("900x600")
        self.root.configure(bg="#f4f4f9")

        self.filepath = None
        self.df = None

        self.create_widgets()

    def create_widgets(self):
        # Header Section
        header_frame = tk.Frame(self.root, bg="#4caf50")
        header_frame.pack(fill=tk.X)

        header_label = tk.Label(header_frame, text="Data Analysis App", font=("Arial", 20, "bold"), fg="white", bg="#4caf50")
        header_label.pack(pady=10)

        # File Upload Section
        file_frame = tk.Frame(self.root, bg="#f4f4f9")
        file_frame.pack(pady=20)

        upload_button = tk.Button(file_frame, text="Upload CSV", command=self.load_file, font=("Arial", 12), bg="#4caf50", fg="white", padx=20, pady=5, borderwidth=0, activebackground="#45a049")
        upload_button.pack()

        self.file_label = tk.Label(file_frame, text="No file selected", font=("Arial", 10), fg="#888888", bg="#f4f4f9")
        self.file_label.pack(pady=5)

        # Dataframe Display Section
        self.table_frame = tk.Frame(self.root, bg="#f4f4f9")
        self.table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Analysis Section
        analysis_frame = tk.Frame(self.root, bg="#f4f4f9")
        analysis_frame.pack(fill=tk.X, pady=10)

        summary_button = tk.Button(analysis_frame, text="Show Summary", command=self.show_summary, font=("Arial", 12), bg="#2196f3", fg="white", padx=20, pady=5, borderwidth=0, activebackground="#1e88e5")
        summary_button.pack(side=tk.LEFT, padx=10)

        plot_button = tk.Button(analysis_frame, text="Show Plot", command=self.show_plot, font=("Arial", 12), bg="#ff5722", fg="white", padx=20, pady=5, borderwidth=0, activebackground="#e64a19")
        plot_button.pack(side=tk.LEFT, padx=10)

    def load_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if self.filepath:
            self.file_label.config(text=self.filepath)
            try:
                self.df = pd.read_csv(self.filepath)
                self.display_table()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {e}")

    def display_table(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        if self.df is not None:
            tree = ttk.Treeview(self.table_frame, columns=list(self.df.columns), show="headings", height=15)

            for col in self.df.columns:
                tree.heading(col, text=col)
                tree.column(col, anchor=tk.W, width=100)

            for index, row in self.df.iterrows():
                tree.insert("", tk.END, values=list(row))

            tree.pack(fill=tk.BOTH, expand=True)

    def show_summary(self):
        if self.df is not None:
            summary = self.df.describe()
            messagebox.showinfo("Summary", summary.to_string())
        else:
            messagebox.showerror("Error", "No data loaded!")

    def show_plot(self):
        if self.df is not None:
            if len(self.df.columns) < 2:
                messagebox.showerror("Error", "The dataset must have at least two columns for plotting!")
                return

            column1, column2 = self.df.columns[:2]

            fig, ax = plt.subplots()
            ax.scatter(self.df[column1], self.df[column2], color="#4caf50")
            ax.set_title(f"Scatter Plot: {column1} vs {column2}", fontsize=14)
            ax.set_xlabel(column1)
            ax.set_ylabel(column2)

            plot_window = tk.Toplevel(self.root)
            plot_window.title("Scatter Plot")
            canvas = FigureCanvasTkAgg(fig, master=plot_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        else:
            messagebox.showerror("Error", "No data loaded!")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalysisApp(root)
    root.mainloop()
