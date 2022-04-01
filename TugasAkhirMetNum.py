from tkinter import *

#mendeklarasikan variable untuk menggunakan classtk yang 
#nantinya digunakan untuk menggunakan fitur tkinter
root=Tk()
root.config(background="light blue")
root.title("Operasi Gauss Seidel")

#input nilai menggunakan get method
def pers():
    x2 = int(entry11.get()) #x persamaan 1
    x3 = int(entry21.get()) #x persamaan 2
    x4 = int(entry31.get()) #x persamaan 3
    y2 = int(entry12.get()) #y persamaan 1
    y3 = int(entry22.get()) #y persamaan 2
    y4 = int(entry32.get()) #y persamaan 3
    z2 = int(entry13.get()) #z persamaan 1
    z3 = int(entry23.get()) #z persamaan 2
    z4 = int(entry33.get()) #z persamaan 3
    q1 = int(entry14.get()) #hasil persamaan 1
    q2 = int(entry24.get()) #hasil persamaan 2
    q3 = int(entry34.get()) #hasil persamaan 3


    '''error handle jika user memasukkan persamaan tidak diurut lebih dulu'''
    if (abs(x3) > abs(x2) and abs(x4)): 
        f1 = lambda x, y, z: (q2 - y3*y - z3*z) / x3
        f2 = lambda x, y, z: (q1 - x2*x - z2*z) / y2
        f3 = lambda x, y, z: (q3 - x4*x - y4*y) / z4
    elif (abs(x4) > abs(x2) and abs(x2)):
        f1 = lambda x, y, z: (q3 - y4*y - z4*z) / x4
        f2 = lambda x, y, z: (q2 - x3*x - z3*z) / y3
        f3 = lambda x, y, z: (q1 - x2*x - y2*y) / z2
    else:
        f1 = lambda x, y, z: (q1 - y2*y - z2*z) / x2
        f2 = lambda x, y, z: (q2 - x3*x - z3*z) / y3
        f3 = lambda x, y, z: (q3 - x4*x - y4*y) / z4

    if (abs(y2) > abs(y3) and abs(y4)): 
        f1 = lambda x, y, z: (q2 - y3*y - z3*z) / x3
        f2 = lambda x, y, z: (q1 - x2*x - z2*z) / y2
        f3 = lambda x, y, z: (q3 - x4*x - y4*y) / z4
    elif (abs(y4) > abs(y2) and abs(y3)):
        f1 = lambda x, y, z: (q1 - y2*y - z2*z) / x2
        f2 = lambda x, y, z: (q3 - x4*x - z4*z) / y4
        f3 = lambda x, y, z: (q2 - x3*x - y3*y) / z3
    else:
        f1 = lambda x, y, z: (q1 - y2*y - z2*z) / x2
        f2 = lambda x, y, z: (q2 - x3*x - z3*z) / y3
        f3 = lambda x, y, z: (q3 - x4*x - y4*y) / z4
    
    if (abs(z2) > abs(z4) and abs(z3)):
        f1 = lambda x, y, z: (q3 - y4*y - z4*z) / x4
        f2 = lambda x, y, z: (q2 - x3*x - z3*z) / y3
        f3 = lambda x, y, z: (q1 - x2*x - y2*y) / z2

    elif (abs(z3) > abs(z4) and abs(z2)):
        f1 = lambda x, y, z: (q1 - y2*y - z2*z) / x2
        f2 = lambda x, y, z: (q3 - x4*x - z4*z) / y4
        f3 = lambda x, y, z: (q2 - x3*x - y3*y) / z3
    
    else :
        f1 = lambda x, y, z: (q1 - y2*y - z2*z) / x2
        f2 = lambda x, y, z: (q2 - x3*x - z3*z) / y3
        f3 = lambda x, y, z: (q3 - x4*x - y4*y) / z4
    
    # sesuai dengan algoritma gauss seidel, setelah diinput persamaan akan dirubah bentuknya menjadi seperti di atas
    # misal x+y+z=10 maka akan dirubah menjadi x=10-y-z

    # Initial setup
    # pada algoritma gauss seidel, mula-mula kita inisialisasi bahwa x,y,z adalah 0
    x0 = 0
    y0 = 0
    z0 = 0
    count = 1

    # masukkan nilai error yang ditoleransi
    e = float(entry41.get())

    # Implementation of Gauss Seidel Iteration
    # membuat tampilan seperti count x   y   z
    print('\nCount\tx\ty\tz\n')

    condition = True

    while condition:
        x1 = f1(x0, y0, z0)
        y1 = f2(x1, y0, z0)
        z1 = f3(x1, y1, z0)
        print('%d\t%0.4f\t%0.4f\t%0.4f\n' % (count, x1, y1, z1))
        #menampilkan hasil looping
        e1 = abs(x0 - x1);
        e2 = abs(y0 - y1);
        e3 = abs(z0 - z1);
        #errornya adalah nilai + - menggunakan abs function

        #selesai memproses iterasi, nilai x baru akan tersimpan pada x1
        #dan lainnya seperti itu
        count += 1
        x0 = x1
        y0 = y1
        z0 = z1

        condition = e1 > e and e2 > e and e3 > e
        #kondisi error yang ditoleransi

    print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n' % (x1, y1, z1))
    hasil.config(text='\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n' % (x1, y1, z1))
Label(root, text="Gauss Seidel", font="Normal 30", background='light blue').grid(row=0,column=0,columnspan=7)

Label(root, text="#Jika Bilangan min bisa langsung di tulis di bilangan tersebut",
      font="Normal 10", background='light blue').grid(row=3,column=0,columnspan=7)


#Persamaan 1
Label(root, text="Persamaan 1", font="Normal 20", background='light blue').grid(row=4,column=0,columnspan=7)

Label(root,text="X",font="Normal 15", background='light blue').grid(row=5,column=0)
entry11=Entry(root, bd=2, relief=RIDGE, font="Normal 15",width=15)
entry11.grid(row=6, column=0, padx=5)

Label(root,text="+",font="Normal 15", background='light blue').grid(row=6,column=1)

Label(root,text="Y",font="Normal 15", background='light blue').grid(row=5,column=2)
entry12=Entry(root, bd=2, relief=RIDGE, font="Normal 15",width=15)
entry12.grid(row=6, column=2, padx=5)

Label(root,text="+",font="Normal 15", background='light blue').grid(row=6,column=3)

Label(root,text="Z",font="Normal 15", background='light blue').grid(row=5,column=4)
entry13=Entry(root, bd=2, relief=RIDGE, font="Normal 15",width=15)
entry13.grid(row=6, column=4, padx=5)

Label(root,text="=",font="Normal 15", background='light blue').grid(row=6,column=5)

entry14=Entry(root, bd=2, relief=RIDGE, font="Normal 15",width=15)
entry14.grid(row=6, column=6, padx=5)


#Persamaan 2
Label(root, text="Persamaan 2", font="Normal 20", background='light blue').grid(row=7,column=0,columnspan=7)

Label(root,text="X",font="Normal 15", background='light blue').grid(row=8,column=0)
entry21=Entry(root, bd=2, relief=RIDGE, font="Normal 15",width=15)
entry21.grid(row=9, column=0, padx=5)

Label(root,text="+",font="Normal 15", background='light blue').grid(row=9,column=1)

Label(root,text="Y",font="Normal 15", background='light blue').grid(row=8,column=2)
entry22=Entry(root, bd=2, relief=RIDGE, font="Normal 15",width=15)
entry22.grid(row=9, column=2, padx=5)

Label(root,text="+",font="Normal 15", background='light blue').grid(row=9,column=3)

Label(root,text="Z",font="Normal 15", background='light blue').grid(row=8,column=4)
entry23=Entry(root, bd=2, relief=RIDGE, font="Normal 15",width=15)
entry23.grid(row=9, column=4, padx=5)

Label(root,text="=",font="Normal 15", background='light blue').grid(row=9,column=5)

entry24=Entry(root, bd=2, relief=RIDGE, font="Normal 15",width=15)
entry24.grid(row=9, column=6, padx=5)

#Persamaan 3
Label(root, text="Persamaan 3", font="Normal 20", background='light blue').grid(row=10,column=0,columnspan=7)

Label(root,text="X",font="Normal 15", background='light blue').grid(row=11,column=0)
entry31=Entry(root, bd=2, relief=RIDGE, font="Normal 15",width=15)
entry31.grid(row=12, column=0, padx=5)

Label(root,text="+",font="Normal 15", background='light blue').grid(row=12,column=1)

Label(root,text="Y",font="Normal 15", background='light blue').grid(row=11,column=2)
entry32=Entry(root, bd=2, relief=RIDGE, font="Normal 15",width=15)
entry32.grid(row=12, column=2, padx=5)

Label(root,text="+",font="Normal 15", background='light blue').grid(row=12,column=3)

Label(root,text="Z",font="Normal 15", background='light blue').grid(row=11,column=4)
entry33=Entry(root, bd=2, relief=RIDGE, font="Normal 15",width=15)
entry33.grid(row=12, column=4, padx=5)

Label(root,text="=",font="Normal 15", background='light blue').grid(row=12,column=5)

entry34=Entry(root, bd=2, relief=RIDGE, font="Normal 15",width=15)
entry34.grid(row=12, column=6, padx=5)

#iterasi
Label(root, text="Iterasi", font="Normal 20", background='light blue').grid(row=13,column=0,columnspan=7)
Label(root,text="h",font="Normal 15", background='light blue').grid(row=14,column=0)
entry41=Entry(root, bd=2, relief=RIDGE, font="Normal 15",width=15)
entry41.grid(row=15, column=0, padx=5)

#tombol
b4=Button(root, text="Tekan", font="Normal 15", relief=RIDGE,
          bd=2, activebackground="lightblue", command=pers)
b4.grid(row=16, column=0, columnspan=7)

#Hasil
Label(root,text="Hasil",font="Normal 15", background='light blue').grid(row=17,column=0, columnspan=7)
hasil= Label(root,text="",font="Normal 20", background='light blue')
hasil.grid(row=18, column=0, columnspan=7)

root.mainloop()