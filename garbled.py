import tkinter
from tkinter import *
import custom_button
import main_menu

import utils
from PIL import ImageTk, Image
from tkinter import Entry
import random


def load_menu(window, frame):
    frame.pack_forget()
    main_menu.start(window)


def start(window):
    filepath = "garbledImages/original_garbled.txt"  # File Path
    garbledImages = utils.getGarbledImages()
    num = random.randint(0, len(garbledImages) - 1)
    filename = garbledImages[num]

    f = open(filepath, "r")

    while True:
        string = f.readline()  # Reading file line by line
        s1 = string.split(' ')[0]  # Getting first word (filename) of line
        if s1 == filename[0:len(filename) - 4]:  # Don't need the file extension, only name
            break
    # print("Original = ", string)
    string = string[9:]  # Cropping string
    string = string.replace(' ', '-')  # Replacing spaces with dashes
    original_text = string
    original_text = original_text.rstrip()  # Removing \n
    f.close()

    print(original_text)
    print(filename)

    window.title("Graphical Authentication System")
    window.geometry("1280x600")

    garbled_frame = Frame(window, height=600, width=1280)
    garbled_frame.pack(fill='both', expand=1)

    label = Label(garbled_frame, text="Type the words in the image", font=('Calibri', 20))
    label.pack(padx=40, pady=10)

    canvas = Canvas(garbled_frame, width=450, height=300)
    img = (Image.open("garbledImages/" + filename))
    img = img.resize((450, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(10, 10, anchor=NW, image=img)
    canvas.place(relx=0.45, rely=0.5, anchor=E)

    def check():
        entered_text = input.get()
        if entered_text == original_text:
            print("Authenticated")
            utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
        else:
            print("Authentication Failed")
            utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")

    input = StringVar()
    Label(garbled_frame, text="Enter word", font="ariel 16 bold").place(relx=0.7, rely=0.40, anchor=CENTER)
    Entry(garbled_frame, textvariable=input, font="ariel 12 bold", relief="groove", width=30, justify=CENTER).place(
        relx=0.7,
        rely=0.5,
        anchor=CENTER)

    custom_button.TkinterCustomButton(master=garbled_frame, text="Check", height=40, corner_radius=10,
                                      command=check).place(relx=0.7, rely=0.6, anchor=CENTER)

    custom_button.TkinterCustomButton(master=garbled_frame, text="Go Back", height=40, corner_radius=10,
                                      command=lambda: load_menu(window, garbled_frame)).place(relx=0.08, rely=0.08, anchor=CENTER)

    while True:
        window.update_idletasks()
        window.update()
