from tkinter import *
import pandas as pd
import random
import os
BACKGROUND_COLOR = "#B1DDC6"

# Creating new Flash Cards -----------------------------------------------------------#
if os.path.exists("data/words_to_learn.csv"):
    data = pd.read_csv("data/words_to_learn.csv")
    if len(data) == 0:
        print("No more data.")
        exit(0)
else:
    data = pd.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")
current_card = {}


def flip_card():
    canvas.itemconfig(french_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_card['English'], fill="white")
    canvas.itemconfig(flash_card_img, image=back_img)


def know_word():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(word_label, text=current_card['French'], fill="black")
    canvas.itemconfig(french_label, text="French", fill="black")
    canvas.itemconfig(flash_card_img, image=front_card_img)
    flip_timer = window.after(3000, func=flip_card)
    data_dict.remove(current_card)
    words_to_learn = pd.DataFrame(data_dict)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)


def do_not_know_word():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(word_label, text=current_card['French'], fill="black")
    canvas.itemconfig(french_label, text="French", fill="black")
    canvas.itemconfig(flash_card_img, image=front_card_img)
    flip_timer = window.after(3000, func=flip_card)

# UI Setup ---------------------------------------------------------------------------#
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)

front_card_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

flash_card_img = canvas.create_image(400, 263, image=front_card_img)
french_label = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=do_not_know_word)
right_button = Button(image=right_image, highlightthickness=0, command=know_word)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)
do_not_know_word()


window.mainloop()
