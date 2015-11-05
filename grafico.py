# -*- coding: utf-8 -*-
import Tkinter as tk
import tkMessageBox

w=tk.Tk()
w.geometry('700x600')
w.title('Ventana!')
#Receta

def abrir():
	#tk.messagebox.showinfo(title='Eehhhh',message='Hiciste click')
	w2=tk.Tk()
	w2.geometry('300x200+100+100')
	w2.title('Otra vez')
	w2.mainloop()

def saluda():
	lblA=tk.Label(w,text='Hola '+entrada.get(), font=('Times New Roman',16)).place(x=200,y=200)

def despide():
	tkMessageBox.showinfo('Jaja','Adiós '+entrada.get())

##MENÚS
barramenu=tk.Menu(w)
menufile=tk.Menu(barramenu)
menuedit=tk.Menu(barramenu)

menufile.add_command(label='Nuevo')
menufile.add_command(label='Abrir',command=abrir)
menufile.add_command(label='Guardar')
menufile.add_separator()
menufile.add_command(label='Salir',command=w.destroy)

menuedit.add_command(label='Cortar')
menuedit.add_command(label='Copiar')
menuedit.add_command(label='Pegar')

barramenu.add_cascade(label='Archivo',menu=menufile)
barramenu.add_cascade(label='Edición',menu=menuedit)
w.config(menu=barramenu)

#TEXTO
lbl1=tk.Label(text='Usuario:',font=('Verdana',12)).place(x=10,y=10)
lbl2=tk.Label(text='Password:',font=('Verdana',12)).place(x=10,y=35)
#CAMPO de TEXTO
entrada=tk.StringVar()
entrada.set('Algo')
txtUsu=tk.Entry(w,textvariable=entrada).place(x=85,y=15)
txtUs2=tk.Entry(w,width=30).place(x=100,y=40)

#BOTONES
btnSaludar=tk.Button(w,text='Saluda',command=saluda,font=('Arial',10)).place(x=200,y=60)
btnDespedir=tk.Button(w,text='Despide',command=despide,font=('Arial',10),width=10).place(x=200,y=100)

w.mainloop()
