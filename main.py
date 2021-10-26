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

goBtn = Button(titleScreen, text="Go", font=font, bg=bg, fg=fg, target=titleScreen.destroy)
goBtn.grid(row=3, column=1)

master = Tk()
master.configure(bg=bg)
master.title("Color Sleuth")

colorsBox = Frame(master, bg=bg)

def Click1():
  pass

def Click2():
  pass

def Click3():
  pass

def Click4():
  pass

click = {
  1: Click1,
  2: Click2,
  3: Click3,
  4: Click4,
}

class ColorButton:
  def __init__(this, buttonNumber):
    assert buttonNumber in [1, 2, 3, 4], "ColorButton argument 'buttonNumber' must be an int between 1 and 4 inclusive"
    this.object = Button(colorsBox, bg=normalBg, fg=bg, width=5, height=5, target=click[buttonNumber])
    this.object.grid(row=1, column=buttonNumber)
    
buttons = []
for x in range(6):
  buttons.append(ColorButton(x + 1))
colorsBox.grid(row=1, column=1)

scoreBox = Frame(master, bg=bg)

p1l = Label(scoreBox, text="P1: ", font=font, bg=bg, fg=fg)
p1s = Label(scoreBox, text="0", font=font, bg=bg, fg=fg)

p2l = Label(scoreBox, text="P2: ", font=font, bg=bg, fg=fg)
p2s = Label(scoreBox, text="0", font=font, bg=bg, fg=fg)

def IncrementP1():
  p1s["text"] = str(
    int(p1s.get()) + 1
  )
  
def IncrementP2():
  p2s["text"] = str(
    int(p2s.get()) + 1
  )

scoreBox.grid(row=2, column=1)

if __name__ == "__main__":
  titleScreen.mainloop()
  master.mainloop()
