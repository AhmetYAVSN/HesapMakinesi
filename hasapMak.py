
from tkinter import *

def yaz(x):
    s = len(giris.get())
    giris.insert(s,str(x))
    #print(x)

hesap = 5

def teksil():
   a=len(giris.get())
   giris.delete(a-1,'end')

def sil():
    giris.delete(0,'end')

s1 = 0

def islemler(x):
    global hesap
    hesap = x
    global s1
    s1 = float(giris.get())
    print(hesap)
    print(s1)
    giris.delete(0,'end')


s2 = 0
def hesapla():
    global s2
    s2 = float(giris.get())
    print(s2)
    global hesap
    sonuc=0
    if(hesap==0):
        sonuc = s1 + s2
    elif(hesap==1):
        sonuc = s1 - s2
    elif (hesap == 2):
        sonuc = s1 * s2
    elif (hesap == 3):
        sonuc = s1 / s2

    giris.delete(0, "end")
    giris.insert(0, (sonuc))


pencere = Tk()
pencere.geometry("230x310")
pencere.configure(background = "salmon")
pencere.title("HESAP MAKİNESİ")

giris = Entry(font="Verdana 14 bold",width=13,justify=RIGHT)
giris.place(x=18,y=15)

b = []

for i in range(1,10):
    b.append(Button(text=str(i),font="Verdana 14 bold",fg="purple",background="skyblue",command=lambda x=i:yaz(x)))

sayac=0

for i in range(0,3):
    for j in range(0,3):
        b[sayac].place(x=20+j*50,y=50+i*50)
        sayac += 1

islem = []

for i in range(0,4):
    islem.append(Button(font="Verdana 14 bold",fg="purple",background="pink",width=2,command=lambda x=i:islemler(x)))
islem[0]['text'] = "+"
islem[1]['text'] = "-"
islem[2]['text'] = "*"
islem[3]['text'] = "/"

for i in range(0,4):
    islem[i].place(x=170,y=50+50*i)

sb = Button(text="0",font="Verdana 14 bold",fg="purple",background="skyblue",command=lambda x=0:yaz(x))
sb.place(x=20,y=200)

nb = Button(text="00",font="Verdana 14 bold",fg="purple",background="skyblue",width=2,command=lambda x="00":yaz(x))
nb.place(x=70,y=200)

eb = Button(text=".",font="Verdana 14 bold",fg="purple",background="skyblue",width=2,command=lambda  x=".":yaz(x))
eb.place(x=120,y=200)

tsb=Button(text="ce",font="Verdana 14 bold",fg="purple",background="pink",width=3,command=teksil)
tsb.place(x=90,y=250)

sb=Button(text="c",font="Verdana 14 bold",fg="purple",background="pink",width=3,command=sil)
sb.place(x=20,y=250)

csb = Button(text="=",font="Verdana 14 bold",fg="purple",background="pink",width=3,command=hesapla)
csb.place(x=157,y=250)

pencere.mainloop()