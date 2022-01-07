import tkinter
from tkinter import *
import custom_button
import main_menu

import utils
from PIL import ImageTk, Image
import random


def load_menu(window, frame):
    frame.pack_forget()
    main_menu.start(window)


def start(window):
    window.title("Graphical Authentication System")
    window.geometry("1280x600")

    segments_frame = Frame(window, height=600, width=1280)
    segments_frame.pack(fill='both', expand=1)

    label = Label(segments_frame, text="Please select the pictures in correct order", font=('Calibri', 20))
    label.pack(padx=400, pady=10)

    ## Draw order image

    canvas = Canvas(segments_frame, width=300, height=250)
    canvas.bind("<Button-1>", utils.callback)
    img = (Image.open("segmentedImages/order.jpg"))
    img = img.resize((300, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(10, 10, anchor=NW, image=img)
    canvas.pack(padx=10, pady=10)

    imgList = utils.getSegmentedImages("circle")
    random.shuffle(imgList)
    imgClickData = []

    for imgPath in imgList:
        var = utils.imageClick(imgPath)
        imgClickData.append(var)

    # Draw shuffled segments

    canvas2 = Canvas(segments_frame, width=200, height=150)
    canvas2.bind("<Button-1>", imgClickData[0].clicked)
    canvas2.place(x=100, y=400)
    img2 = (Image.open(imgList[0]))
    img2 = img2.resize((200, 150), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    canvas2.create_image(10, 10, anchor=NW, image=img2)

    canvas3 = Canvas(segments_frame, width=200, height=150)
    canvas3.bind("<Button-1>", imgClickData[1].clicked)
    canvas3.place(x=400, y=400)
    img3 = (Image.open(imgList[1]))
    img3 = img3.resize((200, 150), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)
    canvas3.create_image(10, 10, anchor=NW, image=img3)

    canvas4 = Canvas(segments_frame, width=200, height=150)
    canvas4.bind("<Button-1>", imgClickData[2].clicked)
    canvas4.place(x=700, y=400)
    img4 = (Image.open(imgList[2]))
    img4 = img4.resize((200, 150), Image.ANTIALIAS)
    img4 = ImageTk.PhotoImage(img4)
    canvas4.create_image(10, 10, anchor=NW, image=img4)

    canvas5 = Canvas(segments_frame, width=200, height=150)
    canvas5.bind("<Button-1>", imgClickData[3].clicked)
    canvas5.place(x=1000, y=400)
    img5 = (Image.open(imgList[3]))
    img5 = img5.resize((200, 150), Image.ANTIALIAS)
    img5 = ImageTk.PhotoImage(img5)
    canvas5.create_image(10, 10, anchor=NW, image=img5)

    custom_button.TkinterCustomButton(master=segments_frame, text="Go Back", height=40, corner_radius=10,
                                      command=lambda: load_menu(window, segments_frame)).place(relx=0.08, rely=0.08,
                                                                                              anchor=CENTER)

    while True:
        window.update_idletasks()
        window.update()

        if utils.checkAllClicked(imgClickData):
            sortedClickList = sorted(imgClickData)

            if (sortedClickList[0].id == 1) and (sortedClickList[1].id == 2) and (sortedClickList[2].id == 3) and (
                    sortedClickList[3].id == 4):
                utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
            else:
                utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")

            utils.setAllUnclicked(imgClickData)
