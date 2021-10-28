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


Label(m,text='Input Head Tumor Symptons').pack()
head_sym_label=Label(m,text='No Pain or Pain?').pack()
p_s = IntVar()
Radiobutton(m, text = 'no', variable = p_s, value=0).pack()
Radiobutton(m, text = 'yes', variable = p_s, value=1).pack()

head_sym_label=Label(m,text='No Vomittings or Vomittings?').pack()
v_s = IntVar()
Radiobutton(m, text = 'no', variable = v_s, value=0).pack()
Radiobutton(m, text = 'yes', variable = v_s, value=1).pack()

head_sym_label=Label(m,text='Short Pain or Long Pain?').pack()
lp_s = IntVar()
Radiobutton(m, text = 'no', variable = lp_s, value=0).pack()
Radiobutton(m, text = 'yes', variable = lp_s, value=1).pack()

head_sym_label=Label(m,text='Normal skin or Yellow skin?').pack()
ys_s = IntVar()
Radiobutton(m, text = 'no', variable = ys_s, value=0).pack()
Radiobutton(m, text = 'yes', variable = ys_s, value=1).pack()

head_sym_label=Label(m,text='Normal Eyes or Yellow Eyes?').pack()
ye_s = IntVar()
Radiobutton(m, text = 'no', variable = ye_s, value=0).pack()
Radiobutton(m, text = 'yes', variable = ye_s, value=1).pack()

Label(m,text='Input Other Symptons').pack()
other_sym_label=Label(m,text='Digestion or Indigestion?').pack()
id_s = IntVar()
Radiobutton(m, text = 'no', variable = id_s, value=0).pack()
Radiobutton(m, text = 'yes', variable = id_s, value=1).pack()

other_sym_label=Label(m,text='Normal Apetite or Low Apetite?').pack()
la_s = IntVar()
Radiobutton(m, text = 'no', variable = la_s, value=0).pack()
Radiobutton(m, text = 'yes', variable = la_s, value=1).pack()

other_sym_label=Label(m,text='No Fever or Fever?').pack()
f_s = IntVar()
Radiobutton(m, text = 'no', variable = f_s, value=0).pack()
Radiobutton(m, text = 'yes', variable = f_s, value=1).pack()

other_sym_label=Label(m,text='No Chills or Chills?').pack()
c_s = IntVar()
Radiobutton(m, text = 'no', variable = c_s, value=0).pack()
Radiobutton(m, text = 'yes', variable = c_s, value=1).pack()

other_sym_label=Label(m,text='No Weight Loss or Weight Loss?').pack()
wl_s = IntVar()
Radiobutton(m, text = 'no', variable = wl_s, value=0).pack()
Radiobutton(m, text = 'yes', variable = wl_s, value=1).pack()

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
