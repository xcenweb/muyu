import tkinter as tk
from PIL import ImageTk, Image
from playsound import playsound
import threading
import sys

class ImageAnimation:
    def __init__(self, root):
        self.root = root
        self.animation_count = 0

        self.original_image = Image.open(sys.path[0] + "\\muyu.jpg")
        self.image_path = sys.path[0] + "\\muyu.jpg"
        self.image = self.original_image.resize((200, 200))
        self.background = Image.new("RGB", (400, 400), color="gray")
        self.offset = (int((400 - 200) / 2), int((400 - 200) / 2))
        self.background.paste(self.image, self.offset)
        self.photo = ImageTk.PhotoImage(self.background)

        self.img_label = tk.Label(self.root, image=self.photo, bg="gray")
        self.img_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        try:
            with open(sys.path[0] + "\\muyu.txt", "r") as f:
                self.animation_count = int(f.read())
        except FileNotFoundError:
            pass

        self.count_label = tk.Label(self.root, text=f"功德无量: {self.animation_count}  ", fg="red", bg="gray",
                                    font=("Arial", 15, "bold"), bd=0)
        self.count_label.place(relx=1, rely=1, anchor=tk.SE)

        self.root.bind("<space>", self.on_space)
        self.root.wm_attributes("-topmost", 1)
    
    def play_sound(self):
        playsound(sys.path[0] + "\\muyu.mp3")

    def animate(self, scale):
        size = int(200 + scale * 10)
        image = self.original_image.resize((size, size))
        background = Image.new("RGB", (400, 400), color="gray")
        offset = (int((400 - size) / 2), int((400 - size) / 2))
        background.paste(image, offset)
        photo = ImageTk.PhotoImage(background)
        self.img_label.config(image=photo)
        self.img_label.image = photo

        if scale < 1.0:
            self.root.after(20, self.animate, scale + 0.2)
        else:
            self.root.after(20, self.animate_reverse, scale - 0.2)

    def animate_reverse(self, scale):
        size = int(200 + scale * 10)
        image = self.original_image.resize((size, size))
        background = Image.new("RGB", (400, 400), color="gray")
        offset = (int((400 - size) / 2), int((400 - size) / 2))
        background.paste(image, offset)
        photo = ImageTk.PhotoImage(background)
        self.img_label.config(image=photo)
        self.img_label.image = photo

        if scale > 0.2:
            self.root.after(20, self.animate_reverse, scale - 0.2)
        else:
            self.root.after(20, self.final_animation)

    def final_animation(self):
        image = self.original_image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        self.img_label.config(image=photo)
        self.img_label.image = photo

        self.animation_count += 1
        self.update_animation_count()

    def on_space(self, event):
        threading.Thread(target=self.play_sound).start()
        self.animate(0.0)

    def update_animation_count(self):
        self.count_label.config(text=f"功德无量: {self.animation_count}  ")
        with open(sys.path[0] + "\\muyu.txt", "w") as f:
            f.write(str(self.animation_count))