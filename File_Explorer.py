from tkinter import *
from tkinter import messagebox
import os
import win32api

#Todo 
'''
new folder func
delete folder func
status bar
'''

class gui(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("File Explorer")
        self.geometry("850x500")

        # variables

        self.root_dir = "Home"
        self.history_memory = []
        self.forward_memory = []

    def nav_bar(self):
        self.nav_frame = Frame()
        self.nav_frame.pack(fill="x",side="top")

        self.Entry_data = StringVar()
        self.Entry_data.set(self.root_dir)

        # Back Button
        self.back_btn = Button(self.nav_frame,text="<")
        self.back_btn.pack(fill="both",expand=0,side="left")
        self.back_btn.bind('<Return>',self.back_btn_logic)
        self.back_btn.bind('<ButtonRelease-1>',self.back_btn_logic)
        
        # Home Button
        self.home_btn = Button(self.nav_frame,text="Home")
        self.home_btn.pack(fill="both",expand=0,side="left")
        self.home_btn.bind('<Return>',self.home_btn_logic)
        self.home_btn.bind('<ButtonRelease-1>',self.home_btn_logic)
        
        # Forward Button
        self.forward_btn = Button(self.nav_frame,text=">")
        self.forward_btn.pack(fill="both",expand=0,side="left")
        self.forward_btn.bind('<Return>',self.forward_btn_logic)
        self.forward_btn.bind('<ButtonRelease-1>',self.forward_btn_logic)

        # Entry Button

        self.path = Entry(self.nav_frame)
        self.path.pack(fill="both",expand=1,side="left")
        self.path["textvariable"] = self.Entry_data
        self.path.bind('<Return>')
        self.path.bind('<ButtonRelease-1>')

        # Search Button

        self.search = Button(self.nav_frame,text="Search")
        self.search.pack(fill="both",expand=0,side="left")
        self.search.bind('<Return>',self.search_btn)
        self.search.bind('<ButtonRelease-1>',self.search_btn)

        # Refresh Button
     
        self.refresh = Button(self.nav_frame,text="Refresh")
        self.refresh.pack(fill="both",expand=0,side="left")
        self.refresh.bind('<Return>',self.refresh_btn)
        self.refresh.bind('<ButtonRelease-1>',self.refresh_btn)
        
        # Create Button
        self.btn_mkdir = Button(self.nav_frame,text="New Folder")
        self.btn_mkdir.pack(fill="both",expand=0,side="left")
        self.btn_mkdir.bind('<Return>')
        self.btn_mkdir.bind('<ButtonRelease-1>')

        # Delete Button
        self.btn_rmdir = Button(self.nav_frame,text="Delete Folder")
        self.btn_rmdir.pack(fill="both",expand=0,side="left")
        self.btn_rmdir.bind('<Return>')
        self.btn_rmdir.bind('<ButtonRelease-1>')
        
    def home_view(self):
        self.h_view = Frame(bg="White")
        self.h_view.pack(fill="both",expand=1)

        drives = win32api.GetLogicalDriveStrings()
        disk_list = [x.rstrip("\\") for x in drives.split('\000') if x]
        
        drive_icon1 = Button(self.h_view,text=disk_list[0],width=10,height=5)
        drive_icon1.pack(side="left",expand=1,padx=2) 
        drive_icon1.bind('<Return>',self.drive_click)    
        drive_icon1.bind('<ButtonRelease-1>',self.drive_click)    

        drive_icon2 = Button(self.h_view,text=disk_list[1],width=10,height=5)
        drive_icon2.pack(side="left",expand=1,padx=2)  
        drive_icon2.bind('<Return>',self.drive_click)    
        drive_icon2.bind('<ButtonRelease-1>',self.drive_click)    

        drive_icon3 = Button(self.h_view,text=disk_list[2],width=10,height=5)
        drive_icon3.pack(side="left",expand=1,padx=2)  
        drive_icon3.bind('<Return>',self.drive_click)    
        drive_icon3.bind('<ButtonRelease-1>',self.drive_click)           
 
    def file_view(self):
        self.f_view = Frame()
        self.f_view.pack(fill="both",expand=1)

        # Main File View / List Box
        self.lst_view = Listbox(self.f_view,border=0)
        self.lst_view.pack(side="left",fill="both",expand=1)
        
        lst_value =StringVar(value=os.listdir(self.root_dir))
        self.lst_view['listvariable']=lst_value
        self.lst_view.update()

        self.lst_view.bind('<Double-Button-1>', self.lst_double_click)
        self.lst_view.bind('<Return>', self.lst_double_click)

        # ScrollBar
        scrollbar = Scrollbar(self.f_view,orient='vertical',command=self.lst_view.yview)
        self.lst_view['yscrollcommand'] = scrollbar.set
        self.lst_view.selection_set(0)
        scrollbar.pack(side="right",fill="both")
      
# ---------------------------- Logic Here ---------------------------------

    def drive_click(self,event):
        btn_val = event.widget.cget("text")
        self.Entry_data.set(btn_val)
        self.root_dir = btn_val
        self.h_view.destroy()
        
        self.file_view()
        self.history_memory.append(self.root_dir)

    def lst_double_click(self,event):
        
        get_loction= self.lst_view.get(self.lst_view.curselection())

        self.lst = os.listdir(os.path.join(self.root_dir,get_loction))

        lst_value =StringVar(value=self.lst)
        self.lst_view['listvariable']= lst_value
        self.lst_view.update()

        new_loc = f"{self.root_dir}\\{get_loction}"
        self.root_dir = new_loc
        self.Entry_data.set(self.root_dir)
        self.path.update()

        self.history_memory.append(self.root_dir)

    def search_btn(self,event):
        self.f_view.destroy()
        self.h_view.destroy()
        self.file_view()


        self.root_dir = self.Entry_data.get()
        
        if self.root_dir == "Home":
            self.f_view.destroy()
            self.home_view()
        else:
            lst = os.listdir(self.root_dir)
            lst_value =StringVar(value=lst)

            self.lst_view['listvariable']=lst_value
            self.lst_view.update() 
        
        self.history_memory.append(self.root_dir)

    def home_btn_logic(self,event):
        self.f_view.destroy()
        self.h_view.destroy()
        self.home_view()

        self.root_dir = "Home"
        self.Entry_data.set(self.root_dir)

        self.path.update()

    def refresh_btn(self,event):

        if self.f_view:
            lst_value =StringVar(value=os.listdir(self.root_dir))
            self.lst_view['listvariable']=lst_value
            self.lst_view.update()
            print("Working")

    def back_btn_logic(self,event):
        if len(self.history_memory) == 0:
            self.f_view.destroy()
            self.h_view.destroy()
            self.home_view()
        else:
            self.root_dir = self.history_memory.pop()
            self.forward_memory.append(self.root_dir)

            lst_value =StringVar(value=os.listdir(self.root_dir))
            self.lst_view['listvariable']= lst_value
            self.lst_view.update()

            self.Entry_data.set(self.root_dir)
            self.path.update()

    def forward_btn_logic(self,event):

        self.root_dir = self.forward_memory.pop(0)
        self.history_memory.append(self.root_dir)
        print(self.root_dir)

        lst_value =StringVar(value=os.listdir(self.root_dir))
        self.lst_view['listvariable']= lst_value
        self.lst_view.update()

        self.Entry_data.set(self.root_dir)
        self.path.update()


if __name__ == "__main__":
    
    win = gui()
    win.nav_bar()
    win.home_view()
    win.mainloop()