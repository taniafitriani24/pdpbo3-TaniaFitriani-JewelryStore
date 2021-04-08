from barang import Barang
from barangnya import Barangnya
from tkinter import *
import tkinter.messagebox as mb

barangs = []
window = Tk()
window.title("Jewelry Store")
window.geometry('650x300')

# ini bagian kiri
frame_b = Frame(window,bg="yellow")
label_nama = Label(frame_b, bg="yellow", text="Nama Barang")
label_nama.grid(row=0, column=0,padx=5,pady=5)
entry_nama = Entry(frame_b,width=25,bd=3)
entry_nama.grid(row=0, column=1,padx=5, sticky="w")

label_jumlah = Label(frame_b, bg="yellow", text="Jumlah",padx=5, pady=5)
label_jumlah.grid(row=1, column=0,padx=5,pady=5)
entry_jumlah = Entry(frame_b,width=25,bd=3)
entry_jumlah.grid(row=1, column=1, sticky="w")

label_warna = Label(frame_b, bg="yellow", text="Warna",padx=5, pady=5)
label_warna.grid(row=2, column=0,padx=5,pady=5)
options = [
    "Gold",
    "Silver",
    "Rose Gold",
]
clicked = StringVar()
drop = OptionMenu(frame_b, clicked,"Gold", "Silver","Rose Gold" )
drop.grid(row=2, column=1, sticky="w")

label_jenis = Label(frame_b, bg="yellow", text="Jenis",padx=5, pady=5)
label_jenis.grid(row=3, column=0,padx=5)
r = StringVar()
r.set("Kalung")
Radiobutton(frame_b,text="Kalung",bg="yellow",variable=r,value="Kalung").grid(row=3, column=1, sticky="w")
Radiobutton(frame_b,text="Gelang",bg="yellow",variable=r,value="Gelang").grid(row=4, column=1, sticky="w")

re = StringVar()
Checkbutton(frame_b,text="Data yang dimasukan sudah benar",bg="yellow",variable=re).grid(row=5, column=1,padx=5, sticky="w")

def pencet():
    nama = entry_nama.get() 
    jumlah = entry_jumlah.get()
    warna = clicked.get()
    jenis = r.get()
    cek = re.get()
    if((nama and jumlah and warna and jenis and cek) != "" ):
        barangs.append(Barangnya(nama, jumlah, warna, jenis))
        mb.showinfo("Info Penting!", "yee data sudah masuk")
    else:
        mb.showinfo("Info Penting!", "Masih ada data kosong:(")


tombol_submit = Button(frame_b, text="SUBMIT!", command=pencet)
tombol_submit.grid(row=6, column=0,padx=5)

# ini bagian kanan
def detail():
    top = Toplevel()
    top.title("All Submission")

    d_frame = LabelFrame(top, text="Data Barang", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    opts = LabelFrame(top, padx=0, pady=0)
    opts.pack(padx=0, pady=0)

    for index, h in enumerate(barangs):
        if(index == 0):
            idx = Label(d_frame, text="No.", width=5, borderwidth=1, relief="solid")
            idx.grid(row=index, column=0)
            name = Label(d_frame, text=" Nama", width=20, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=1)
            jum = Label(d_frame, text=" Jumlah", width=20, borderwidth=1, relief="solid", anchor="w")
            jum.grid(row=index, column=2)
            war = Label(d_frame, text=" Warna", width=20, borderwidth=1, relief="solid", anchor="w")
            war.grid(row=index, column=3)
            jen = Label(d_frame, text=" Jenis", width=20, borderwidth=1, relief="solid", anchor="w")
            jen.grid(row=index, column=4)
        
        idx = Label(d_frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index+1, column=0)
        name = Label(d_frame, text=" " + h.get_nama(), width=20, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index+1, column=1)
        jum = Label(d_frame, text=" " + str(h.get_jumlah()), width=20, borderwidth=1, relief="solid", anchor="w")
        jum.grid(row=index+1, column=2)
        war = Label(d_frame, text=" " + h.get_warna(), width=20, borderwidth=1, relief="solid", anchor="w")
        war.grid(row=index+1, column=3)
        jen = Label(d_frame, text=" " + h.get_jenis(), width=20, borderwidth=1, relief="solid", anchor="w")
        jen.grid(row=index+1, column=4)

def hapus():
    MsgBox = mb.askquestion ('Hapus data','yakin datanya mau dihapus?',icon = 'warning')
    if MsgBox == 'yes':
       barangs[:] = []

def about():
    top = Toplevel()
    top.title("About")
    d_frame = LabelFrame(top, text="Keterangan", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Nama Aplikasi : Jewelry Store ", anchor="w").grid(row=0, column=0, sticky="w")
    d_summary = Label(d_frame, text="deskripsi : Aplikasi untuk pendataan barang", anchor="w").grid(row=1, column=0, sticky="w")
    d_summary = Label(d_frame, text="Tania Fitriani - 1903476", anchor="w").grid(row=2, column=0, sticky="w")

def keluar():
    MsgBox = mb.askquestion ('Keluar','yakin mau keluar?',icon = 'warning')
    if MsgBox == 'yes':
       window.destroy()
    else:
        mb.showinfo('kembali','yuk balik lagi')


frame_a = Frame(window)
label_a = Label(frame_a, text="Jewelry Store",width=20, fg="red", font=("Arial", 20))
label_a.grid(row=0, column=0,padx=5, sticky="w")
label_a = Label(frame_a, text="Aplikasi pendataan perhiasan cantik",font=("Arial", 8))
label_a.grid(row=1, column=0,padx=5)

tombol_sas = Button(frame_a,text="See all submission", command=detail)
tombol_sas.grid(row=2, column=0,padx=5,pady=10, sticky="w")
tombol_cs = Button(frame_a,text="Clear submission", command=hapus)
tombol_cs.grid(row=3, column=0,padx=5,pady=10, sticky="w")
tombol_about = Button(frame_a,text="About", command=about)
tombol_about.grid(row=4, column=0,padx=5,pady=10, sticky="w")
tombol_exit = Button(frame_a,text="Exit", command=keluar)
tombol_exit.grid(row=5, column=0,padx=5,pady=10, sticky="w")
# Swap the order of `frame_a`
frame_a.pack(side=RIGHT)
frame_b.pack(fill=Y, side=LEFT)

window.mainloop()
