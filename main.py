from tkinter import *
import bnb1
import stc1
m = Tk()
m.title('Head Tumor')

def bnb_prediction():
    values_list=[p,v,lp,ys,ye,id,la,f,c,wl]
    y = bnb1.classifier.predict([values_list])
    print(y)

def stacking_prediction():
    values_list=[p,v,lp,ys,ye,id,la,f,c,wl]
    z = stc1.classifier.predict([values_list])
    print(z)

"""""
hsymp1 = StringVar()
hsymp2 = StringVar()
hsymp3 = StringVar()
hsymp4 = StringVar()
hsymp5 = StringVar()
"""""

head_sym_label=Label(m,text='No Pain(0) or Pain(1)?').pack()
p = IntVar()
Radiobutton(m, text = '0', variable = p, value=0).pack()
Radiobutton(m, text = '1', variable = p, value=1).pack()

head_sym_label=Label(m,text='No Vomittings(0) or Vomittings(1)?').pack()
v = IntVar()
Radiobutton(m, text = '0', variable = v, value=0).pack()
Radiobutton(m, text = '1', variable = v, value=1).pack()

head_sym_label=Label(m,text='Short Pain(0) or Long Pain(1)?').pack()
lp = IntVar()
Radiobutton(m, text = '0', variable = lp, value=0).pack()
Radiobutton(m, text = '1', variable = lp, value=1).pack()

head_sym_label=Label(m,text='Normal skin(0) or Yellow skin(1)?').pack()
ys = IntVar()
Radiobutton(m, text = '0', variable = ys, value=0).pack()
Radiobutton(m, text = '1', variable = ys, value=1).pack()

head_sym_label=Label(m,text='Normal Eyes(0) or Yellow Eyes(1)?').pack()
ye = IntVar()
Radiobutton(m, text = '0', variable = ye, value=0).pack()
Radiobutton(m, text = '1', variable = ye, value=1).pack()

"""""
hs1 = hsymp1.get()
hs2 = hsymp2.get()
hs3 = hsymp3.get()
hs4 = hsymp4.get()
hs5 = hsymp5.get()



osymp1 = StringVar()
osymp2 = StringVar()
osymp3 = StringVar()
osymp4 = StringVar()
osymp5 = StringVar()
"""""""""

other_sym_label=Label(m,text='Digestion(0) or Indigestion(1)?').pack()
id = IntVar()
Radiobutton(m, text = '0', variable = id, value=0).pack()
Radiobutton(m, text = '1', variable = id, value=1).pack()

other_sym_label=Label(m,text='Normal Apetite(0) or Low Apetite(1)?').pack()
la = IntVar()
Radiobutton(m, text = '0', variable = la, value=0).pack()
Radiobutton(m, text = '1', variable = la, value=1).pack()

other_sym_label=Label(m,text='No Fever(0) or Fever(1)?').pack()
f = IntVar()
Radiobutton(m, text = '0', variable = f, value=0).pack()
Radiobutton(m, text = '1', variable = f, value=1).pack()

other_sym_label=Label(m,text='No Chills(0) or Chills(1)?').pack()
c = IntVar()
Radiobutton(m, text = '0', variable = c, value=0).pack()
Radiobutton(m, text = '1', variable = c, value=1).pack()

other_sym_label=Label(m,text='No Weight Loss(0) or Weight Loss(1)?').pack()
wl = IntVar()
Radiobutton(m, text = '0', variable = wl, value=0).pack()
Radiobutton(m, text = '1', variable = wl, value=1).pack()

"""""
os1 = osymp1.get()
os2 = osymp2.get()
os3 = osymp3.get()
os4 = osymp4.get()
os5 = osymp5.get()
"""""

Button(m, text = 'BNB Prediction', width = '50',command = bnb_prediction).pack()
Button(m, text = 'Stacking Prediction', width = '50',command = stacking_prediction).pack()

print(wl)
m.mainloop()
