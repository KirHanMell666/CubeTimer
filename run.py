import os
from tkinter import *
import time
import sys
import scrambleGenerator


"""
--- TO DO ---
1. Średnie czasów ao5, a012 oraz ogólna
2. kolory na podstawie średniej ogólnej
3. zapisywanie do pliku lokalnie + dodać do niego gitignore # --- # DONE
4. jakies ustawienia kolorów
"""


# ------ Functions ------

def fileSave(time):
    global timesTXT
    f = open(timesTXT, "a")
    f.write(str(time) + "\n")
    f.close()


def fileLoad():
    global times, timesTXT
    if os.path.isfile(timesTXT):
        f = open(timesTXT, "r")
        for line in f:
            times.insert(END, line)
        f.close()


def clearTimes():
    global timesTXT, times
    if os.path.isfile(timesTXT):
        os.remove(timesTXT, dir_fd=None)
        times.delete(0, END)


def startTimer(event):
    global timer, startTime, isTimerRunning, canTimerStart
    if not isTimerRunning:
        timer.config(fg=SolvingColor, text="Solving...")
        startTime = time.time()
        hideLastScrambleLabel()
        isTimerRunning = True
        canTimerStart = False


def stopTimer(event):
    global timer, startTime, stopTime, solveTime, isTimerRunning, averageTime, times
    if isTimerRunning:
        stopTime = time.time()
        solveTime = round(stopTime - startTime, 2)
        if solveTime < averageTime:
            timer.config(fg=StartColor, text=str(solveTime))
        elif solveTime > averageTime:
            timer.config(fg=StopColor, text=str(solveTime))
        else:
            timer.config(fg=SolvingColor, text=str(solveTime))
        times.insert(END, str(solveTime))
        fileSave(solveTime)
        isTimerRunning = False
        doScrambleString()

def stopTimerOnButton():
    global timer, startTime, stopTime, solveTime, isTimerRunning, averageTime, times
    if isTimerRunning:
        stopTime = time.time()
        solveTime = round(stopTime - startTime, 2)
        if solveTime < averageTime:
            timer.config(fg=StartColor, text=str(solveTime))
        elif solveTime > averageTime:
            timer.config(fg=StopColor, text=str(solveTime))
        else:
            timer.config(fg=SolvingColor, text=str(solveTime))
        times.insert(END, str(solveTime))
        isTimerRunning = False
        doScrambleString()


def useSettings():
    global R, G, B, settingsWindow

    #Zdefiniowac poza funkcją okno, stworzyc w funkcji i przypisac do tego zdefiniowanego poza funkcją
    newWindow = Tk()
    newWindow.geometry("500x300")
    newWindow.config()

    settingsFrameNewWindow = Frame(newWindow)

    RcolorSlider = Scale(settingsFrameNewWindow, from_=0, to=255, orient=HORIZONTAL, width=20, length=200)
    GcolorSlider = Scale(settingsFrameNewWindow, from_=0, to=255, orient=HORIZONTAL, width=20, length=200)
    BcolorSlider = Scale(settingsFrameNewWindow, from_=0, to=255, orient=HORIZONTAL, width=20, length=200)

    canvas = Canvas(settingsFrameNewWindow, bg=BGColor, width=200, height=200)

    newWindow.withdraw()

    newWindow.deiconify()

    # --- RED ---
    RcolorSlider.set(R)
    RcolorSlider.grid(column=0, row=1)

    RcolorLabel = Label(settingsFrameNewWindow, text="Red")
    RcolorLabel.grid(column=1, row=1)

    # --- GREEN ---
    GcolorSlider.set(G)
    GcolorSlider.grid(column=0, row=2)

    GcolorLabel = Label(settingsFrameNewWindow, text="Green")
    GcolorLabel.grid(column=1, row=2)

    # --- BLUE ---
    BcolorSlider.set(B)
    BcolorSlider.grid(column=0, row=3)

    BcolorLabel = Label(settingsFrameNewWindow, text="Blue")
    BcolorLabel.grid(column=1, row=3)

    # --- CANVAS ---
    canvas.grid(column=2, row=1, rowspan=3, pady=25)

    settingsFrameNewWindow.pack()
    newWindow.mainloop()
    settingsWindow = newWindow


def closeApp():
    sys.exit()


def listToString(s):
    str1 = ""

    for ele in s:
        str1 += ele + "  "

    return str1

def doScrambleString():
    global scramble, scrambleString, scrambleLabel, previousScramble
    scr = scrambleGenerator.ScrambleGenerator
    previousScramble = scramble
    scramble = scr.getScramble(scr, 20)
    scrambleString = listToString(scramble)
    scrambleLabel.config(text=scrambleString)

    #scramble = ['L\'', 'F\'', 'R\'', 'B\'', 'U\'', 'D\'']
    scr.drawImage(scr, scramble)
    draw(scr.cube)

def setLastScrambleLabel():
    global lastScrambleLabel, previousScramble, previousScramble
    previousScrambleString = listToString(previousScramble)
    lastScrambleLabel.config(text="Last Scramble: " + previousScrambleString)

def hideLastScrambleLabel():
    global lastScrambleLabel
    lastScrambleLabel.config(text="")

def colorPicker(letter):
    if letter == 'w':
        return "white"
    elif letter == 'g':
        return "green"
    elif letter == 'o':
        return "orange"
    elif letter == 'r':
        return "red"
    elif letter == 'b':
        return "blue"
    elif letter == 'y':
        return "yellow"

def draw(cubeColorString):
    global u1, u2, u3, u4, u5, u6, u7, u8
    global d1, d2, d3, d4, d5, d6, d7, d8
    global r1, r2, r3, r4, r5, r6, r7, r8
    global l1, l2, l3, l4, l5, l6, l7, l8
    global f1, f2, f3, f4, f5, f6, f7, f8
    global b1, b2, b3, b4, b5, b6, b7, b8

    u1.config(bg=colorPicker(cubeColorString[0][0]))
    u2.config(bg=colorPicker(cubeColorString[0][1]))
    u3.config(bg=colorPicker(cubeColorString[0][2]))
    u4.config(bg=colorPicker(cubeColorString[0][3]))
    u5.config(bg=colorPicker(cubeColorString[0][4]))
    u6.config(bg=colorPicker(cubeColorString[0][5]))
    u7.config(bg=colorPicker(cubeColorString[0][6]))
    u8.config(bg=colorPicker(cubeColorString[0][7]))

    l1.config(bg=colorPicker(cubeColorString[1][0]))
    l2.config(bg=colorPicker(cubeColorString[1][1]))
    l3.config(bg=colorPicker(cubeColorString[1][2]))
    l4.config(bg=colorPicker(cubeColorString[1][3]))
    l5.config(bg=colorPicker(cubeColorString[1][4]))
    l6.config(bg=colorPicker(cubeColorString[1][5]))
    l7.config(bg=colorPicker(cubeColorString[1][6]))
    l8.config(bg=colorPicker(cubeColorString[1][7]))

    f1.config(bg=colorPicker(cubeColorString[2][0]))
    f2.config(bg=colorPicker(cubeColorString[2][1]))
    f3.config(bg=colorPicker(cubeColorString[2][2]))
    f4.config(bg=colorPicker(cubeColorString[2][3]))
    f5.config(bg=colorPicker(cubeColorString[2][4]))
    f6.config(bg=colorPicker(cubeColorString[2][5]))
    f7.config(bg=colorPicker(cubeColorString[2][6]))
    f8.config(bg=colorPicker(cubeColorString[2][7]))

    r1.config(bg=colorPicker(cubeColorString[3][0]))
    r2.config(bg=colorPicker(cubeColorString[3][1]))
    r3.config(bg=colorPicker(cubeColorString[3][2]))
    r4.config(bg=colorPicker(cubeColorString[3][3]))
    r5.config(bg=colorPicker(cubeColorString[3][4]))
    r6.config(bg=colorPicker(cubeColorString[3][5]))
    r7.config(bg=colorPicker(cubeColorString[3][6]))
    r8.config(bg=colorPicker(cubeColorString[3][7]))

    b1.config(bg=colorPicker(cubeColorString[4][0]))
    b2.config(bg=colorPicker(cubeColorString[4][1]))
    b3.config(bg=colorPicker(cubeColorString[4][2]))
    b4.config(bg=colorPicker(cubeColorString[4][3]))
    b5.config(bg=colorPicker(cubeColorString[4][4]))
    b6.config(bg=colorPicker(cubeColorString[4][5]))
    b7.config(bg=colorPicker(cubeColorString[4][6]))
    b8.config(bg=colorPicker(cubeColorString[4][7]))

    d1.config(bg=colorPicker(cubeColorString[5][0]))
    d2.config(bg=colorPicker(cubeColorString[5][1]))
    d3.config(bg=colorPicker(cubeColorString[5][2]))
    d4.config(bg=colorPicker(cubeColorString[5][3]))
    d5.config(bg=colorPicker(cubeColorString[5][4]))
    d6.config(bg=colorPicker(cubeColorString[5][5]))
    d7.config(bg=colorPicker(cubeColorString[5][6]))
    d8.config(bg=colorPicker(cubeColorString[5][7]))

def keyup(event):
    global canTimerStart
    if(event.keysym == "space"):
        if canTimerStart:
            startTimer(event)
        else:
            canTimerStart = True


def keydown(event):
    global canTimerStart, timer
    if (event.keysym == "space"):
        stopTimer(event)
        if canTimerStart:
            timer.config(fg=NeutralColor, text="Ready")
    else:
        timer.config(fg=NeutralColor)

# ------ Timer Variables ------
startTime = time.time()
stopTime = startTime
isTimerRunning = False
canTimerStart = True
solveTime = 0.0
averageTime = 15.00
scramble = []
previousScramble = []
scrambleString = ""
previousScrambleString = ""

timesTXT = "times.txt"

# ------ Colors ------
BGColor = "#ababab"
SettingsBGColor = "#7b7b7b"
StartColor = "#09d940"
StopColor = "#cc0000"
NeutralColor = "#1f1f1f"
SolvingColor = "#ebb505"
R = 171
G = 171
B = 171
# ------ Window Config ------

window = Tk()
window.geometry("1500x850")
window.minsize(1500, 850)
window.title("Cube Timer")
window.config(bg=BGColor)

mainFrame = Frame(window, bg=BGColor)

# ------ Settings Window ------
settingsWindow = Tk()
settingsWindow.withdraw()

# ------ Upper Frame ------
upperFrame = Frame(mainFrame, bg=BGColor)

label = Label(upperFrame, text="Cube Timer", bg=BGColor, font=("Courier", 30), pady=15)
label.grid(row=0, column=0, sticky="nsew")

scrambleLabel = Label(upperFrame, text="", bg=BGColor, font=("Courier", 20), pady=5, width=40)
scrambleLabel.grid(row=1, column=0, sticky="nsew")

#photo = PhotoImage(file=r"close.png")
#imageClose = photo.subsample(6, 6)

bClose = Button(upperFrame, text="Clear\nTimes", font=("Courier", 20), bg=SettingsBGColor, command=clearTimes )
bClose.grid(row=0, column=1, rowspan=2, sticky="nsew")

upperFrame.grid_columnconfigure(0, weight=15)
upperFrame.grid_columnconfigure(1, weight=1)

upperFrame.pack(fill="both", expand=True)

# ------ Last Scramble Frame ------
lastScrambleFrame = Frame(mainFrame, bg=BGColor)

lastScrambleLabel = Label(lastScrambleFrame, text="", bg=BGColor, font=("Courier", 16), pady=5)
lastScrambleLabel.pack(anchor="w", padx=85)

lastScrambleFrame.pack(fill="both", expand=True)

# ------ Timer Frame ------
timerFrame = Frame(mainFrame, bg=BGColor)

timer = Label(timerFrame, text="0.00", font=("Courier", 140), bg=BGColor, fg=NeutralColor, width=18)
timer.grid(row=0, column=0, sticky="nsew")

times = Listbox(timerFrame, bg=BGColor, height=17, font=("Courier", 14))
times.grid(row=0, column=1, sticky="nsew")

timerFrame.grid_columnconfigure(0, weight=5)
timerFrame.grid_columnconfigure(1, weight=1)

timerFrame.pack(fill="both", expand=True)

# ------ Draw Frame ------
drawFrame = Frame(mainFrame, bg=BGColor)

u1 = Label(drawFrame, text="     ", bg="white")
u2 = Label(drawFrame, text="     ", bg="white")
u3 = Label(drawFrame, text="     ", bg="white")
u4 = Label(drawFrame, text="     ", bg="white")
u5 = Label(drawFrame, text="     ", bg="white")
u6 = Label(drawFrame, text="     ", bg="white")
u7 = Label(drawFrame, text="     ", bg="white")
u8 = Label(drawFrame, text="     ", bg="white")
uCenter = Label(drawFrame, text="     ", bg="white")

u1.grid(row=0, column=3)
u2.grid(row=0, column=4)
u3.grid(row=0, column=5)
u4.grid(row=1, column=5)
u5.grid(row=2, column=5)
u6.grid(row=2, column=4)
u7.grid(row=2, column=3)
u8.grid(row=1, column=3)
uCenter.grid(row=1, column=4)

l1 = Label(drawFrame, text="     ", bg="orange")
l2 = Label(drawFrame, text="     ", bg="orange")
l3 = Label(drawFrame, text="     ", bg="orange")
l4 = Label(drawFrame, text="     ", bg="orange")
l5 = Label(drawFrame, text="     ", bg="orange")
l6 = Label(drawFrame, text="     ", bg="orange")
l7 = Label(drawFrame, text="     ", bg="orange")
l8 = Label(drawFrame, text="     ", bg="orange")
lCenter = Label(drawFrame, text="     ", bg="orange")

l1.grid(row=3, column=0)
l2.grid(row=3, column=1)
l3.grid(row=3, column=2)
l4.grid(row=4, column=2)
l5.grid(row=5, column=2)
l6.grid(row=5, column=1)
l7.grid(row=5, column=0)
l8.grid(row=4, column=0)
lCenter.grid(row=4, column=1)

f1 = Label(drawFrame, text="     ", bg="green")
f2 = Label(drawFrame, text="     ", bg="green")
f3 = Label(drawFrame, text="     ", bg="green")
f4 = Label(drawFrame, text="     ", bg="green")
f5 = Label(drawFrame, text="     ", bg="green")
f6 = Label(drawFrame, text="     ", bg="green")
f7 = Label(drawFrame, text="     ", bg="green")
f8 = Label(drawFrame, text="     ", bg="green")
fCenter = Label(drawFrame, text="     ", bg="green")

f1.grid(row=3, column=3)
f2.grid(row=3, column=4)
f3.grid(row=3, column=5)
f4.grid(row=4, column=5)
f5.grid(row=5, column=5)
f6.grid(row=5, column=4)
f7.grid(row=5, column=3)
f8.grid(row=4, column=3)
fCenter.grid(row=4, column=4)

r1 = Label(drawFrame, text="     ", bg="red")
r2 = Label(drawFrame, text="     ", bg="red")
r3 = Label(drawFrame, text="     ", bg="red")
r4 = Label(drawFrame, text="     ", bg="red")
r5 = Label(drawFrame, text="     ", bg="red")
r6 = Label(drawFrame, text="     ", bg="red")
r7 = Label(drawFrame, text="     ", bg="red")
r8 = Label(drawFrame, text="     ", bg="red")
rCenter = Label(drawFrame, text="     ", bg="red")

r1.grid(row=3, column=6)
r2.grid(row=3, column=7)
r3.grid(row=3, column=8)
r4.grid(row=4, column=8)
r5.grid(row=5, column=8)
r6.grid(row=5, column=7)
r7.grid(row=5, column=6)
r8.grid(row=4, column=6)
rCenter.grid(row=4, column=7)

b1 = Label(drawFrame, text="     ", bg="blue")
b2 = Label(drawFrame, text="     ", bg="blue")
b3 = Label(drawFrame, text="     ", bg="blue")
b4 = Label(drawFrame, text="     ", bg="blue")
b5 = Label(drawFrame, text="     ", bg="blue")
b6 = Label(drawFrame, text="     ", bg="blue")
b7 = Label(drawFrame, text="     ", bg="blue")
b8 = Label(drawFrame, text="     ", bg="blue")
bCenter = Label(drawFrame, text="     ", bg="blue")

b1.grid(row=3, column=9)
b2.grid(row=3, column=10)
b3.grid(row=3, column=11)
b4.grid(row=4, column=11)
b5.grid(row=5, column=11)
b6.grid(row=5, column=10)
b7.grid(row=5, column=9)
b8.grid(row=4, column=9)
bCenter.grid(row=4, column=10)

d1 = Label(drawFrame, text="     ", bg="yellow")
d2 = Label(drawFrame, text="     ", bg="yellow")
d3 = Label(drawFrame, text="     ", bg="yellow")
d4 = Label(drawFrame, text="     ", bg="yellow")
d5 = Label(drawFrame, text="     ", bg="yellow")
d6 = Label(drawFrame, text="     ", bg="yellow")
d7 = Label(drawFrame, text="     ", bg="yellow")
d8 = Label(drawFrame, text="     ", bg="yellow")
dCenter = Label(drawFrame, text="     ", bg="yellow")

d1.grid(row=6, column=3)
d2.grid(row=6, column=4)
d3.grid(row=6, column=5)
d4.grid(row=7, column=5)
d5.grid(row=8, column=5)
d6.grid(row=8, column=4)
d7.grid(row=8, column=3)
d8.grid(row=7, column=3)
dCenter.grid(row=7, column=4)

drawFrame.pack(fill="both", expand=True)

# ------ Settings Frame ------
settingsFrame = Frame(mainFrame, bg=SettingsBGColor)

photo = PhotoImage(file=r"settings.png")
imageSettings = photo.subsample(6, 6)

photo = PhotoImage(file=r"pause.png")
imagePause = photo.subsample(6, 6)

settingsHeight = 120

bSettings = Button(settingsFrame, image=imageSettings, bg=SettingsBGColor, command=useSettings, height=settingsHeight)
bSettings.grid(row=0, column=0, sticky="nsew")

bStart = Button(settingsFrame, text="Show Last Scramble", font=("Courier", 35), bg=SettingsBGColor, command=setLastScrambleLabel)
bStart.grid(row=0, column=1, sticky="nsew")

bPause = Button(settingsFrame, image=imagePause, bg=SettingsBGColor, height=settingsHeight, command=stopTimerOnButton)
bPause.grid(row=0, column=2, sticky="nsew")

settingsFrame.grid_columnconfigure(0, weight=1)
settingsFrame.grid_columnconfigure(1, weight=1)
settingsFrame.grid_columnconfigure(2, weight=1)

settingsFrame.pack(fill="x")

# ------ End ------

window.bind("<KeyRelease>", keyup)
window.bind("<KeyPress>", keydown)

mainFrame.pack(fill="both", expand=True)

doScrambleString()
fileLoad()

window.mainloop()
