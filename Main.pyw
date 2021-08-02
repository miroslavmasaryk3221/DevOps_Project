import tkinter as tk
import time
import re


from PIL import ImageTk

Tstat = "True"
Fstat = "False"
###############################
# This script is made for Administrators in order to to save amount of time by checking individual folders if a  transfer problem appears
# This is a first check for DpePost
# Made by Miroslav Masaryk
###############################
# PS Script text output opening
#Final version 08.07.2021

# file opening
with open('Dpe_Post.txt') as my_file:
    testsite_array = my_file.readlines()

i = 1
for i in range(15):
    testsite_array[i] = re.sub("[^a-zA-Z0-9,-.@]+", "", testsite_array[i], flags=re.IGNORECASE)

    i = i + 1

    if i == 15:
        break


with open('DEOTIS-APC.txt') as my_file:
    testsite1_array = my_file.readlines()

i = 1
for i in range(15):
    testsite1_array[i] = re.sub("[^a-zA-Z0-9,-.@]+", "", testsite1_array[i], flags=re.IGNORECASE)

    i = i + 1

    if i == 4:
        break
# initialization of canvas
animation = tk.Tk()
animation.geometry("900x780+700+100")
canvas = tk.Canvas(animation, width=900, height=780)
canvas.pack()

# load the  image file
gif1 = ImageTk.PhotoImage(file='./servers/servers1.png')


canvas.create_image(10, 10, image=gif1, anchor=tk.NW)
# FirstLine begin
canvas.create_line(330, 389, 370, 389,  arrow=tk.LAST, fill="green", width=5, tags="Firstline")


# First check FMF01


for x in range(0, 10):
    canvas.move(2, 10, 0)
    animation.update()
    time.sleep(0.05)
    if x == 4:
        canvas.delete("Firstline")
        break
# FirstLine end

# FirstLineUp begin
canvas.create_line(419, 410, 419, 370, arrow=tk.LAST, fill="green", width=5, tags="FirstlineUp")
time.sleep(1)

for x in range(0, 10):
    canvas.move(3, 0, -10)
    animation.update()
    time.sleep(0.05)
    if x == 2:
        time.sleep(0.5)
        canvas.delete("FirstlineUp")

        break
# FirstLineUp end
if testsite_array[1] == Tstat and testsite1_array[1] == Tstat or testsite_array[1] == Fstat and testsite1_array[1] == Tstat:
    print("FMF01 Transfer check ok")
    canvas.create_text(20, 620, fill="red", font=('Arial', 8, 'bold'),
                       text="FMF01 ExtPrintProd Transfer check is ok...", anchor=tk.NW)
    good = ImageTk.PhotoImage(file='./servers/good.png')
    canvas.create_image(304, 172, image=good, anchor=tk.NW)
    animation.update()
    time.sleep(0.5)
else:
    print("FMF01 Transfer check not ok")
    canvas.create_text(20, 620, fill="red", font=('Arial', 8, 'bold'),
                       text="FMF01 ExtPrintProd Transfer check is not ok...\n"
                            "Check FMF01 for duplicate .exe apps or restart the server", anchor=tk.NW)

    bad = ImageTk.PhotoImage(file='./servers/bad.PNG')
    canvas.create_image(305, 171, image=bad, anchor=tk.NW)
    animation.update()
    time.sleep(0.5)
# Check between ODEFMA74->
canvas.create_line(310, 94, 350, 94, arrow=tk.LAST, fill="green", width=5, tags="Secondline")
time.sleep(0.5)
for x in range(0, 40):
    canvas.move(6, 10, 0)
    animation.update()
    time.sleep(0.05)
    if x == 39:
        time.sleep(0.5)
        canvas.delete("Secondline")
        animation.update()
        break
# SecondLineUp
canvas.create_line(744, 70, 744, 110, arrow=tk.LAST, fill="green", width=5, tags="SecondlineDown")


for x in range(0, 10):
    canvas.move(7, 0, 5)
    animation.update()
    time.sleep(0.05)
    if x == 2:

        canvas.delete("SecondlineDown")

if testsite1_array[3] == Tstat:
    print("ODEFMA74->ODEFMF01->ODEFMA08 is ok")
    canvas.create_text(20, 640, fill="red", font=('Arial', 8, 'bold'),
                       text="ODEFMA74->ODEFMF01->ODEFMA08 is ok...", anchor=tk.NW)
    good1 = ImageTk.PhotoImage(file='./servers/good.png')
    canvas.create_image(52, 101, image=good1, anchor=tk.NW)
    animation.update()
    time.sleep(0.5)
else:
    print("ODEFMA74->ODEFMA08 is  not ok")
    canvas.create_text(20, 640, fill="red", font=('Arial', 8, 'bold'),
                       text="ODEFMA74->ODEFMF01->ODEFMA08 is not ok...", anchor=tk.NW)
    bad1 = ImageTk.PhotoImage(file='./servers/bad.png')
    canvas.create_image(52, 101, image=bad1, anchor=tk.NW)
    animation.update()
    time.sleep(0.5)

#####################################
# Case 3
# Third line begin
canvas.create_line(460, 280, 500, 280, arrow=tk.LAST, fill="green", width=5)
time.sleep(0.5)


for x in range(0, 10):
    canvas.move(10, 15, 0)
    animation.update()
    time.sleep(0.05)
    if x == 8:

        break
#third line end

#third case
if testsite_array[1] == Tstat:
    print("FMF01 Transfer check ok")
    canvas.create_text(20, 660, fill="red", font=('Arial', 8, 'bold'),
                       text="FMF01 ExtPrintProd to ODEFMA08 PDF Transfer check is ok...", anchor=tk.NW)
    good2 = ImageTk.PhotoImage(file='./servers/good.png')
    canvas.create_image(633, 171, image=good2, anchor=tk.NW)
    animation.update()
    time.sleep(0.5)
elif testsite_array[3] == Fstat or testsite_array[5] == Fstat or testsite_array[7] == Fstat or testsite_array[9] == Fstat or testsite_array[13] == Fstat:
    print("FMF01 Transfer check ok")
    canvas.create_text(20, 660, fill="red", font=('Arial', 8, 'bold'),
                       text="FMF01 ExtPrintProd to ODEFMA08 PDF Transfer check is not ok...", anchor=tk.NW)
    good2 = ImageTk.PhotoImage(file='./servers/good.PNG')
    canvas.create_image(633, 171, image=good2, anchor=tk.NW)
    animation.update()
    time.sleep(0.5)
else:
    print("FMF01 Transfer check not ok ok")
    canvas.create_text(20, 660, fill="red", font=('Arial', 8, 'bold'),
                       text="FMF01 ExtPrintProd to ODEFMA08 PDF Transfer check is not ok...", anchor=tk.NW)
    bad2 = ImageTk.PhotoImage(file='./servers/bad.PNG')
    canvas.create_image(633, 171, image=bad2, anchor=tk.NW)
    animation.update()
    time.sleep(0.5)
