from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk,Image
from yolov3Image import detect


root = Tk()
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
canvas = Canvas(root, width = 500, height = 500)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open(filename))  
canvas.create_image(20, 20, anchor=NW, image=img)
detect(filename)
root.mainloop()     

