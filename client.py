import requests
import tkinter as tk
from tkinter import filedialog, messagebox

API_BASE_URL = "XXXXXXXXX"  

def upload_file():
    """Uploads a selected file to the Flask API."""
    file_path = filedialog.askopenfilename()
    
    if not file_path:
        return  
    
    try:
        with open(file_path, "rb") as file:
            files = {"file": file}
            response = requests.post(f"{API_BASE_URL}/upload", files=files)
        
        result = response.json()
        
        if response.status_code == 200:
            messagebox.showinfo("Success", f"File uploaded: {result['filename']}")
        else:
            messagebox.showerror("Error", result.get("error", "Unknown error"))
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to upload file:\n{e}")

def list_files():
    """Fetches and displays a list of uploaded files."""
    try:
        response = requests.get(f"{API_BASE_URL}/files")
        result = response.json()
        
        if response.status_code == 200:
            files = "\n".join(result["files"]) if result["files"] else "No files uploaded yet."
            messagebox.showinfo("Uploaded Files", files)
        else:
            messagebox.showerror("Error", result.get("error", "Unknown error"))
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch files:\n{e}")

root = tk.Tk()
root.title("Flask File Upload Client")
root.geometry("300x200")

upload_button = tk.Button(root, text="Upload File", command=upload_file, width=20)
upload_button.pack(pady=20)

list_button = tk.Button(root, text="List Uploaded Files", command=list_files, width=20)
list_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit, width=20)
exit_button.pack(pady=10)

root.mainloop()
