# import the library
from appJar import gui
from time import sleep
import datetime
import struct

'''
    The zin of Zen .. 
'''

bits = str((struct.calcsize("P") * 8)) + " Bits"
#print(bits)

def launch(win):
    app.showSubWindow(win)

# create a GUI variable called app

app = gui("Zenloos Geweldig! - "+ bits, "500x400", showIcon=False, bg='orange', font={'size':38})


# global variable to store the count
global counter


counter = 100
mS_time = 1000


def press(btn):
    app.setLabel("message", 'Zin of Zen'.upper())
    print(btn + app.getButton("Do Nothing!"))

    if app.getButton("Do Nothing!") == "What!":

        sleep(3)
        print("I'm done here")
        app.stop()
    else:
        app.setButton("Do Nothing!", "What!")


def countdown():
    # now = datetime.datetime.utcnow()
    # https://tecadmin.net/get-current-date-time-python/

    currentDT = datetime.datetime.now()

    now = datetime.datetime.now()
    currentDT = now.strftime("%A, %d %B ")

    day, hour, minute, second = now.day, now.hour, now.minute, now.second

    if hour < 10:
        hour = "0" + str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    if second < 10:
        second = "0" + str(second)

    # Weekday  = > Zondag, Maandag, Woensdag, Donderdag, Vrijdag, Zaterdag
    tm_string = "Day:" + str(day) + " Time:" + str(hour) + ":" + str(minute) + ":" + str(second)

    app.setLabel("time", tm_string)
    app.setLabel("date", currentDT)

    global counter
    if counter > 0:
        app.setLabel("counter", str(counter))
        counter -= 1
    else:
        app.stop()

# Make window slightly invisible slick look
app.setTransparency(90)

# 'title' Widget Label  => display countdown timer
app.addLabel("counter", "0")
app.getLabelWidget("counter").config(font=("Times", "100", "bold"))
app.setLabelFg("counter", "steelblue")

# 'message' Widget Label  => Give some sense!?
app.addLabel("message", 'Zin of Zen')
app.setLabelFg("message", "darkgrey")
app.setLabelBg("message", "orange")
app.getLabelWidget("message").config(font=("Times", "48"))

# 'time' Widget Label => Where aree we in time and space?!
app.addLabel("time", 'Whats the time?',)
app.setLabelFg("time", "darkorange")
app.setLabelBg("time", "orange")
app.getLabelWidget("time").config(font=("Times", "14"))

# 'date' Widget Label => What is the current date we live @?!
app.addLabel("date", 'Whats the date?',)
app.setLabelFg("date", "darkorange")
app.setLabelBg("date", "orange")
app.getLabelWidget("date").config(font=("Times", "14"))

# one of 4 possible Event triggers making a countdown loop
app.registerEvent(countdown)
# change interval time in mS
app.setPollTime(mS_time)

# Create a button with one function , parse label to press function.
app.addButton("Do Nothing!", press)


# start the GUI
app.go()

