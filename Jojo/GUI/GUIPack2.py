import tkinter as tk
from tkinter import ttk

def create_window():
    window = tk.Tk()
    window.title("Multiple Frame Layout")

    # Top Frame
    top_frame = ttk.Frame(window)
    top_frame.pack(side=tk.TOP, fill=tk.X)

    # Left Frame and Right Frame
    left_frame = ttk.Frame(window, width=window.winfo_screenwidth() // 3)
    left_frame.pack(side=tk.LEFT, fill=tk.Y)

    right_frame = ttk.Frame(window, width=2 * window.winfo_screenwidth() // 3)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Left Frame Subdivisions
    left_top_frame = ttk.Frame(left_frame)
    left_top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    left_bottom_frame = ttk.Frame(left_frame)
    left_bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Bottom Frame
    bottom_frame = ttk.Frame(window)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

    # Add widgets to frames (replace with your desired widgets)
    label1 = ttk.Label(top_frame, text="Top Frame")
    label1.pack()

    label2 = ttk.Label(left_top_frame, text="Left Top Frame")
    label2.pack()

    label3 = ttk.Label(left_bottom_frame, text="Left Bottom Frame")
    label3.pack()

    label4 = ttk.Label(right_frame, text="Right Frame")
    label4.pack()

    label5 = ttk.Label(bottom_frame, text="Bottom Frame")
    label5.pack()

    window.mainloop()

if __name__ == "__main__":
    create_window()