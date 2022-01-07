# Import the required libraries
from tkinter import *
from tkinter import font
import custom_button
import garbled
import obscure
import password
import segments


def load_garbled(window, menu_frame):
    menu_frame.pack_forget()
    garbled.start(window)


def load_obscured(window, menu_frame):
    menu_frame.pack_forget()
    obscure.start(window)


def load_segmented(window, menu_frame):
    menu_frame.pack_forget()
    segments.start(window)


def load_password(window, menu_frame):
    menu_frame.pack_forget()
    password.start(window)


def start(win):
    win.geometry("1280x600")
    win.title("Graphical Authentication System")

    menu_frame = Frame(win, height=600, width=1280)
    menu_frame.pack(fill='both', expand=1)

    label = Label(menu_frame, text="Graphical Authentication System", font=('Freestyle Script', 54))
    label.pack(padx=40, pady=30)

    btn_height = 90
    btn_width = 450
    btn_font = ('Trebuchet MS', 14)

    btn1 = custom_button.TkinterCustomButton(master=menu_frame, text="Test Garbled Images", text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=10,
                                             command=lambda: load_garbled(win, menu_frame)).place(relx=0.3, rely=0.4,
                                                                                                  anchor=CENTER)
    btn2 = custom_button.TkinterCustomButton(master=menu_frame, text="Test Segmented Images", text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=10,
                                             command=lambda: load_segmented(win, menu_frame)).place(relx=0.3,
                                                                                                    rely=0.7,
                                                                                                    anchor=CENTER)
    btn3 = custom_button.TkinterCustomButton(master=menu_frame, text="Test Obscured Images", text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=10,
                                             command=lambda: load_obscured(win, menu_frame)).place(relx=0.7,
                                                                                                   rely=0.4,
                                                                                                   anchor=CENTER)
    btn4 = custom_button.TkinterCustomButton(master=menu_frame, text="Test Password/Image Authentication",
                                             text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=10,
                                             command=lambda: load_password(win, menu_frame)).place(relx=0.7,
                                                                                                   rely=0.7,
                                                                                                   anchor=CENTER)

    win.mainloop()


if __name__ == "__main__":
    win = Tk()
    start(win)
