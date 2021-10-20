from tkinter import *
from random import randint as r

bg = "#000000"
fg = "#FFFFFF"
font = ("OCR A Extended", 32)

normalBg = "#000000"
targetBg = "#000000"

def regenerateBgs():
  nbg = [r(0,235), r(0,235), r(0,235)]
  tbg = []
  for x in nbg:
    tbg.append(x + 20)
  
  on = "#"
  for x in nbg:
    on = on + str(x) + str(x)
  
  ot = "#"
  for x in tbg:
    ot = ot + str(x) + str(x)
    
  normalBg = on
  targetBg = ot

titleScreen = Tk()
titleScreen.configure(bg=bg)
titleScreen.title("Color Sleuth (Title Screen)")

pgTitle = Label(titleScreen, text="Color Sleuth", font=font, bg=bg, fg=fg)
pgTitle.grid(row=1, column=1)

pgSubtitle = Label(titleScreen, text="Pick which color is different to get the most points!", font=font, bg=bg, fg=fg)
pgSubtitle.grid(row=2, column=1)

master = Tk()
master.configure(bg=bg)
master.title("Color Sleuth")

colorsBox = Frame(master, bg=bg)

def ButtonClicked():
  regenerateBgs()

class ColorButton:
  def __init__(this):
    this.object = Button(colorsBox, bg=normalBg, fg=bg, width=5, height=5)
    
  def

for x in range(8):
  for y in range(4)

if __name__ == "__main__":
  titleScreen.mainloop()
  master.mainloop()
	
