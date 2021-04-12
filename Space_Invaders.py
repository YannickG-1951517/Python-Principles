from tkinter import Tk, Canvas
import keyboard
import time

class Screen:
    """Screen class"""
    def makeScreen(self):
        HEIGHT = 700
        WIDTH = 700
        window = Tk()
        canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000012")
        canvas.pack()
        canvas.mainloop()

    def printx(self):
        self.canvas.delete("all")
        x1, y1, x2, y2 = 10, 20, 30, 40
        distance = 30
        for i in range(3):
            for cube in range(23):
                self.canvas.create_rectangle(x1, y1, x2, y2, fill='#FFFFFF')
                x1 += distance
                x2 += distance
                #time.sleep(1)
            x1, x2 = 10, 30
            y1 += distance
            y2 += distance
        self.canvas.update()
        print('x')

    def inputs(self):
        keyboard.add_hotkey('alt', self.printx)


    def __init__(self):
        self.inputs()
        self.HEIGHT = 700
        self.WIDTH = 700
        self.window = Tk()
        self.canvas = Canvas(self.window, width=self.WIDTH, height=self.HEIGHT, bg="#000012")
        self.canvas.pack()
        self.canvas.mainloop()
        # self.makeScreen()




test = Screen()
"""
def on_press():
    print('x')


keyboard.add_hotkey('alt', on_press)
"""

