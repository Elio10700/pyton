import os
import tkinter as tk
from tkinter import messagebox

def shutdown():
    confirm = messagebox.askyesno("Confirm Shutdown", "Are you sure you want to shut down?")
    if confirm:
        os.system("shutdown /s /t 0")

def restart():
    confirm = messagebox.askyesno("Confirm Restart", "Are you sure you want to restart?")
    if confirm:
        os.system("shutdown /r /t 0")

# Create the window
root = tk.Tk()
root.title("Shutdown/Restart Tool")
root.geometry("300x150")
root.resizable(False, False)

# Buttons
shutdown_btn = tk.Button(root, text="Shutdown", command=shutdown, bg="red", fg="white", font=("Arial", 12))
shutdown_btn.pack(pady=10)

restart_btn = tk.Button(root, text="Restart", command=restart, bg="blue", fg="white", font=("Arial", 12))
restart_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", command=root.destroy, bg="gray", fg="white", font=("Arial", 12))
exit_btn.pack(pady=10)

root.mainloop()
