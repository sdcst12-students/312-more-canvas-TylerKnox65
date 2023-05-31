import tkinter as tk
from types import CoroutineType
"""
Task 2
Read the map2.txt file and convert to a map that you can navigate a
rectangle object through. Use images for your map.
You will want to make sure that your rectangle is above the map tiles
Legend:
0 Water
1 Plains
2 Forest
3 Hills
4 Mountains
5 Swamp
6 City
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
f = open('map2.txt')
data = f.read()
water = tk.PhotoImage(file="assets\map.water.png")
plains = tk.PhotoImage(file="assets\map.plains.png")
forest = tk.PhotoImage(file="assets\map.forest.png")
hills = tk.PhotoImage(file="assets\map.hills.png")
mountains = tk.PhotoImage(file="assets\map.mountain.png")
swamp = tk.PhotoImage(file="assets\map.swamp.png")
city = tk.PhotoImage(file="assets\map.city.png")

count = 0
county = 0
countGrid = 0 
data = list(data)
print(data) 
for i in data:
    if i == "0":
        c.create_image(0 + (30 * count),0+(30*county), image=water)
    if i == "1":
        c.create_image(0 + (30 * count),0+(30*county), image=plains)
    if i == "2":
        c.create_image(0 + (30 * count),0+(30*county), image=forest)
    if i == "3":
        c.create_image(0 + (30 * count),0+(30*county), image=hills)
    if i == "4":
        c.create_image(0 + (30 * count),0+(30*county), image=mountains)
    if i == "5":
        c.create_image(0 + (30 * count),0+(30*county), image=swamp)
    if i == "6":
        c.create_image(0 + (30 * count),0+(30*county), image=city)
    count +=1
    countGrid += 1
    if i == "\n":
        county += 1
        count = 0
        countGrid = 0
w.mainloop()