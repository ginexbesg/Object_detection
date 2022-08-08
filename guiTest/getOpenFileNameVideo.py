from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk,Image
from tkVideoPlayer import TkinterVideo
from tkvideo import tkvideo
from yolov3Video import detectVideo
root = Tk()

def open_file(root):
    global filename
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)

    
    
    

def detectPlay():
    print(filename)
    detectVideo(filename)

    #global player
    #my_label = Label(root)
    #my_label.pack()
    #player = tkvideo(filename, my_label, loop = 1, size = (1280,720))
    #player.play()
    

#def StopVideo():
#    print(filename)
#    global player
#    player.stop()

#def PauseVideo():
#    print(filename)
#    global player
#    player.pause()
    

# center this label
lbl1 = Label(root, text="Tkinter Video Player", bg="orange red",
             fg="white", font="none 24 bold")
lbl1.config(anchor=CENTER)
lbl1.pack()

openbtn = Button(root, text='Open', command=lambda: open_file(root))
openbtn.pack(side=TOP, pady=2)

playbtn = Button(root, text='Detect Play', command=lambda: detectPlay())
playbtn.pack(side=TOP, pady=3)

#stopbtn = Button(root, text='Stop Video', command=lambda: StopVideo())
#stopbtn.pack(side=TOP, padx=4)


#pausebtn = Button(root, text='Pause Video', command=lambda: PauseVideo())
#pausebtn.pack(side=TOP, padx=5)

root.mainloop() 
