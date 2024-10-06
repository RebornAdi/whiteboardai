import google.generativeai as genai
import os
import pyttsx3
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
import tkinter as tk
from tkinter import Canvas
from PIL import ImageGrab
import pyautogui
def AI():    
    genai.configure(api_key='AIzaSyDkXCF9pwFnauJcN4_FwX8YIDQtkw7HoPk')
    import PIL.Image
    model = genai.GenerativeModel("gemini-1.5-flash")
    question = PIL.Image.open("media/screenshot.png")
    response = model.generate_content(["Tell me about this", question])
    print(response.text)
    say(response.text)
class WhiteboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Whiteboard")
        
        self.brush_size = 5  # Default brush size
        self.color = 'black'  # Default color (for marker)

        # Set up canvas (whiteboard)
        self.canvas = Canvas(root, bg='white', width=1000, height=500)
        self.canvas.pack()

        # Bind mouse events to draw on the whiteboard
        self.canvas.bind('<B1-Motion>', self.draw)

        # Screenshot button
        self.screenshot_button = tk.Button(root, text="Process", command=self.take_screenshot)
        self.screenshot_button.pack()

        # Clear button
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_board)
        self.clear_button.pack()
        
        # Eraser button
        self.eraser_button = tk.Button(root, text="Eraser", command=self.use_eraser)
        self.eraser_button.pack()

        # Marker button
        self.marker_button = tk.Button(root, text="Marker", command=self.use_marker)
        self.marker_button.pack()

        # Increase brush size button
        self.increase_brush_button = tk.Button(root, text="Increase Brush Size", command=self.increase_brush_size)
        self.increase_brush_button.pack()

        # Decrease brush size button
        self.decrease_brush_button = tk.Button(root, text="Decrease Brush Size", command=self.decrease_brush_size)
        self.decrease_brush_button.pack()

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x, y, x + self.brush_size, y + self.brush_size, fill=self.color, outline=self.color)

    def take_screenshot(self):
        # Capture the canvas area as a screenshot
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()

        ImageGrab.grab().crop((x, y, x1, y1)).save("media/screenshot.png")
        print("Screenshot taken and saved as 'screenshot.png'")
        AI()
        # Clear the canvas after taking the screenshot
        self.clear_board()

    def clear_board(self):
        # Clear the whiteboard by deleting all items on the canvas
        self.canvas.delete("all")

    def use_eraser(self):
        # Set the color to white for erasing
        self.color = 'white'

    def use_marker(self):
        # Set the color to black for drawing
        self.color = 'black'

    def increase_brush_size(self):
        # Increase the brush size for a bolder marker
        self.brush_size += 2

    def decrease_brush_size(self):
        # Decrease the brush size (prevent it from getting too small)
        if self.brush_size > 2:
            self.brush_size -= 2

if __name__ == "__main__":
    root = tk.Tk()
    app = WhiteboardApp(root)
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = WhiteboardApp(root)
    root.mainloop()
    