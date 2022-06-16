from tkinter import ttk
from tkinter.ttk import *
import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter import *

window = Tk()
window.title("Parking Reservation")
window.geometry("1100x900")
window.configure(bg="orange")
name = StringVar()
phonenumber = IntVar()
vehiclenumber = StringVar()
fromtime1 = StringVar()
totime1 = StringVar()
parkingspot1 = tk.StringVar()


def DarkenLabel1():
    button1.configure(bg="red")
    checkbox1.configure(bg="red")


def DarkenLabel2():
    button2.configure(bg="red")
    checkbox2.configure(bg="red")
    parkingspot1.configure(text="2")


def DarkenLabel3():
    button3.configure(bg="red")
    checkbox3.configure(bg="red")
    parkingspot1.configure(text="3")


def DarkenLabel4():
    button4.configure(bg="red")
    checkbox4.configure(bg="red")
    parkingspot1.configure(text="4")


def DarkenLabel5():
    button5.configure(bg="red")
    checkbox5.configure(bg="red")
    parkingspot1.configure(text="5")


def DarkenLabel6():
    button6.configure(bg="red")
    checkbox6.configure(bg="red")
    parkingspot1.configure(text="6")


def DarkenLabel7():
    button7.configure(bg="red")
    checkbox7.configure(bg="red")
    parkingspot1.configure(text="7")


def DarkenLabel8():
    button8.configure(bg="red")
    checkbox8.configure(bg="red")
    parkingspot1.configure(text="8")


def DarkenLabel9():
    button9.configure(bg="red")
    checkbox9.configure(bg="red")
    parkingspot1.configure(text="9")


def DarkenLabel10():
    button10.configure(bg="red")
    checkbox10.configure(bg="red")
    parkingspot1.configure(text="10")


def DarkenLabel11():
    button11.configure(bg="red")
    checkbox11.configure(bg="red")
    parkingspot1.configure(text="11")


def DarkenLabel12():
    button12.configure(bg="red")
    checkbox12.configure(bg="red")
    parkingspot1.configure(text="12")


def DarkenLabel13():
    button13.configure(bg="red")
    checkbox13.configure(bg="red")
    parkingspot1.configure(text="13")


def DarkenLabel14():
    button14.configure(bg="red")
    checkbox14.configure(bg="red")
    parkingspot1.configure(text="14")


def DarkenLabel15():
    button15.configure(bg="red")
    checkbox15.configure(bg="red")
    parkingspot1.configure(text="15")


def DarkenLabel16():
    button16.configure(bg="red")
    checkbox16.configure(bg="red")
    parkingspot1.configure(text="16")


def DarkenLabel17():
    button17.configure(bg="red")
    checkbox17.configure(bg="red")
    parkingspot1.configure(text="17")


def DarkenLabel18():
    button18.configure(bg="red")
    checkbox18.configure(bg="red")
    parkingspot1.configure(text="18")


def DarkenLabel19():
    button19.configure(bg="red")
    checkbox19.configure(bg="red")
    parkingspot1.configure(text="19")


def DarkenLabel20():
    button20.configure(bg="red")
    checkbox20.configure(bg="red")
    parkingspot1.configure(text="20")


def DarkenLabel21():
    button21.configure(bg="red")
    checkbox21.configure(bg="red")
    parkingspot1.configure(text="21")


def DarkenLabel22():
    button22.configure(bg="red")
    checkbox22.configure(bg="red")
    parkingspot1.configure(text="22")


def DarkenLabel23():
    button23.configure(bg="red")
    checkbox23.configure(bg="red")
    parkingspot1.configure(text="23")


def DarkenLabel24():
    button24.configure(bg="red")
    checkbox24.configure(bg="red")
    parkingspot1.configure(text="24")


def DarkenLabel25():
    button25.configure(bg="red")
    checkbox25.configure(bg="red")
    parkingspot1.configure(text="25")


def DarkenLabel26():
    button26.configure(bg="red")
    checkbox26.configure(bg="red")
    parkingspot1.configure(text="26")


def DarkenLabel27():
    button27.configure(bg="red")
    checkbox27.configure(bg="red")
    parkingspot1.configure(text="27")


def DarkenLabel28():
    button28.configure(bg="red")
    checkbox28.configure(bg="red")
    parkingspot1.configure(text="28")


def DarkenLabel29():
    button29.configure(bg="red")
    checkbox29.configure(bg="red")
    parkingspot1.configure(text="29")


def DarkenLabel30():
    button30.configure(bg="red")
    checkbox30.configure(bg="red")
    parkingspot1.configure(text="30")


def DarkenLabel31():
    button31.configure(bg="red")
    checkbox31.configure(bg="red")
    parkingspot1.configure(text="31")


def DarkenLabel32():
    button32.configure(bg="red")
    checkbox32.configure(bg="red")
    parkingspot1.configure(text="32")


def DarkenLabel33():
    button33.configure(bg="red")
    checkbox33.configure(bg="red")
    parkingspot1.configure(text="33")


def DarkenLabel34():
    button34.configure(bg="red")
    checkbox34.configure(bg="red")
    parkingspot1.configure(text="34")


def DarkenLabel35():
    button35.configure(bg="red")
    checkbox35.configure(bg="red")
    parkingspot1.configure(text="35")


def DarkenLabel36():
    button36.configure(bg="red")
    checkbox36.configure(bg="red")
    parkingspot1.configure(text="36")


def DarkenLabel37():
    button37.configure(bg="red")
    checkbox37.configure(bg="red")
    parkingspot1.configure(text="37")


def DarkenLabel38():
    button38.configure(bg="red")
    checkbox38.configure(bg="red")
    parkingspot1.configure(text="38")


def DarkenLabel39():
    button39.configure(bg="red")
    checkbox39.configure(bg="red")
    parkingspot1.configure(text="39")


def DarkenLabel40():
    button40.configure(bg="red")
    checkbox40.configure(bg="red")
    parkingspot1.configure(text="40")


def data():
    nm = name.get()
    pno = phonenumber.get()
    vno = vehiclenumber.get()
    ft1 = fromtime1.get()
    ft2 = fromtime2.get()
    tt1 = totime1.get()
    tt2 = totime2.get()
    ps = parkingspot1.cget("text")


#  db = sqlite3.connect('Parking.db')
#  cursor=db.cursor()
#  cursor.execute('CREATE TABLE IF NOT EXISTS Parking(name TEXT,phonenumber TEXT,vehiclenumber
# TEXT,fromtime1 TEXT,fromtime2 TEXT,totime1 TEXT,totime2 TEXT,parkingspot1 TEXT)')
#  cursor.execute('INSERT INTO
# Parking(name,phonenumber,vehiclenumber,fromtime1,fromtime2,totime1,totime2,parkingspot1)
# VALUES(?,?,?,?,?,?,?,?)',(nm,pno,vno,ft1,ft2,tt1,tt2,ps))
#  db.commit()
#  msg = messagebox.showinfo( "DB Demo","Parking Spot Reserved Successfully")

# canvas = Canvas(window, width = 100, height = 75)      
# canvas.place(x=100, y=5)      
# img = PhotoImage(file="pro.ppm")      
# canvas.create_image(20,20, anchor=NW, image=img)

ja = Label(
    window,
    text="Parking Booking System",
    background="orange",
    foreground="black",
    font=("Arial Bold", 45),
).place(x=300, y=0)
name = Label(window, text="Name", background="orange", font=("Arial", 25)).place(
    x=0, y=80
)
name = Entry(window, width=60)
name.place(x=350, y=80, height=40)
phonenumber = Label(
    window, text="Contact No.", background="orange", font=("Arial", 25)
).place(x=760, y=80)
phonenumber = Entry(window, width=50)
phonenumber.place(x=995, y=80, height=40)
vehiclenumber = Label(
    window, text="Vehicle Number", background="orange", font=("Arial", 25)
).place(x=0, y=130)
vehiclenumber = Entry(window, width=60)
vehiclenumber.place(x=350, y=130, height=40)
time = Label(window, text="Time", background="orange", font=("Arial", 25)).place(
    x=800, y=130
)
time1 = Label(
    window, text="(24Hr format)", background="orange", font=("Arial", 15)
).place(x=780, y=175)
fromtime1 = Spinbox(window, from_=0, to=23, font=("Arial", 25), width=3)
fromtime1.place(x=1040, y=135, height=30)
fromtime2 = Spinbox(window, from_=0, to=59, font=("Arial", 25), width=3)
fromtime2.place(x=1140, y=135, height=30)
totime1 = Spinbox(window, from_=0, to=23, font=("Arial", 25), width=3)
totime1.place(x=1040, y=170, height=30)
totime2 = Spinbox(window, from_=0, to=59, font=("Arial", 25), width=3)
totime2.place(x=1140, y=170, height=30)
a = Label(window, text="From", background="orange", font=("Arial", 15)).place(
    x=970, y=135
)
b = Label(window, text="To", background="orange", font=("Arial", 15)).place(
    x=970, y=170
)
f1 = Label(window, text=" : ", font=(
    "Arial", 15), width=2).place(x=1113, y=136)
f2 = Label(window, text=" : ", font=(
    "Arial", 15), width=2).place(x=1113, y=171)
parkingspot = Label(
    window, text="Select Parking Spot", font=("Arial", 30), background="orange"
).place(x=0, y=200)
parkingspot1 = tk.Label(window, text=" ", font=(
    "Arial", 30), background="orange")
parkingspot1.place(x=550, y=200, height=40)
label1 = Label(window, text="IN", font=("Arial", 30), background="orange").place(
    x=100, y=390
)
label2 = Label(window, text="OUT", font=("Arial", 30), background="orange").place(
    x=1150, y=390
)
x1 = 100
y1 = 40
button1 = tk.Button(
    window,
    text="1",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button1.place(x=x1 + 115, y=280)
button2 = tk.Button(
    window,
    text="2",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button2.place(x=x1 + 201, y=280)
button3 = tk.Button(
    window,
    text="3",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button3.place(x=x1 + 287, y=280)
button4 = tk.Button(
    window,
    text="4",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button4.place(x=x1 + 373, y=280)
button5 = tk.Button(
    window,
    text="5",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button5.place(x=x1 + 459, y=280)
button6 = tk.Button(
    window,
    text="6",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button6.place(x=x1 + 545, y=280)
button7 = tk.Button(
    window,
    text="7",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button7.place(x=x1 + 631, y=280)
button8 = tk.Button(
    window,
    text="8",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button8.place(x=x1 + 717, y=280)
button9 = tk.Button(
    window,
    text="9",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button9.place(x=x1 + 803, y=280)
button10 = tk.Button(
    window,
    text="10",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button10.place(x=x1 + 889, y=280)
button11 = tk.Button(
    window,
    text="11",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button11.place(x=x1 + 115, y=y1 + 320)
button12 = tk.Button(
    window,
    text="12",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button12.place(x=x1 + 201, y=y1 + 320)
button13 = tk.Button(
    window,
    text="13",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button13.place(x=x1 + 287, y=y1 + 320)
button14 = tk.Button(
    window,
    text="14",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button14.place(x=x1 + 373, y=y1 + 320)
button15 = tk.Button(
    window,
    text="15",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button15.place(x=x1 + 459, y=y1 + 320)
button16 = tk.Button(
    window,
    text="16",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button16.place(x=x1 + 545, y=y1 + 320)
button17 = tk.Button(
    window,
    text="17",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button17.place(x=x1 + 631, y=y1 + 320)
button18 = tk.Button(
    window,
    text="18",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button18.place(x=x1 + 717, y=y1 + 320)
button19 = tk.Button(
    window,
    text="19",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button19.place(x=x1 + 803, y=y1 + 320)
button20 = tk.Button(
    window,
    text="20",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button20.place(x=x1 + 889, y=y1 + 320)
button21 = tk.Button(
    window,
    text="21",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button21.place(x=x1 + 115, y=(2 * y1) + 360)
button22 = tk.Button(
    window,
    text="22",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button22.place(x=x1 + 201, y=(2 * y1) + 360)
button23 = tk.Button(
    window,
    text="23",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button23.place(x=x1 + 287, y=(2 * y1) + 360)
button24 = tk.Button(
    window,
    text="24",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button24.place(x=x1 + 373, y=(2 * y1) + 360)
button25 = tk.Button(
    window,
    text="25",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button25.place(x=x1 + 459, y=(2 * y1) + 360)
button26 = tk.Button(
    window,
    text="26",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button26.place(x=x1 + 545, y=(2 * y1) + 360)
button27 = tk.Button(
    window,
    text="27",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button27.place(x=x1 + 631, y=(2 * y1) + 360)
button28 = tk.Button(
    window,
    text="28",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button28.place(x=x1 + 717, y=(2 * y1) + 360)
button29 = tk.Button(
    window,
    text="29",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button29.place(x=x1 + 803, y=(2 * y1) + 360)
button30 = tk.Button(
    window,
    text="30",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button30.place(x=x1 + 889, y=(2 * y1) + 360)
button31 = tk.Button(
    window,
    text="31",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button31.place(x=x1 + 115, y=(3 * y1) + 400)
button32 = tk.Button(
    window,
    text="32",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button32.place(x=x1 + 201, y=(3 * y1) + 400)
button33 = tk.Button(
    window,
    text="33",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button33.place(x=x1 + 287, y=(3 * y1) + 400)
button34 = tk.Button(
    window,
    text="34",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button34.place(x=x1 + 373, y=(3 * y1) + 400)
button35 = tk.Button(
    window,
    text="35",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button35.place(x=x1 + 459, y=(3 * y1) + 400)
button36 = tk.Button(
    window,
    text="36",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button36.place(x=x1 + 545, y=(3 * y1) + 400)
button37 = tk.Button(
    window,
    text="37",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button37.place(x=x1 + 631, y=(3 * y1) + 400)
button38 = tk.Button(
    window,
    text="38",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button38.place(x=x1 + 717, y=(3 * y1) + 400)
button39 = tk.Button(
    window,
    text="39",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button39.place(x=x1 + 803, y=(3 * y1) + 400)
button40 = tk.Button(
    window,
    text="40",
    font=("Arial", 15),
    width=7,
    anchor="w",
    background="lime green",
    relief="solid",
)
button40.place(x=x1 + 889, y=(3 * y1) + 400)
checkbox1 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel1)
checkbox1.place(x=x1 + 155, y=287)
checkbox2 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel2)
checkbox2.place(x=x1 + 241, y=287)
checkbox3 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel3)
checkbox3.place(x=x1 + 327, y=287)
checkbox4 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel4)
checkbox4.place(x=x1 + 413, y=287)
checkbox5 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel5)
checkbox5.place(x=x1 + 499, y=287)
checkbox6 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel6)
checkbox6.place(x=x1 + 585, y=287)
checkbox7 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel7)
checkbox7.place(x=x1 + 671, y=287)
checkbox8 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel8)
checkbox8.place(x=x1 + 757, y=287)
checkbox9 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel9)
checkbox9.place(x=x1 + 843, y=287)
checkbox10 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel10)
checkbox10.place(x=x1 + 929, y=287)
checkbox11 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel11)
checkbox11.place(x=x1 + 155, y=y1 + 327)
checkbox12 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel12)
checkbox12.place(x=x1 + 241, y=y1 + 327)
checkbox13 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel13)
checkbox13.place(x=x1 + 327, y=y1 + 327)
checkbox14 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel14)
checkbox14.place(x=x1 + 413, y=y1 + 327)
checkbox15 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel15)
checkbox15.place(x=x1 + 499, y=y1 + 327)
checkbox16 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel16)
checkbox16.place(x=x1 + 585, y=y1 + 327)
checkbox17 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel17)
checkbox17.place(x=x1 + 671, y=y1 + 327)
checkbox18 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel18)
checkbox18.place(x=x1 + 757, y=y1 + 327)
checkbox19 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel19)
checkbox19.place(x=x1 + 843, y=y1 + 327)
checkbox20 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel20)
checkbox20.place(x=x1 + 929, y=y1 + 327)
checkbox21 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel21)
checkbox21.place(x=x1 + 155, y=(2 * y1) + 367)
checkbox22 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel22)
checkbox22.place(x=x1 + 241, y=(2 * y1) + 367)
checkbox23 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel23)
checkbox23.place(x=x1 + 327, y=(2 * y1) + 367)
checkbox24 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel24)
checkbox24.place(x=x1 + 413, y=(2 * y1) + 367)
checkbox25 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel25)
checkbox25.place(x=x1 + 499, y=(2 * y1) + 367)
checkbox26 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel26)
checkbox26.place(x=x1 + 585, y=(2 * y1) + 367)
checkbox27 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel27)
checkbox27.place(x=x1 + 671, y=(2 * y1) + 367)
checkbox28 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel28)
checkbox28.place(x=x1 + 757, y=(2 * y1) + 367)
checkbox29 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel29)
checkbox29.place(x=x1 + 843, y=(2 * y1) + 367)
checkbox30 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel30)
checkbox30.place(x=x1 + 929, y=(2 * y1) + 367)
checkbox31 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel31)
checkbox31.place(x=x1 + 155, y=(3 * y1) + 407)
checkbox32 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel32)
checkbox32.place(x=x1 + 241, y=(3 * y1) + 407)
checkbox33 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel33)
checkbox33.place(x=x1 + 327, y=(3 * y1) + 407)
checkbox34 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel34)
checkbox34.place(x=x1 + 413, y=(3 * y1) + 407)
checkbox35 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel35)
checkbox35.place(x=x1 + 499, y=(3 * y1) + 407)
checkbox36 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel36)
checkbox36.place(x=x1 + 585, y=(3 * y1) + 407)
checkbox37 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel37)
checkbox37.place(x=x1 + 671, y=(3 * y1) + 407)
checkbox38 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel38)
checkbox38.place(x=x1 + 757, y=(3 * y1) + 407)
checkbox39 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel39)
checkbox39.place(x=x1 + 843, y=(3 * y1) + 407)
checkbox40 = tk.Checkbutton(window, bg="lime green", command=DarkenLabel40)
checkbox40.place(x=x1 + 929, y=(3 * y1) + 407)


def open_popup():
    top = Toplevel(window)
    top.geometry("550x100")
    top.title("Confirmation")
    top.config(bg="Orange")
    Label(
        top,
        text="Congratulations! Your slot has been booked",
        font=("Arial", 16),
        background="orange",
        foreground="black",
    ).place(x=50, y=35)


button2 = ttk.Button(window, text="Confirm", command=open_popup).place(
    x=700, y=600, width=150
)
window.mainloop()
