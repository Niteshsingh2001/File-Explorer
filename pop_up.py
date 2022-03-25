from tkinter import *

class pop_up(Toplevel):

    def __init__(self,t_name,text_msg,btn1_name,btn2_name) -> None:
        super().__init__()
        
        self.title(t_name)
        self.geometry("400x90")
        self.minsize(400,90)
        self.maxsize(400,90)
        self["bg"] = "white"
        self.resizable(False,False)

        

        f1 = Frame(self,bg="white")
        f2 = Frame(self,bg="white")
        f3 = Frame(self,bg="white")
        f1.pack(fill=X,padx=2,pady=5)
        f2.pack(fill=X,padx=2,pady=2)
        f3.pack(fill=X,padx=5,pady=5)

        self.text_msg = Label(f1,text=text_msg,anchor=W,bg="white")
        self.text_msg.pack(fill=X)

        self.f_name = StringVar()
        self.temp = ""

        self.text_area = Entry(f2,textvariable=self.f_name)
        self.text_area.pack(fill=X)
        
        self.btn2 = Button(f3,text=btn2_name,padx=3)
        self.btn2.pack(side="right")
        self.btn2.bind('<Return>',self.btn2_logic)
        self.btn2.bind('<ButtonRelease-1>',self.btn2_logic)

        self.btn1 = Button(f3,text=btn1_name)
        self.btn1.pack(side="right",padx=3)
        # self.btn1.bind('<Return>',self.btn1_logic)
        # self.btn1.bind('<ButtonRelease-1>',self.btn1_logic)


    def btn2_logic(self,event):
        self.destroy()

    # def btn1_logic(self,event):
    #     d = self.f_name.get()
    #     self.temp = d
    #     return d