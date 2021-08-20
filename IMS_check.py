import tkinter as tk
import time
import re


from pil import ImageTk

Tstat = "True"
Fstat = "False"
###############################
# This script is made for Administrators in order to to save amount of time by checking individual folders if a  transfer problem appears
# This is a second check for IMS
# Made by Miroslav Masaryk
###############################


# opening&reading file


with open('IMS.txt') as my_file:
    testsite_array = my_file.readlines()

i = 1
for i in range(15):
    testsite_array[i] = re.sub("[^a-zA-Z0-9,-.@]+", "", testsite_array[i], flags=re.IGNORECASE)

    i = i + 1

    if i == 4:
        break


# initialization of canvas
animation = tk.Tk()
animation.geometry("900x780+700+100")
canvas = tk.Canvas(animation, width=900, height=780)
canvas.pack()

# loading the background image file
gif1 = ImageTk.PhotoImage(file='./servers/servers2.png')

# creating background from the image file
canvas.create_image(10, 10, image=gif1, anchor=tk.NW)
# First moving arrow
canvas.create_line(280, 183, 320, 183,  arrow=tk.LAST, fill="green", width=5, tags="Firstline")

for x in range(0, 10):
    canvas.move(2, 10, 0)
    animation.update()
    time.sleep(0.05)
    if x == 8:
        canvas.delete("Firstline")
        break

if testsite_array[1] == Tstat:
    canvas.create_text(20, 620, fill="red", font=('Arial', 8, 'bold'),
                       text="FMF01 IMS Transfer check is ok...", anchor=tk.NW)
    good = ImageTk.PhotoImage(file='./servers/good.png')
    canvas.create_image(393, 122, image=good, anchor=tk.NW)
    animation.update()
    time.sleep(0.5)
else:
    canvas.create_text(20, 620, fill="red", font=('Arial', 8, 'bold'),
                       text="FMF01 IMS Transfer check is not ok...", anchor=tk.NW)
    bad = ImageTk.PhotoImage(file='./servers/bad.png')
    canvas.create_image(394, 121, image=bad, anchor=tk.NW)
    animation.update()
    time.sleep(0.5)

# Second moving arrow
canvas.create_line(560, 183, 600, 183,  arrow=tk.LAST, fill="green", width=5, tags="Secondline")

for x in range(0, 15):
    canvas.move(5, 10, 0)
    animation.update()
    time.sleep(0.05)
    if x == 12:
        canvas.delete("Secondline")
        break

if testsite_array[3] == Tstat:
    canvas.create_text(20, 630, fill="red", font=('Arial', 8, 'bold'),
                       text="ODEFMA08 IMS Transfer check is ok...", anchor=tk.NW)
    good = ImageTk.PhotoImage(file='./servers/good.png')
    canvas.create_image(698, 122, image=good, anchor=tk.NW)
    animation.update()
    time.sleep(0.5)

else:
    canvas.create_text(20, 630, fill="red", font=('Arial', 8, 'bold'),
                       text="ODEFMA08 IMS Transfer check is not ok...", anchor=tk.NW)
    bad = ImageTk.PhotoImage(file='./servers/bad.png')
    canvas.create_image(699, 121, image=bad, anchor=tk.NW)
    animation.update()
    time.sleep(0.5)







