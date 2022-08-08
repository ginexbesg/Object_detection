from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk,Image
from tkVideoPlayer import TkinterVideo
from tkvideo import tkvideo
import os

root = Tk()
def runImage():
    os.system('python getOpenFileName.py')
    
    
def runVideo():
    os.system('python getOpenFileNameVideo.py')
    

    
def runVideoStop():
    os.system('python videoPlay.py')
    
    

frm = ttk.Frame(root, padding=10)
frm.grid()
mylabel = ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Image", command=runImage).grid(column=1, row=0)
ttk.Button(frm, text="Video", command=runVideo).grid(column=2, row=0)
#ttk.Button(frm, text="Stop", command=runVideoStop).grid(column=3, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=0)

    
root.mainloop()
