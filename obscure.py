import tkinter
from tkinter import *
import custom_button
import main_menu
import speech_recognition as sr

import utils
from PIL import ImageTk, Image
import random


def load_menu(window, frame):
    frame.pack_forget()
    main_menu.start(window)


original_text = []


def toggle(event):
    input_text = None

    while True:
        e = sr.Recognizer()  # Recognizes all input devices
        with sr.Microphone() as source:  # setting microphone as default input device
            try:
                print("Say Something. Say 'stop' inorder to stop")
                audio = e.listen(source)  # Listens audio
                input_text = e.recognize_google(audio)  # Recognizes text using speech recognition
                if input_text == "stop":  # Break condition
                    break
            except:
                print("Exception occured when trying to record")
        break
    input_text = input_text[:-5]  # Removing stop from the end of line
    input_text = input_text.rstrip()  # Removing \n
    input_text = input_text.lower()  # Converting everything to lowercase
    input_text = input_text.replace(' ', '-')  # Replacing spaces with dashes

    print("Original Text = ", original_text[0])
    print("Input Text = ", input_text)

    if original_text[0] == input_text:
        print("Authenticated")
        utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
    else:
        print("Authentication Failed")
        utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")


def start(window):
    obscuredImages = utils.getObscuredImages()
    num = random.randint(1, len(obscuredImages) - 1)
    filename = obscuredImages[num]  # Filename that will be displayed
    filepath = "obscuredImages/original_obscure.txt"  # File Path

    f = open(filepath, "r")

    while True:
        string = f.readline()  # Reading file line by line
        s1 = string.split(' ')[0]  # Getting first word (filename) of line
        if s1 == filename[0:len(filename) - 4]:  # Don't need the file extension, only name
            break
    # print("Original = ", string)
    string = string[9:]  # Cropping string
    string = string.replace(' ', '-')  # Replacing spaces with dashes
    string = string
    original_text.append(string.rstrip())  # Removing \n
    f.close()

    obscure_frame = Frame(window, height=600, width=1280)
    obscure_frame.pack(fill='both', expand=1)

    window.title("Graphical Authentication System")
    window.geometry("1280x600")

    label = Label(obscure_frame, text="Click on the microphone and speak the words in the following image",
                  font=('Calibri', 20))
    label.pack(padx=40, pady=10)

    canvas = Canvas(obscure_frame, width=450, height=300)
    img = (Image.open("obscuredImages/" + filename))
    img = img.resize((450, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(10, 10, anchor=NW, image=img)
    canvas.pack(padx=10, pady=10)

    canvas2 = Canvas(obscure_frame, width=200, height=170)
    canvas2.bind("<Button-1>", toggle)
    img2 = (Image.open("assets/mic.jpg"))
    img2 = img2.resize((200, 170), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    canvas2.create_image(10, 10, anchor=NW, image=img2)
    canvas2.pack(padx=20, pady=20)

    custom_button.TkinterCustomButton(master=obscure_frame, text="Go Back", height=40, corner_radius=10,
                                      command=lambda: load_menu(window, obscure_frame)).place(relx=0.08, rely=0.08,
                                                                                              anchor=CENTER)

    while True:
        window.update_idletasks()
        window.update()
