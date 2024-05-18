
import customtkinter
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import random
from customtkinter import filedialog
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import tensorflow as tf
import numpy as np

def preprocess_image(image_path, size):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Resize the image
    image = cv2.resize(image, (size, size))
    # Reshape the image to match model input shape
    image = image.reshape(-1, size, size, 1)
    # Normalize the image
    image = image / 255.0
    return image
def predict_label(image_path):
    # Load and preprocess the image
    #image = Image.open(image_path)  # Convert to grayscale
    
    preprocessed_image = preprocess_image(image_path, 64)

    # Perform prediction
    prediction = model.predict(preprocessed_image)
    predicted_label = np.argmax(prediction)
    print(predicted_label)
    return class_names[predicted_label]

def submit():
    file_path = image_label.cget("text")
    if file_path:
        predicted_label = predict_label(file_path)
        output_label.configure(text=f"'هذا حرف ال  '{predicted_label}")
        SelectBtn.configure(text="Select another image")



def select_image(): 
    file_path = filedialog.askopenfilename()
    
    if file_path:
        image_label.configure(text=file_path)
        display_image(file_path)
        submit()


        
def display_image(file_path):
    photo = customtkinter.CTkImage(
    light_image=Image.open(os.path.join(file_path)),
    dark_image=Image.open(os.path.join(file_path)),
    size=(500, 500),
    )
    #image = Image.open(file_path)
    #image = image.resize((64, 64))  
    #photo = ImageTk.PhotoImage(image)
    image_label.configure(image=photo,compound="top",text_color="#fff",fg_color="#222222")
    #image_label.image = photo
photo = customtkinter.CTkImage(
    light_image=Image.open(os.path.join("assets/Rectangle 3101.png")),
    dark_image=Image.open(os.path.join("assets/Rectangle 3101.png")),
    size=(500, 500),
)

class_names =['أ', 'ئ', 'ال', 'ب', 'ة', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'لا', 'م', 'ن', 'ه', 'و', 'ي']    
model = tf.keras.models.load_model('models/finalmodel.h5')

root = customtkinter.CTk()
root.wm_attributes("-alpha",0.9)
root.title("Arabic Sign Language Translator")
root.configure(fg_color="#222222")
root.iconbitmap("assets/Rectangle-3100.ico")
root.attributes("-fullscreen", True)

root.after(0, lambda: root.state("zoomed"))
customtkinter.set_widget_scaling(0.8)

SelectBtn = customtkinter.CTkButton(
        root,
        text="Select Image",
        width=787,
        height=100,
        fg_color="#444",
        hover_color="#333",
        corner_radius=0,
        font=("Inter", 40),
        text_color="#fff",
        command = select_image
    )

output_label = customtkinter.CTkLabel(root, text="", font=("Inter", 60),)

image_frame = customtkinter.CTkFrame(
    root,
    corner_radius=0,
    border_width=0,
    fg_color="#fff",
    width=500,
    height=500
)

image_frame.pack(pady=(110,50))
output_label.pack(pady=50)
SelectBtn.pack(pady=50)

image_label = customtkinter.CTkLabel(image_frame, text="", image = photo)
image_label.pack()










def iconify():
    root.iconify()


def maximize():
    root.state("zoomed")


def close():
    root.destroy()


red_icon = customtkinter.CTkImage(
    light_image=Image.open(os.path.join("assets/red.png")),
    dark_image=Image.open(os.path.join("assets/red.png")),
    size=(38, 38),
)
green_icon = customtkinter.CTkImage(
    light_image=Image.open(os.path.join("assets/green.png")),
    dark_image=Image.open(os.path.join("assets/green.png")),
    size=(38, 38),
)
yellow_icon = customtkinter.CTkImage(
    light_image=Image.open(os.path.join("assets/yellow.png")),
    dark_image=Image.open(os.path.join("assets/yellow.png")),
    size=(38, 38),
)

red_icon_hoverd = customtkinter.CTkImage(
    light_image=Image.open(os.path.join("assets/red_click.png")),
    dark_image=Image.open(os.path.join("assets/red_click.png")),
    size=(38, 38),
)
green_icon_hoverd = customtkinter.CTkImage(
    light_image=Image.open(os.path.join("assets/green_click.png")),
    dark_image=Image.open(os.path.join("assets/green_click.png")),
    size=(38, 38),
)
yellow_icon_hoverd = customtkinter.CTkImage(
    light_image=Image.open(os.path.join("assets/yellow_click.png")),
    dark_image=Image.open(os.path.join("assets/yellow_click.png")),
    size=(38, 38),
)

red_button = customtkinter.CTkButton(
    root,
    text="",
    width=38,
    height=38,
    image=red_icon,
    fg_color=("#222222", "#222222"),
    hover=False,
    corner_radius=0,
    command=close,

)
green_button = customtkinter.CTkButton(
    root,
    text="",
    width=38,
    height=38,
    image=green_icon,
    fg_color=("#222222", "#222222"),
    hover=False,
    corner_radius=0,
)
yellow_button = customtkinter.CTkButton(
    root,
    text="",
    width=38,
    height=38,
    image=yellow_icon,
    fg_color=("#222222", "#222222"),
    hover=False,
    corner_radius=0,
    command=iconify,

)

red_button.place(x=26, y=22)
green_button.place(x=73.27, y=22)
yellow_button.place(x=120.04, y=22)


def change_to_hoverd_icon(event):
    red_button.configure(image=red_icon_hoverd)
    yellow_button.configure(image=yellow_icon_hoverd)


def change_to_normal_icon(event):
    red_button.configure(image=red_icon)
    yellow_button.configure(image=yellow_icon)


red_button.bind("<Enter>", change_to_hoverd_icon)
red_button.bind("<Leave>", change_to_normal_icon)

green_button.bind("<Enter>", change_to_hoverd_icon)
green_button.bind("<Leave>", change_to_normal_icon)

yellow_button.bind("<Enter>", change_to_hoverd_icon)
yellow_button.bind("<Leave>", change_to_normal_icon)







root.mainloop()
