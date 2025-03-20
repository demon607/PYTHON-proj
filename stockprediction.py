import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Placeholder functions for analysis and prediction
def analyze_stock():
    stock = stock_entry.get()
    if not stock:
        messagebox.showerror("Error", "Please enter a stock ticker")
        return
    result_label.config(text=f"Analyzing {stock}...\n(Placeholder for analysis results)")
    animate_label(result_label)
    display_analysis(stock)

def predict_stock():
    stock = stock_entry.get()
    if not stock:
        messagebox.showerror("Error", "Please enter a stock ticker")
        return

    # Simulate prediction logic
    prediction = random.uniform(100, 500)  # Simulated prediction value
    confidence = random.uniform(70, 99)   # Simulated confidence percentage

    result_text = (f"Prediction for {stock}:\n"
                   f"Price: ${prediction:.2f}\n"
                   f"Confidence: {confidence:.2f}%\n"
                   f"(Placeholder for prediction details)")

    result_label.config(text=result_text)
    stock_entry.config(font=("Helvetica", 14, "bold"), foreground="#FF4500")  # Make ticker bold and orange
    animate_label(result_label)
    display_graph(stock)

def clear_inputs():
    stock_entry.delete(0, tk.END)
    result_label.config(text="")
    clear_graph()

def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

def about_app():
    messagebox.showinfo("About", "Stock Analysis & Prediction App\nVersion 1.0")

def animate_label(label):
    # Simple color animation
    colors = ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1"]
    for i, color in enumerate(colors):
        root.after(100 * i, lambda c=color: label.config(fg=c))

def display_analysis(stock):
    # Placeholder for analysis details
    analysis_details = f"Analysis for {stock}:\n(Placeholder for analysis details)"
    result_label.config(text=analysis_details)

def display_graph(stock):
    clear_graph()
    # Simulate stock price data
    days = np.arange(1, 31)  # Days of the month
    prices = np.random.uniform(100, 500, size=30)  # Random prices

    # Create a Matplotlib figure
    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
    ax.plot(days, prices, marker="o", linestyle="-", color="#6B5B95", label=f"{stock} Prices")
    ax.set_title(f"{stock} Price Prediction", fontsize=14, fontweight="bold")
    ax.set_xlabel("Days", fontsize=12)
    ax.set_ylabel("Price ($)", fontsize=12)
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.6)

    # Customize the appearance of the graph
    ax.set_facecolor("#F0F0F0")  # Set background color
    ax.spines['bottom'].set_color('#DDDDDD')  # Set color of the bottom spine
    ax.spines['bottom'].set_linewidth(2)  # Set width of the bottom spine
    ax.spines['left'].set_color('#DDDDDD')  # Set color of the left spine
    ax.spines['left'].set_linewidth(2)  # Set width of the left spine

    # Embed the plot in the Tkinter app
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def clear_graph():
    for widget in graph_frame.winfo_children():
        widget.destroy()

# Create the main window
root = tk.Tk()
root.title("Stock Prices Analysis and Prediction")
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="#1E1E2E")

# Title label
title_label = tk.Label(root, text="Stock Analysis & Prediction", font=("Helvetica", 20, "bold"), bg="#1E1E2E", fg="#FFDD93")
title_label.pack(pady=10)

# Entry for stock ticker
entry_frame = tk.Frame(root, bg="#1E1E2E")
entry_frame.pack(pady=10)

stock_label = tk.Label(entry_frame, text="Enter Stock Ticker:", font=("Arial", 12), bg="#1E1E2E", fg="white")
stock_label.pack(side=tk.LEFT, padx=5)

stock_entry = ttk.Entry(entry_frame, font=("Arial", 12))
stock_entry.pack(side=tk.LEFT, padx=5)

# Buttons for analysis and prediction
button_frame = tk.Frame(root, bg="#1E1E2E")
button_frame.pack(pady=20)

analyze_button = ttk.Button(button_frame, text="Analyze", command=analyze_stock)
analyze_button.pack(side=tk.LEFT, padx=10)

predict_button = ttk.Button(button_frame, text="Predict", command=predict_stock)
predict_button.pack(side=tk.LEFT, padx=10)

clear_button = ttk.Button(button_frame, text="Clear", command=clear_inputs)
clear_button.pack(side=tk.LEFT, padx=10)

exit_button = ttk.Button(button_frame, text="Exit", command=exit_app)
exit_button.pack(side=tk.LEFT, padx=10)

# Additional Button for About Section
about_button = ttk.Button(root, text="About", command=about_app)
about_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#1E1E2E", fg="white")
result_label.pack(pady=20)

# Graph frame for displaying the stock graph
graph_frame = tk.Frame(root, bg="#1E1E2E")
graph_frame.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="Stock Predictions powered by stockers", font=("Arial", 10, "italic"), bg="#1E1E2E", fg="#F7CAC9")
footer_label.pack(side=tk.BOTTOM, pady=10)

# Start the main loop
root.mainloop()
