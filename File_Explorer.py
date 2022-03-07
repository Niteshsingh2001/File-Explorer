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
        self.search = Button(self.top_frame,text="Refresh",command=self.search)
        self.search.pack(fill="both",expand=0,side="left")

        # Refresh Button 
        self.refresh = Button(self.top_frame,text="Search",command=self.refresh_cmd)
        self.refresh.pack(fill="both",expand=0,side="left")
        
        # Create Button
        self.btn_mkdir = Button(self.top_frame,text="Create Folder",command=self.mk_folder)
        self.btn_mkdir.pack(fill="both",expand=0,side="left")

        # Delete Button
        self.btn_rmdir = Button(self.top_frame,text="Delete Folder")
        self.btn_rmdir.pack(fill="both",expand=0,side="left")

        # Main File View / List Box
        self.block = Listbox(self.f_view,border=0,)
        self.block.pack(side="left",fill="both",expand=1)

        # ScrollBar
        scrollbar = Scrollbar(self.f_view,orient='vertical',command=self.block.yview)
        self.block['yscrollcommand'] = scrollbar.set
        scrollbar.pack(side="right",fill="both")

        


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
        # print(self.root)       
        # print(self.dirctory.get())       

    def refresh_cmd(self):
        lst = os.listdir(self.root)
        lst_value =StringVar(value=lst)
        self.block['listvariable']=lst_value
        self.block.update()
        
        
        #for i in range(len(lst)) :
        #self.block.insert(i,lst[i])
        


if __name__ == "__main__":
    win = File_Explorer()
    win.refresh_cmd() 
    win.file_view()
       
    win.mainloop()