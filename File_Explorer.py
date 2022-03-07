from tkinter import *
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
        # self.root = os.path.join("C:/Users")
        self.root = os.getcwd()

        
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
        
        self.block.bind('<Button-1>', self.click)

    def click(self,event):
        
        x = self.block.get(self.block.curselection())
        print(x)


    def file_view(self):
        lst_value =StringVar(value=os.listdir(self.root))
        self.block['listvariable']=lst_value
        self.block.update()
        
        

    def mk_folder(self):
        os.mkdir("New Folder")

    def back(self):
        n=self.root.rfind("/")
        d= self.root[0:n+1]
        x=os.chdir(d)
        print(x)
        
        print(self.root)
        
    def search(self):
        self.root = self.dirctory.get()

        self.lst = os.listdir(self.root)
        self.lst_value =StringVar(value=self.lst)

        self.block['listvariable']=self.lst_value
        self.block.update()   

    def refresh_cmd(self):
        self.block['listvariable']=self.lst_value
        self.block.update()
        


if __name__ == "__main__":
    win = File_Explorer()
    win.file_view()
    
       
    win.mainloop()