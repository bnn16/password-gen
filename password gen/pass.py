import random, string, tkinter
from tkinter import *
import tkinter as tk

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
nums = string.digits
symbols = string.punctuation
samples = lower_case + upper_case + nums + symbols

#generating the password
def random_new():

    entry_pass.delete(0, END)
    #get pw lenght
    #len1 = int(input()) ##this inputs the lenght of the password that is wanted
    passlen = int(entry_box.get())
    password = "".join(random.sample(samples, passlen))

    entry_pass.insert(0, password)

# copy to clip
def clipp():
    root.clipboard_clear() #clears the clipboard
    root.clipboard_append(entry_pass.get()) #copies to clipboard


#making of the GUI
root = tk.Tk()
root.title("Password Gen")
root.iconbitmap("C:/Users/Bogda/Untitled Folder 1/pass.ico")
root.geometry("500x400")

# The frame
label_frame = LabelFrame(root, text = "How long would you like your password to be? : ")
label_frame.pack(pady = 20)

#Entry box for how long you would like your pass to be 
entry_box = Entry(label_frame, font = ("Times New Roman", 16))
entry_box.pack(pady = 20, padx = 20)

#box for the password
entry_pass = Entry(root, text = "", font = ("Times New Roman", 16), bd = 0, bg = "systembuttonface")
entry_pass.pack(pady = 20)

frame = Frame(root)
frame.pack(pady = 20)
#button for new pass
gen_password = Button(frame, text = "Password generate", command = random_new)
gen_password.grid(row = 0, column = 0, padx = 10)

#clipboard
clip = Button(frame, text = "Clipboard copy", command = clipp)
clip.grid(row = 0, column = 1, padx = 10)


root.mainloop()