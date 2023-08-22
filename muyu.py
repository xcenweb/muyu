import tkinter as tk
from animation import ImageAnimation

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Animation") 
    root.geometry("600x338+550+260")
    root.configure(bg="gray")
    ImageAnimation(root) # 动画类
    root.mainloop()