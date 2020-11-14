from tkinter import *

class Gui(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.parent.title("ToolBox")
        self.parent.geometry("300x250")
        self.main_frame = Frame(self.parent)
        self.wifi_frame = Frame(self.parent)


        self.main_frame.grid(row=0,column=0)
        self.InitGui()
    def InitGui(self):
        buttons_name = ["Airrivals", "Wifi Passwords"]
        self.buttons_command = [self.run_airrivals,self.run_wifi]
        self.buttons = []
        for i in range(0,len(buttons_name)):
            self.buttons.append(Button(self.main_frame, text = buttons_name[i],font = ("Helvatica bold",12),command =self.buttons_command[i]))
            self.buttons[-1].grid(row=0,column=i)
        self.run_wifi_init()

    def run_airrivals(self):
        print("airrivals")


    def run_main(self):
        self.remove_all_frame()
        self.main_frame.grid(row=0,column=0)
        self.parent.title("ToolBox")
        self.parent.geometry("300x250")
    def remove_all_frame(self):
        self.main_frame.grid_remove()
        self.wifi_frame.grid_remove()

    def run_wifi(self):
        self.remove_all_frame()
        self.wifi_frame.grid(row=0, column=0)
        self.wifi_frame.config(bg="white")
        passwd = wifi_passwd.see_wifi_pass()
        self.parent.geometry("390x" + str(50 + 15 * len(passwd[0])))
        self.parent.title("Wifi Scanner")
        for i in range(0, len(passwd[0])):
            self.wifi_id_tree.insert('end', passwd[0][i])
            self.wifi_passwd_tree.insert('end', passwd[1][i])
    def run_wifi_init(self):
        self.close_wifi = Button(self.wifi_frame, text="Close Page", command=self.run_main, font=("Helvatica bold", 12),
                                 bg="pink")
        self.close_wifi.grid(row=0, column=0, columnspan=2, ipadx=157)
        self.wifi_id_label = Label(self.wifi_frame, text="Wifi Name", font=("Helvatica bold", 12), bg="white", fg="red")
        self.wifi_id_label.grid(row=1, column=0)
        self.wifi_passwd_label = Label(self.wifi_frame, text="Wifi Password", font=("Helvatica bold", 12), bg="white",
                                       fg="red")
        self.wifi_passwd_label.grid(row=1, column=1)
        self.wifi_id_tree = FancyListbox(self.wifi_frame, font=("Helvatica bold", 12), justify=CENTER)
        self.wifi_id_tree.grid(row=2, column=0, rowspan=4, columnspan=1, ipady=40)
        self.wifi_passwd_tree = FancyListbox(self.wifi_frame, font=("Helvatica bold", 12), justify=CENTER)
        self.wifi_passwd_tree.grid(row=2, column=1, rowspan=4, columnspan=2, ipadx=50, ipady=40)


if __name__ == "__main__":
    try:
        from airrivals.airrivals import *
        from wifi_id_pass.wifi import *
    except:
        import download
        download.download_libs()
        from airrivals.airrivals import *
        from wifi_id_pass.wifi import *

    root = Tk()
    root.call('tk', 'scaling', 1.0)
    run = Gui(root)
    root.mainloop()




