#!python3

# Find an image to use as a sprite from the Internet.
# Modify the image (flipping horizontally is a quick way to do that) so that you have
# a second, different image. Use the tkObject.after() method to animate it.
# Note: You can find sprite sheets or tile sheets on the internet to help you!

import tkinter as tk
import random
w = tk.Tk()
w.geometry("600x400")
w.title("sample")

c = tk.Canvas(width=550,height=450,background="#cccccc",bd="2")
c.pack()
sprite = tk.PhotoImage(file="assets\sprite.png")
x = 4
char = c.create_image(100,100, image=sprite)
def animate(i=x):
    if i == None:
        print(i)
    global anim, x
    if i == 1:
        anim = tk.PhotoImage(file="assets\sprite2.png")
    if i == 2:
        anim = tk.PhotoImage(file="assets\sprite3.png")
    if i == 3:
        anim = tk.PhotoImage(file="assets\sprite4.png")
    if i == 4:
        anim = tk.PhotoImage(file="assets\sprite.png")
    
    if x == 2:
        x == 1
    else:
        x == 1

    c.itemconfigure(char, image=anim)
    w.after(500, animate)

def keyPress(e):
    print(e)
    print(e.keycode, e.keysym, e.x, e.y)
    animate(random.randint(1,4))
    if e.keysym == "Left":
            c.move(char,-5,0)    
    if e.keysym == "Right":
            c.move(char,5,0)    
    if e.keysym == "Up":
            c.move(char,0,-5) 
    if e.keysym == "Down":
            c.move(char,0,5) 
    
w.bind("<Left>",keyPress)
w.bind("<Right>",keyPress)
w.bind("<Up>",keyPress)
w.bind("<Down>",keyPress)
w.after(1000, animate)

w.mainloop()