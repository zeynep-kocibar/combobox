from tkinter import* 
import tkinter as tk 
import tkinter.ttk as ttk
from tkinter.ttk import*

ekran=Tk() 
ekran.title("telefon fiyatı bul")
ekran.geometry("600x600")

model=["samsung","iphone","huawei","xiamoi","nokia"] 
kar=["5","10","15"] 
vergi=["18","25"] 

def calıstır(event):
  global tfiy  
  if t_model.get()=="samsung":
    tfiy=4500
   
  elif t_model.get()=="iphone":
    
    tfiy=5500

  elif t_model.get()=="huawei":
    
    tfiy=4000

  elif t_model.get()=="xiamoi":
    
    tfiy=3000
  
  elif t_model.get()=="nokia":
    
    tfiy=2000
    
def calıstır2(event):
  global kor
  if t_kar.get()=="5":
    kor=5
  elif t_kar.get()=="10":
    kor=10
  elif t_kar.get()=="15":
    kor=15
    
def calıstır3(event):
  global tvo
  if t_vergi.get()=="18":
    tvo=18
  elif t_vergi.get()=="25":
    tvo=25
    
def bul():
    
    sonf=int(tfiy)+((int(tfiy)*int(kor)/100)+(int(tfiy)*int(tvo)/100))

    yazi["text"]=str(sonf) +str( "TL")              
     
t_model=ttk.Combobox()
t_model['values']=model
t_model.bind('<<ComboboxSelected>>', calıstır)
t_model.current(1)
t_model.grid(column=0,row=0)

t_kar=ttk.Combobox()
t_kar['values']=kar
t_kar.bind('<<ComboboxSelected>>', calıstır2)
t_kar.current(1)
t_kar.grid(column=1,row=0)

t_vergi=ttk.Combobox()
t_vergi['values']=vergi
t_vergi.bind('<<ComboboxSelected>>', calıstır3)
t_vergi.current(1)
t_vergi.grid(column=2,row=0)

hesapla=Button(text="HESAPLA",command=bul)
hesapla.grid(column=0,row=3)

yazi=Label(text="..........." )
yazi.grid(column=1,row=3)








