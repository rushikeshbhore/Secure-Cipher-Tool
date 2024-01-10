import tkinter as tk

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

def encrypt():
    shift = int(entry_shift.get())
    plaintext = text_original.get("1.0", tk.END).strip()

    if plaintext:
        encrypted_text = caesar_encrypt(plaintext, shift)
        text_encrypted.delete("1.0", tk.END)
        text_encrypted.insert("1.0", encrypted_text)

def decrypt():
    shift = int(entry_shift.get())
    ciphertext = text_encrypted.get("1.0", tk.END).strip()

    if ciphertext:
        decrypted_text = caesar_decrypt(ciphertext, shift)
        text_decrypted.delete("1.0", tk.END)
        text_decrypted.insert("1.0", decrypted_text)

def reset():
    entry_shift.delete(0, tk.END)
    text_original.delete("1.0", tk.END)
    text_encrypted.delete("1.0", tk.END)
    text_decrypted.delete("1.0", tk.END)

# Create the main Tkinter window
root = tk.Tk()
root.title("Secure Cipher Tool")
root.geometry("600x610")
root.configure(bg="#000000")  # Background color
root.resizable(0, 0)

image_icon = tk.PhotoImage(file="keys.png")
root.iconphoto(False, image_icon)

# Labels and Entries
label_shift = tk.Label(root, text="Enter The Key:", font=("verdana bold", 10))
label_shift.pack(pady=10)

entry_shift = tk.Entry(root, font=("verdana bold", 10),show="*", bd=2)
entry_shift.pack(pady=5)

label_original = tk.Label(root, text="Enter The Plain Text:", font=("verdana bold", 10))
label_original.pack(pady=10)

text_original = tk.Text(root, height=5, width=50, bd=3)
text_original.pack(pady=5)

label_encrypted = tk.Label(root, text="Encrypted Text:", font=("verdana bold", 10))
label_encrypted.pack(pady=10)

text_encrypted = tk.Text(root, height=5, width=50, bd=3)
text_encrypted.pack(pady=5)

label_decrypted = tk.Label(root, text="Decrypted Text:", font=("verdana bold", 10))
label_decrypted.pack(pady=10)

text_decrypted = tk.Text(root, height=5, width=50, bd=3)
text_decrypted.pack(pady=5)

# Button Frame
btn_encrypt = tk.Button(root, text="ENCRYPT", height=2, width=20, bg="#ed3833", fg="white", bd=2, command=encrypt)
btn_encrypt.place(x=145, y=500)

# Decrypt Button
btn_decrypt = tk.Button(root, text="DECRYPT", height=2, width=20, bg="#00bd56", fg="white", bd=2, command=decrypt)
btn_decrypt.place(x=310, y=500)

# Reset Button
btn_reset = tk.Button(root, text="RESET", height=2, width=44, bg="#1089ff", fg="white", bd=2, command=reset)
btn_reset.place(x=144, y=550)

root.mainloop()

root.mainloop()
