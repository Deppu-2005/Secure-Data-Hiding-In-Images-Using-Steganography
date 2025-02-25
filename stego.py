import cv2
import os
import string
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image, ImageTk

def select_image():
    global img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if img_path:
        img = Image.open(img_path)
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)
        lbl_img.config(image=img)
        lbl_img.image = img

def hide_message():
    msg = entry_msg.get()
    password = entry_pass.get()
    if not img_path or not msg or not password:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    encrypted_message = password + '|' + msg + '|END'  # Store password + message together with an end marker
    img = cv2.imread(img_path)
    d = {chr(i): i for i in range(255)}
    n, m, z = 0, 0, 0
    
    for char in encrypted_message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3
    
    cv2.imwrite("encryptedImage.png", img)
    messagebox.showinfo("Success", "Message hidden in encryptedImage.png")

def decrypt_message():
    img = cv2.imread("encryptedImage.png")
    c = {i: chr(i) for i in range(255)}
    n, m, z = 0, 0, 0
    extracted_data = ""
    
    try:
        while True:
            char = c.get(img[n, m, z], None)
            if char is None or char == '|END':
                break
            extracted_data += char
            n += 1
            m += 1
            z = (z + 1) % 3
    except KeyError:
        pass  # Stop when invalid character is reached
    
    return extracted_data

def extract_message():
    extracted_data = decrypt_message()
    try:
        stored_password, message = extracted_data.split('|', 1)
    except ValueError:
        messagebox.showerror("Error", "Failed to extract message!")
        return
    
    user_password = simpledialog.askstring("Password Required", "Enter password for decryption:", show='*')
    
    if user_password == stored_password:
        messagebox.showinfo("Decryption", f"Decrypted Message: {message.replace('|END', '')}")
    else:
        messagebox.showerror("Error", "Incorrect passcode!")

# GUI Setup
root = tk.Tk()
root.title("Image Steganography")
root.geometry("400x500")

btn_select = tk.Button(root, text="Select Image", command=select_image)
btn_select.pack()

lbl_img = tk.Label(root)
lbl_img.pack()

tk.Label(root, text="Enter Message:").pack()
entry_msg = tk.Entry(root, show="*")
entry_msg.pack()

tk.Label(root, text="Enter Passcode:").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

btn_hide = tk.Button(root, text="Hide Message", command=hide_message)
btn_hide.pack()

btn_extract = tk.Button(root, text="Extract Message", command=extract_message)
btn_extract.pack()

root.mainloop()
