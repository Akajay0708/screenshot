import pyautogui

import tkinter as tk

from tkinter.filedialog import *

root=tk.Tk()
window=tk.Canvas(root,width=200, height=200)

window.pack()

def take_ss():
    screen_shot =pyautogui.screenshot()
    save_path = asksaveasfilename()
    screen_shot.save(save_path+"_screenshot.png")
    



window.config(bg="black")
root.iconbitmap("shadow.ico")



ss_button=tk.Button(text="TAKE SCREENSHOT",bg="green",command=take_ss,font=15)

ss_button.pack()

window.create_window(100,100,window=ss_button)




root.mainloop()
