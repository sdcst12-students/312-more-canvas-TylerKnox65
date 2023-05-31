import tkinter as tk
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""

'''
*****************************
  *   *    ****  **     ** **
* * *   ** *   *    * *    **
* * ** * * *** ** * *** *****
* **   * * *      *   *     *
* ** ***   *** ****** *** * *
*    *** ***   *      **  * *
******** *** *** ******  ** *
*   *        *   *      **  *
* *   ******** ********** ***
* ****  *      **    **    **
*    ** * ******  **    **  *
****    * **     ************
*    ****    * *   
*****************************

'''
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
count = 0
county = 0
countGrid = 0  
i = 0
walls = []
def place():
    global count,county,countGrid,i,w,walls,c
    
    #print(i)
    f = open('map1.txt')
    data = f.read()
    data = list(data)
    #print(data)
    #print(data[i]) 
    if data[i] == "*":
        walls.append( c.create_rectangle(0 + (25 * count),0 + (25 * county),25 + (25 * count),25 + (25 * county), fill = "black") )
    count +=1
    countGrid += 1
    if countGrid == 30 or data[i] == "\n":
        county += 1
        count = 0
        countGrid = 0
    i += 1    
    timer = 0 if data[i] != "*" else 20
    if i < len(data):
        w.after(timer,place)

w.after(200,place)
w.mainloop()