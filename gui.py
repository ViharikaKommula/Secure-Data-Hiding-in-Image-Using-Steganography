import tkinter as tk
from tkinter import filedialog, messagebox
from encode_lsb_encrypted import encode_lsb, generate_key
from decode_lsb_encrypted import decode_lsb

def run_gui():
    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            entry_image_path.delete(0, tk.END)
            entry_image_path.insert(0, file_path)

    def encode_data():
        image_path = entry_image_path.get()
        data = entry_data.get()
        if image_path and data:
            try:
                key = generate_key()
                encoded_image_path = encode_lsb(image_path, data, key)
                messagebox.showinfo("Success", f"Data encoded in {encoded_image_path}\nKey: {key.decode()}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    def decode_data():
        image_path = entry_image_path.get()
        key = entry_key.get().encode()
        if image_path and key:
            try:
                decoded_message = decode_lsb(image_path, key)
                messagebox.showinfo("Decoded Message", decoded_message)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    root = tk.Tk()
    root.title("Steganography Tool with Encryption")

    tk.Label(root, text="Image Path:").pack()
    entry_image_path = tk.Entry(root, width=50)
    entry_image_path.pack()

    tk.Button(root, text="Browse", command=open_file).pack()

    tk.Label(root, text="Data to Encode: ").pack()
    entry_data = tk.Entry(root, width=50)
    entry_data.pack()

    tk.Label(root, text="Encryption Key:").pack()
    entry_key = tk.Entry(root, width=50)
    entry_key.pack()

    tk.Button(root, text="Encode", command=encode_data).pack()
    tk.Button(root, text="Decode", command=decode_data).pack()

    root.mainloop()