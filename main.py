import tkinter as tk
from tkinter import messagebox
import requests

def download_content():
    url = url_entry.get()
    filename = filename_entry.get()
    
    if not url or not filename:
        messagebox.showerror("Input Error", "Please enter both URL and filename.")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        with open(filename, "wb") as file:
            file.write(response.content)
        
        messagebox.showinfo("Success", f"Content downloaded and saved to '{filename}'.")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Download Error", f"Failed to download content: {e}")

# Create the main tkinter window
root = tk.Tk()
root.title("Content Downloader")
root.geometry("400x200")
root.configure(bg="white")

# URL Label and Entry
url_label = tk.Label(root, text="Enter URL:", bg="white", font=("Helvetica", 10))
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Filename Label and Entry
filename_label = tk.Label(root, text="Enter Filename:", bg="white", font=("Helvetica", 10))
filename_label.pack(pady=5)
filename_entry = tk.Entry(root, width=50)
filename_entry.pack(pady=5)

# Download Button
download_button = tk.Button(
    root, 
    text="Download", 
    command=download_content, 
    bg="#4CAF50", 
    fg="white", 
    font=("Helvetica", 12, "bold")
)
download_button.pack(pady=20)

# Run the tkinter event loop
root.mainloop()