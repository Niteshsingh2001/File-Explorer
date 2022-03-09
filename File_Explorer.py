from tkinter import *
from tkinter import messagebox
import os

class File_Explorer(Tk):
    
    def __init__(self) -> None:
        super().__init__()
        self.title("File Explorer")
        self.geometry("850x500")

        # Navigation Bar

        self.top_frame = Frame()
        self.top_frame.pack(fill="x",side="top")

        self.f_view = Frame()
        self.f_view.pack(fill="both",expand=1)

        self.disk_frame=Frame()
       

        #root location / File locations
        # self.root = os.path.join("/storage/emulated/0/")
        self.root = os.path.join("/")
        # self.root = os.getcwd()
        self.history_memory =[]

        self.dirctory = StringVar()
        self.dirctory.set(self.root)
        

        # Navigation Bar Buttons

        # Back Button 
        self.back = Button(self.top_frame,text="Back",command=self.back)
        self.back.pack(fill="both",expand=0,side="left")

        # Search and Entry Bar
        self.dir_path = Entry(self.top_frame,textvariable=self.dirctory)
        self.dir_path.pack(fill="both",expand=1,side="left")

        #Search Button
        self.search = Button(self.top_frame,text="Search",command=self.search)
        self.search.pack(fill="both",expand=0,side="left")
        

        # Refresh Button 
        self.refresh = Button(self.top_frame,text="refresh",command=self.refresh_cmd)
        self.refresh.pack(fill="both",expand=0,side="left")
        
        # Create Button
        self.btn_mkdir = Button(self.top_frame,text="Create Folder",command=self.mk_folder)
        self.btn_mkdir.pack(fill="both",expand=0,side="left")

        # Delete Button
        self.btn_rmdir = Button(self.top_frame,text="Delete Folder")
        self.btn_rmdir.pack(fill="both",expand=0,side="left")

        # Main File View / List Box
        self.block = Listbox(self.f_view,border=0)
        self.block.pack(side="left",fill="both",expand=1)

        # ScrollBar
        scrollbar = Scrollbar(self.f_view,orient='vertical',command=self.block.yview)
        self.block['yscrollcommand'] = scrollbar.set
        self.block.selection_set(0)
        scrollbar.pack(side="right",fill="both")
        
        self.block.bind('<Double-Button-1>', self.d_click)

    # ----------------------------Logic Here--------------------------------------

    def d_click(self,event):
        
        f_loction= self.block.get(self.block.curselection())
        # if len(f_loction)==0:
        #     f_loction.append(self.block.get(self.block.curselection()))
        
        # f_loction.append(f"/{self.block.get(self.block.curselection())}")

        self.root = f"{self.root + f_loction}"

        self.lst = os.listdir(self.root)
        self.lst_value =StringVar(value=self.lst)
        
        self.history_memory.append(self.root)

        self.dirctory.set(self.root)
        self.dir_path.update()

        self.block['listvariable']=self.lst_value
        self.block.update()   


    def file_view(self):
        lst_value =StringVar(value=os.listdir(self.root))
        self.block['listvariable']=lst_value
        self.block.update()
        
        

    def mk_folder(self):
        # os.mkdir(path=self.root,"New Folder")
        os.mkdir(self.root)
        print(" i am make folder")

    def back(self):
       self.root=self.history_memory.pop()

       self.lst = os.listdir(self.root)
       self.lst_value =StringVar(value=self.lst)
    
       print("I am working")
       self.block['listvariable']=self.lst_value
       self.block.update() 
       
        
    def search(self):
        self.root = self.dirctory.get()

        self.lst = os.listdir(self.root)
        self.lst_value =StringVar(value=self.lst)
        self.history_memory.append(self.root)

        self.block['listvariable']=self.lst_value
        self.block.update()   

    def refresh_cmd(self):
        self.block['listvariable']=self.lst_value
        self.block.update()

if __name__ == "__main__":
    win = File_Explorer()
    win.file_view()
    
       
    win.mainloop()