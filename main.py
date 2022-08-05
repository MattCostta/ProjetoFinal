from tkinter import *

master = Tk()
master1 = Frame(master)
master2 = Frame(master)
master.title("BarberShop")
master.geometry("490x560+610+153")
master.resizable(width=1,height=1)




master.grid_rowconfigure(0, weight=1)
master.grid_rowconfigure(1, weight=1)
master.grid_rowconfigure(2, weight=1)
master.grid_rowconfigure(3, weight=1)
master.grid_columnconfigure(0, weight=1)
master.grid_columnconfigure(1, weight=1)

#funcoes
def user_janela():
    master2.pack()
    master1.pack_forget()
    #master1 = Tk()
    #master1.title("Janela User")
    #master1.geometry("490x560+610+153")



def barber_janela():
    master1 = Tk()
    master1.title("Janela barbearia")
    master1.geometry("490x560+610+153")




img_fundo = PhotoImage(file="imagens\\barber.png")
lab_fundo = Label(master1, image=img_fundo)

#botões
bt_usuario = Button(master1,text="Usuario",bg='#1d1f21',font='arimo',highlightcolor='#1d1f21',
                    highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8',
                    command=user_janela)

bt_barber = Button(master1,text="Barbearia",bg='#1d1f21',font='arimo',highlightcolor='#1d1f21',
                    highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8',
                   command=barber_janela)

#posicionamento
lab_fundo.pack()
bt_usuario.place(width=118,height=14, x=183, y=419)
bt_barber.place(width=118,height=14, x=183, y=487)



master1.pack()




#Funcionários


bt_voltar = Button (master2, text='Início', font='arimo', highlightcolor='#1d1f21', highlightbackground='#1d1f21',
                    highlightthickness=0, bd='0', activebackground='#1d1f21', fg='#f6f9f8', command= lambda: [master2.pack_forget(), master1.pack])















bt_voltar.grid(row=1, column=0)














#run
master.mainloop()