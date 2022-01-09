from tkinter import *
import time


class TrafficLight(Tk):

    def __init__(self):
        self.state = 0
        super().__init__()
        self.title('TrafficLight')
        self.canvas = c = Canvas(self, width=70, height=190, bg="black")
        self.red = c.create_oval(10, 10, 60, 60, fill="#ff0000")
        self.yellow = c.create_oval(10, 70, 60, 120, fill="#808000")
        self.green = c.create_oval(10, 130, 60, 180, fill="#008000")
        c.pack()
        self.update()
        self.after(7000, self.running)

    def running(self):
        if self.state == 0:
            self.state = 1
            self.canvas.itemconfigure(self.red, fill='#800000')
            self.canvas.itemconfigure(self.yellow, fill='#ffff00')
            self.after(2000, self.running)
        elif self.state == 1:
            self.state = 2
            self.canvas.itemconfigure(self.yellow, fill='#808000')
            self.canvas.itemconfigure(self.green, fill='#00ff00')
            self.after(2000, self.running)
        elif self.state == 2:
            self.state = 3
            self.canvas.itemconfigure(self.green, fill='#008000')
            self.canvas.itemconfigure(self.red, fill='#800000')
            self.after(2000, self.running)
        else:
            self.state = 0
            self.canvas.itemconfigure(self.red, fill='#ff0000')
            self.canvas.itemconfigure(self.yellow, fill='#808000')
            self.after(7000, self.running)


root = TrafficLight()
root.mainloop()
