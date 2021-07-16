
from tkinter import *
import tkinter.font

root = Tk()
root.geometry("300x600")

# membuat file pada komputer kita 
f_data = open("data.txt","a")
notice = Label(root,text="file is created").place(x = 100,y = 370)

# mengganti ukuran font
changefont = tkinter.font.Font(size=20)

# ini judulnya
judl = Label(root,text = "REGISTER",font =changefont)
judl.place(x =80,y = 10)

# ini label frame untuk menampilkan pada aplikasi 
labelfr = LabelFrame(root,text = "result",padx=20,pady=20)
labelfr.place(x = 60,y = 380)

# membuat nama nama pada setiap baris kotak
nama = Label(root,text = "First Name")
nama2 = Label(root,text = "Last Name")
age = Label(root,text = "Age")
username = Label(root,text = "Username")
email = Label(root,text = "Email")
password = Label(root,text = "password" )
gender = Label(root,text = "Gender")

# membuat kotaknya
e1 = Entry(root,width=40)
e2 = Entry(root,width=40)
e3 = Entry(root)
e4 = Entry(root,width=40)
e5 = Entry(root,width=40)
e6 = Entry(root,width=40,show="*")

# meletakkan  setiap kotak pada aplikasi
nama.place(x = 20, y =50)
nama2.place(x = 20, y =90)
age.place(x = 20, y =130)
username.place(x = 20, y =170)
email.place(x = 20, y =210)
password.place(x = 20, y =250)
gender.place(x = 20, y =290)

e1.place(x = 20, y = 70)
e2.place(x = 20, y = 110)
e3.place(x = 20, y = 150)
e4.place(x = 20, y = 190)
e5.place(x = 20, y = 230)
e6.place(x = 20, y = 270)

# membuat nama nilai dari radio button
r = StringVar()
r.set("male")
# membuat tombol radiobuttonnya
rb = Radiobutton(root,text = "male",variable=r,value="male").place(x = 20,y =310 )
rb2 = Radiobutton(root,text = "female",variable=r,value="female").place(x = 80,y =310 )

# membuat object untuk semua nilai dan menampung semua nilainya
def cetak():
    class orang:
        def __init__(self,nama,nama2,age,username,email,pas,gender):
            self.nama = nama
            self.nama2 = nama2
            self.age = age
            self.username = username
            self.email = email
            self.password = pas
            self.gender = gender
        def hasil(self):
            # ini adalah nilai yang dapat ditampilkan pada aplikasi
            # lbl = Label(labelfr,text="first name ="+self.nama+"\nlast name ="+self.nama2+"\nage ="+self.age+"\nusername = "+self.username+"\nemail ="+self.email+"\npassword ="+self.password+"\ngender ="+self.gender).grid()

            # ini hanya nilai nya saja
            lbl = ("first name ="+self.nama+"\nlast name ="+self.nama2+"\nage ="+self.age+"\nusername = "+self.username+"\nemail ="+self.email+"\npassword ="+self.password+"\ngender ="+self.gender+"\n\n")
            # mengirim data ke notepad atau txt file
            f_data.write(lbl)
            
    # memanggil fungsi pada object
    ditampilkan = orang(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),r.get())
    ditampilkan.hasil()
    # menghapus tulisan ketika tombol submit ditekan
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
   


btn = Button(root,text = "submit",command=cetak).place(x = 100,y = 350)


root.mainloop()
