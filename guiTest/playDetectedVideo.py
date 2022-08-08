from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk,Image
from tkVideoPlayer import TkinterVideo
from tkvideo import tkvideo

root = Tk()


    
global player
my_label = Label(root)
my_label.pack()
player = tkvideo("outputYOLO.mp4", my_label, loop = 1, size = (1280,720))
player.play()


lbl1 = Label(root, text="After Detection", bg="orange red",
             fg="white", font="none 24 bold")
lbl1.config(anchor=CENTER)
lbl1.pack()
root.mainloop() 
