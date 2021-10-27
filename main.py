from tkinter import *
import bnb1
import stc1
m = Tk()
m.title('Head Tumor')

def bnb_prediction():
    values_list = st_vs()
    y = bnb1.classifier.predict([values_list])
    print(y)

def stacking_prediction():
    values_list = st_vs()
    z = stc1.classifier.predict([values_list])
    print(z)




head_sym_label=Label(m,text='No Pain(0) or Pain(1)?').pack()
p_s = IntVar()
Radiobutton(m, text = '0', variable = p_s, value=0).pack()
Radiobutton(m, text = '1', variable = p_s, value=1).pack()

head_sym_label=Label(m,text='No Vomittings(0) or Vomittings(1)?').pack()
v_s = IntVar()
Radiobutton(m, text = '0', variable = v_s, value=0).pack()
Radiobutton(m, text = '1', variable = v_s, value=1).pack()

head_sym_label=Label(m,text='Short Pain(0) or Long Pain(1)?').pack()
lp_s = IntVar()
Radiobutton(m, text = '0', variable = lp_s, value=0).pack()
Radiobutton(m, text = '1', variable = lp_s, value=1).pack()

head_sym_label=Label(m,text='Normal skin(0) or Yellow skin(1)?').pack()
ys_s = IntVar()
Radiobutton(m, text = '0', variable = ys_s, value=0).pack()
Radiobutton(m, text = '1', variable = ys_s, value=1).pack()

head_sym_label=Label(m,text='Normal Eyes(0) or Yellow Eyes(1)?').pack()
ye_s = IntVar()
Radiobutton(m, text = '0', variable = ye_s, value=0).pack()
Radiobutton(m, text = '1', variable = ye_s, value=1).pack()


other_sym_label=Label(m,text='Digestion(0) or Indigestion(1)?').pack()
id_s = IntVar()
Radiobutton(m, text = '0', variable = id_s, value=0).pack()
Radiobutton(m, text = '1', variable = id_s, value=1).pack()

other_sym_label=Label(m,text='Normal Apetite(0) or Low Apetite(1)?').pack()
la_s = IntVar()
Radiobutton(m, text = '0', variable = la_s, value=0).pack()
Radiobutton(m, text = '1', variable = la_s, value=1).pack()

other_sym_label=Label(m,text='No Fever(0) or Fever(1)?').pack()
f_s = IntVar()
Radiobutton(m, text = '0', variable = f_s, value=0).pack()
Radiobutton(m, text = '1', variable = f_s, value=1).pack()

other_sym_label=Label(m,text='No Chills(0) or Chills(1)?').pack()
c_s = IntVar()
Radiobutton(m, text = '0', variable = c_s, value=0).pack()
Radiobutton(m, text = '1', variable = c_s, value=1).pack()

other_sym_label=Label(m,text='No Weight Loss(0) or Weight Loss(1)?').pack()
wl_s = IntVar()
Radiobutton(m, text = '0', variable = wl_s, value=0).pack()
Radiobutton(m, text = '1', variable = wl_s, value=1).pack()

#stores values
def st_vs():
    p = int(p_s.get())
    v = int(v_s.get())
    lp = int(lp_s.get())
    ys = int(ys_s.get())
    ye = int(ye_s.get())
    id1 = int(id_s.get())
    la = int(la_s.get())
    f = int(f_s.get())
    c = int(c_s.get())
    wl = int(wl_s.get())
    return[p,v,lp,ys,ye,id1,la,f,c,wl]


Button(m, text = 'BNB Prediction', width = '50',command = bnb_prediction).pack()
Button(m, text = 'Stacking Prediction', width = '50',command = stacking_prediction).pack()

m.mainloop()
