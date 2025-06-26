import tkinter as tk
import pyttsx3
from tkinter import StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def replace_word():
    sentence = input_text.get("1.0", tk.END).strip()
    old_word = old_entry.get().strip()
    new_word = new_entry.get().strip()
    result = sentence.replace(old_word, new_word)
    output_text.config(state='normal')
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state='disabled')
    preview.set(result)
    update_count(result)

def update_count(text):
    words = len(text.split())
    chars = len(text)
    word_count.set(f"Words: {words}")
    char_count.set(f"Characters: {chars}")

def clear_all():
    input_text.delete("1.0", tk.END)
    old_entry.delete(0, tk.END)
    new_entry.delete(0, tk.END)
    output_text.config(state='normal')
    output_text.delete("1.0", tk.END)
    output_text.config(state='disabled')
    preview.set("")
    word_count.set("Words: 0")
    char_count.set("Characters: 0")

def speak_input():
    sentence = input_text.get("1.0", tk.END).strip()
    speak(sentence)

def speak_output():
    sentence = output_text.get("1.0", tk.END).strip()
    speak(sentence)

def toggle_dark_mode():
    style.theme_use("darkly" if style.theme.name == "flatly" else "flatly")

app = ttk.Window(themename="flatly")
app.title("Elite Word Replacer")
app.geometry("700x600")
app.resizable(False, False)

style = ttk.Style()

title = ttk.Label(app, text="Elite Word Replacer", font=("Segoe UI", 20, "bold"))
title.pack(pady=10)

frame = ttk.Frame(app)
frame.pack(pady=5)

input_label = ttk.Label(frame, text="Input Sentence:")
input_label.grid(row=0, column=0, sticky='w')
input_text = tk.Text(frame, width=80, height=5, font=("Segoe UI", 11))
input_text.grid(row=1, column=0, columnspan=3, pady=5)

old_label = ttk.Label(frame, text="Word to Replace:")
old_label.grid(row=2, column=0, sticky='w')
old_entry = ttk.Entry(frame, width=30)
old_entry.grid(row=3, column=0, padx=5, pady=5)

new_label = ttk.Label(frame, text="New Word:")
new_label.grid(row=2, column=1, sticky='w')
new_entry = ttk.Entry(frame, width=30)
new_entry.grid(row=3, column=1, padx=5, pady=5)

replace_btn = ttk.Button(frame, text="Replace Word", command=replace_word, bootstyle=SUCCESS)
replace_btn.grid(row=3, column=2, padx=5)

output_label = ttk.Label(app, text="Modified Sentence:")
output_label.pack(pady=(10, 0))
output_text = tk.Text(app, width=80, height=5, font=("Segoe UI", 11), state='disabled')
output_text.pack(pady=5)

preview = StringVar()
word_count = StringVar(value="Words: 0")
char_count = StringVar(value="Characters: 0")

info_frame = ttk.Frame(app)
info_frame.pack()

preview_label = ttk.Label(info_frame, textvariable=preview, wraplength=650)
preview_label.grid(row=0, column=0, columnspan=2, pady=5)

count_label1 = ttk.Label(info_frame, textvariable=word_count)
count_label1.grid(row=1, column=0, padx=5, sticky='w')

count_label2 = ttk.Label(info_frame, textvariable=char_count)
count_label2.grid(row=1, column=1, padx=5, sticky='w')

btn_frame = ttk.Frame(app)
btn_frame.pack(pady=10)

speak_input_btn = ttk.Button(btn_frame, text="🔊 Read Input", command=speak_input, bootstyle=INFO)
speak_input_btn.grid(row=0, column=0, padx=5)

speak_output_btn = ttk.Button(btn_frame, text="🔊 Read Output", command=speak_output, bootstyle=INFO)
speak_output_btn.grid(row=0, column=1, padx=5)

clear_btn = ttk.Button(btn_frame, text="🧹 Clear All", command=clear_all, bootstyle=WARNING)
clear_btn.grid(row=0, column=2, padx=5)

dark_mode_btn = ttk.Button(btn_frame, text="🌓 Toggle Dark Mode", command=toggle_dark_mode, bootstyle=SECONDARY)
dark_mode_btn.grid(row=0, column=3, padx=5)

app.mainloop()
