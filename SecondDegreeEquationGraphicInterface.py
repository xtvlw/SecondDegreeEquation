#_[N_F]_
import tkinter as tk

root = tk.Tk()

a, x1, x2 = 0, 0 , 0


def error():
    X1Label['text'] = 'ERROR'
    X2Label['text'] = 'ERROR'
    DeltaLabel['text'] = 'ERROR'


def Click():
    global a, b, c, Delta
    try:
        a = float(boxA.get())
        b = float(boxB.get())
        c = float(boxC.get())
    except:
        error()
    if a == 0:
        error()
    else:

        Delta = b ** 2 - 4 * a * c
        x1 = (- b - Delta ** 0.5) / (2 * a)
        x2 = (- b + Delta ** 0.5) / (2 * a)
        X1Label['text'] = '{:.2f}'.format(x1)
        X2Label['text'] = '{:.2f}'.format(x2)
        DeltaLabel['text'] = '{:.2f}'.format(Delta)




X1Label = tk.Label(root, width=10, font='calabri 12'
                   , text=x1,relief='solid', background='white')
X2Label = tk.Label(root, width=10, font='calabri 12'
                   , text=x2,relief='solid', background='white')
DeltaLabel = tk.Label(root, width=10, font='calabri 12'
                   , text=x2,relief='solid', background='white')

X1Label.place(x=10, y=170)
X2Label.place(x=110, y=170)
DeltaLabel.place(x=210, y=170)



button = tk.Button(root, width=33, font='calabri 12'
                   , text='GO!',relief='solid',command=Click)
button.place(x=10, y= 90)



boxA = tk.Entry(root, width=10, font='calabri 12')
boxB = tk.Entry(root, width=10, font='calabri 12')
boxC = tk.Entry(root, width=10, font='calabri 12')

boxA.place(x=10, y=25)
boxB.place(x=110, y=25)
boxC.place(x=210, y=25)

Tx1 = tk.Label(root, width=10, font='calabri 12', text='X1')
Tx2 = tk.Label(root, width=10, font='calabri 12', text='X2')
TD = tk.Label(root, width=10, font='calabri 12', text='Delta')

Tx1.place(x=10, y=140)
Tx2.place(x=110, y=140)
TD.place(x=210, y=140)


TxA = tk.Label(root, width=10, font='calabri 12', text='A')
TxB = tk.Label(root, width=10, font='calabri 12', text='B')
TxC = tk.Label(root, width=10, font='calabri 12', text='C')

TxA.place(x=10, y=45)
TxB.place(x=110, y=45)
TxC.place(x=210, y=45)

Ex = tk.Label(root, text='Equation : AX^2 + BX + C = 0')
Ex.place(x=10, y=2)


root.title("Equations")
root.geometry("320x300")
root.mainloop()
