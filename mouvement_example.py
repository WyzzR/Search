import tkinter as tk
import time
from PIL import Image, ImageTk

class figure():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("900x900")

        self.image_front = Image.open("figure/viewfront.png")
        self.image_back = Image.open("figure/viewback.png")
        self.image_left = Image.open("figure/viewleft.png")
        self.image_right = Image.open("figure/viewright.png")
        # Convert images to Tkinter-compatible format
        self.front = ImageTk.PhotoImage(self.image_front)
        self.back = ImageTk.PhotoImage(self.image_back)
        self.left = ImageTk.PhotoImage(self.image_left)
        self.right = ImageTk.PhotoImage(self.image_right)
        
        self.create_widgets(self.window)
        self.window.mainloop()
    def create_widgets(self,root):
        
        self.canvas =tk.Canvas(root,width=900, height=900)
        self.canvas.bind("<Key>", self.move)
        self.canvas.focus_set()
        self.canvas.pack()
        self.figure = self.canvas.create_image(250, 250, image=self.front)
   
    def move(self,event):
            x, y = 0,0
            if event.char == "w":
                y = -10
                self.canvas.itemconfig(self.figure, image=self.back)
            elif event.char == "a":
                x = -10
                self.canvas.itemconfig(self.figure, image=self.left)
            elif event.char == "s":
                y = 10
                self.canvas.itemconfig(self.figure, image=self.front)
            elif event.char == "d":
                x = 10
                self.canvas.itemconfig(self.figure, image=self.right)
            self.canvas.move(self.figure, x, y)
            time.sleep(0.05)


if __name__ == "__main__":
    figure()
    