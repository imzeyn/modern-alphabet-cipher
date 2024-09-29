# -*- coding: utf-8 -*-
# Python Version: 3.12.3
import random, base64
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

class AlphabetCipher:
    def __init__(self):
        pass

    def encode_text(self, text, coordinates):
        encoded_text = text
        for coord in coordinates:
            cipher = AlphabetCipherWithSeed(int(coord))
            encoded_text, _ = cipher.encode_text(encoded_text)

        return encoded_text

    def decode_text(self, text, coordinates):
        decoded_text = text
        for coord in reversed(coordinates):
            cipher = AlphabetCipherWithSeed(int(coord))  # Her koordinatı int olarak kullan
            decoded_text = cipher.decode_text(decoded_text)
        return decoded_text

class AlphabetCipherWithSeed:
    def __init__(self, seed_number):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        self.new_alphabet = self.generate_new_alphabet(seed_number)

    def generate_new_alphabet(self, seed_number):
        random.seed(seed_number)
        s_list = list(self.alphabet)
        random.shuffle(s_list)
        return ''.join(s_list)

    def encode_text(self, text):
        text = base64.b64encode(text.encode("UTF-8")).decode("UTF-8")
        encoded_text = ""
        indexes = []

        for char in text:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                encoded_char = self.new_alphabet[index]
                encoded_text += encoded_char
                indexes.append(self.new_alphabet.index(encoded_char))
            else:
                encoded_text += char

        return encoded_text, indexes

    def decode_text(self, encoded_text):
        decoded_text = ""

        for char in encoded_text:
            if char in self.new_alphabet:
                index = self.new_alphabet.index(char)
                decoded_char = self.alphabet[index]
                decoded_text += decoded_char
            else:
                decoded_text += char

        return base64.b64decode(decoded_text.encode("UTF-8")).decode("UTF-8")

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Modern Alphabet Cipher")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)  


        input_frame = ttk.Frame(master, padding="10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label1 = ttk.Label(input_frame, text="Text:")
        self.label1.grid(row=0, column=0, sticky=tk.W)

        self.text_entry = tk.Text(input_frame, height=10, width=50)
        self.text_entry.grid(row=1, column=0, sticky=(tk.W, tk.E))

        self.label3 = ttk.Label(input_frame, text="Coordinates (comma-separated):")
        self.label3.grid(row=2, column=0, sticky=tk.W)

        self.coordinates_entry = ttk.Entry(input_frame, width=50)
        self.coordinates_entry.grid(row=3, column=0, sticky=(tk.W, tk.E))

        # Frame for the buttons
        button_frame = ttk.Frame(master, padding="10")
        button_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

        self.encode_button = ttk.Button(button_frame, text="Encode", command=self.encode)
        self.encode_button.grid(row=0, column=0, padx=5)

        self.decode_button = ttk.Button(button_frame, text="Decode", command=self.decode)
        self.decode_button.grid(row=0, column=1, padx=5)

        self.load_button = ttk.Button(button_frame, text="Load from File", command=self.load_from_file)
        self.load_button.grid(row=0, column=2, padx=5)

        self.save_button = ttk.Button(button_frame, text="Save Result", command=self.save_result)
        self.save_button.grid(row=0, column=3, padx=5)


        result_frame = ttk.Frame(master, padding="10")
        result_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))

        self.result_label = ttk.Label(result_frame, text="Result:")
        self.result_label.grid(row=0, column=0, sticky=tk.W)

        self.result_text = tk.Text(result_frame, height=10, width=50)
        self.result_text.grid(row=1, column=0, sticky=(tk.W, tk.E))

        style = ttk.Style()
        style.configure("TButton", padding=6)
        style.configure("TLabel", font=("Arial", 10))

        for frame in [input_frame, button_frame, result_frame]:
            frame.columnconfigure(0, weight=1)
            frame.rowconfigure(0, weight=1)

    def encode(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        coordinates = self.coordinates_entry.get().strip().split(',')

        if not text or not coordinates:
            messagebox.showerror("Input Error", "Please enter text and coordinates.")
            return

        try:
            coordinates = [int(coord.strip()) for coord in coordinates if coord.strip()]
            cipher = AlphabetCipher()
            encoded_text = cipher.encode_text(text, coordinates)

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"{encoded_text}")

        except ValueError:
            messagebox.showerror("Input Error", "Coordinates must be numbers.")

    def decode(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        coordinates = self.coordinates_entry.get().strip().split(',')

        if not text or not coordinates:
            messagebox.showerror("Input Error", "Please enter text and coordinates.")
            return

        try:
            coordinates = [float(coord.strip()) for coord in coordinates if coord.strip()]
            cipher = AlphabetCipher()
            decoded_text = cipher.decode_text(text, coordinates)

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"{decoded_text}")

        except ValueError:
            messagebox.showerror("Input Error", "Coordinates must be numbers.")

    def load_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            self.text_entry.delete("1.0", tk.END)
            self.text_entry.insert(tk.END, content)

    def save_result(self):
        result = self.result_text.get("1.0", tk.END).strip()
        if not result:
            messagebox.showerror("Save Error", "No result to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(result)
            messagebox.showinfo("Save Successful", "Result saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()