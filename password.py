from tkinter import messagebox
import copy
import hashlib
from random import randint

import tkinter
from tkinter import *
import custom_button
import main_menu

import utils
from PIL import ImageTk, Image
from tkinter import Entry

s_image = []
s_image.append("")

def load_menu(window, frame):
    frame.pack_forget()
    main_menu.start(window)


# saves image selected by user
def clicked(canvas, img_name, event):
    canvas.config(highlightthickness=1, highlightbackground="black")
    s_image[0] = img_name;
    # print(s_image[0])


# authenticate credentials provided by users
def authenticate(selected_image, selected_password, selected_name):
    # checks if there is no empty entry
    if selected_name == "":
        messagebox.showinfo("Login System", "Please enter the Username")
    elif selected_password == "":
        messagebox.showinfo("Login System", "Please enter the Password")
    elif selected_name == "" and selected_password == "":
        messagebox.showinfo("Login System", "Please enter the Username and Password")
    # print("hiii",selected_image)

    # taking hash of password entered as its hash stored in backend
    h = hashlib.new('sha512_256')
    h.update(selected_password.encode())
    selected_password = h.hexdigest()
    filepath = "credentialImages/orig_credentials.txt"  # File Path
    f = open(filepath, "r")
    name = ""
    password = ""
    image = ""
    str = ""
    isUser = 0
    # file reading to get original credentials
    while True:
        string = f.readline()  # Reading file line by line
        if string == "":
            if (isUser == 0):
                print("username not exist")
                messagebox.showinfo("Login System", "password is not correct")
            break
        info = string.split(" ")
        name = copy.deepcopy(info[0])
        password = copy.deepcopy(info[1])
        image = copy.deepcopy(info[2])
        name = name.rstrip()
        password = password.rstrip()
        image = image.rstrip()

        # checks the credentials by somparing with original one
        if name == selected_name:
            isUser = 1
            if password == selected_password:
                if image == selected_image:
                    print("authenticated!!")
                    messagebox.showinfo("Login System", "authenticated!!")
                    break
                else:
                    print("image is not correct")
                    messagebox.showinfo("Login System", "image is not correct")

                    break
            else:
                print("password is not correct")
                messagebox.showinfo("Login System", "password is not correct")
                break


# login page canvas
def create_canvas(window):
    window.title("Login Page")
    window.geometry("1280x600")

    root = Frame(window, height=600, width=1280)
    root.pack(fill='both', expand=1)

    #root.title("Login Page")
    #root.resizable(0, 0)
    width = 700
    height = 700
    # image class names
    img_name1 = "cat"
    img_name2 = "flower"
    img_name3 = "mouse"

    # Generates random number to display images
    num = randint(0, 2)
    print("Random number = ", num)
    selected_image = ""

    # getting image paths from utils
    imgList = utils.getCredentialImages()

    # canvas for title
    canvas = Canvas(root, width=width, height=height, bd=0, highlightthickness=0)
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_image(0, 0, anchor='nw')
    label = Label(root, text="Login Page", font=("Ariel 15 bold"))
    canvas.create_window(550, 40, anchor="nw", window=label)

    # canvas for username title
    user_label = Label(root, text="User name:", font=("Ariel 12 bold"))
    canvas.create_window(480, 130, anchor="nw", window=user_label)

    # canvas for password title
    password_label = Label(root, text="Password:", font=("Ariel 12 bold"))
    canvas.create_window(480, 210, anchor="nw", window=password_label)

    # usernmae input feild display
    user_entry = Entry(root, font=("Ariel 12"))
    user_entry.focus()
    selected_name = user_entry.get()
    canvas.create_window(580, 130, anchor="nw", window=user_entry)

    # password input feild display
    pas = StringVar()
    password_entry = Entry(root, textvar=pas, font=("Ariel 12"), show="*")
    selected_password = password_entry.get()
    canvas.create_window(580, 210, anchor="nw", window=password_entry)

    # Random image display from first class
    canvas2 = Canvas(root, width=110, height=70)
    canvas2.bind("<Button-1>",
                 lambda event: clicked(canvas2, img_name1, event))  # binding button to check if image is clicked
    canvas2.place(x=450, y=290)
    img2 = (Image.open("credentialImages/" + imgList[num]))
    img2 = img2.resize((90, 60), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    canvas2.create_image(10, 10, anchor="nw", image=img2)

    # Random image display from second class
    canvas3 = Canvas(root, width=110, height=70)
    canvas3.bind("<Button-1>",
                 lambda event: clicked(canvas3, img_name2, event))  # binding button to check if image is clicked
    canvas3.place(x=600, y=290)
    img3 = (Image.open("credentialImages/" + imgList[num + 3]))
    img3 = img3.resize((90, 60), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)
    canvas3.create_image(10, 10, anchor="nw", image=img3)

    # Random image display from third class
    canvas4 = Canvas(root, width=110, height=70)
    canvas4.bind("<Button-1>",
                 lambda event: clicked(canvas4, img_name3, event))  # binding button to check if image is clicked
    canvas4.place(x=750, y=290)
    img4 = (Image.open("credentialImages/" + imgList[num + 6]))
    img4 = img4.resize((90, 60), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)
    canvas4.create_image(10, 10, anchor="nw", image=img4)

    # login button display
    # calls authenticate on click with credentials as arguments
    login = custom_button.TkinterCustomButton(master=root, text="Log In", height=40, corner_radius=10,
                   command=lambda: authenticate(s_image[0], password_entry.get(), user_entry.get())).place(relx=0.5, rely=0.7, anchor=CENTER)

    custom_button.TkinterCustomButton(master=root, text="Go Back", height=40, corner_radius=10,
                                      command=lambda: load_menu(window, root)).place(relx=0.08, rely=0.08,
                                                                                              anchor=CENTER)

    window.mainloop()


def start(window):
    create_canvas(window)
