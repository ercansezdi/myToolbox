#!/usr/bin/env python
# -*- coding: utf8 -*-
#import download
#download.download(["keyboard", "pillow", "pymongo", "pymongo[srv]"])

import threading
import keyboard
from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import os
import ctypes
import pymongo
import tkinter.ttk
import datetime
from time import sleep
import sqlite3
import configparser
from tkinter import messagebox

class tkinterGui(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.parent.title("ToolBox")
        self.parent.geometry("166x280")
        self.variables()
        self.InitGui()


    def InitGui(self):

        # Airrivals Menu Screen
        self.timer_button = Button(self.air_toolbox, text = "Timer", font = ("Helvatica bold",12), command = self.run_timer)
        self.timer_button.grid(row=0,column=0)
        self.timer_button = Button(self.air_toolbox, text="Auto Upgrade", font=("Helvatica bold", 12),
                                   command=self.run_autoUpgrade)
        self.timer_button.grid(row=0, column=1)
        self.timer_button = Button(self.air_toolbox, text="Calc Exp", font=("Helvatica bold", 12),
                                   command=self.run_calcExp)
        self.timer_button.grid(row=0, column=2)
        self.timer_button = Button(self.air_toolbox, text="Item Destroy", font=("Helvatica bold", 12),
                                   command=self.run_destroy)
        self.timer_button.grid(row=0, column=3)
        self.timer_button = Button(self.air_toolbox, text="Auto Buff", font=("Helvatica bold", 12),
                                   command=self.run_otoBuf)
        self.timer_button.grid(row=0, column=4)
        self.timer_button = Button(self.air_toolbox, text="Id Pass", font=("Helvatica bold", 12),
                                   command=self.run_passworDirectory                                   )
        self.timer_button.grid(row=0, column=5)

        # Password Directory Screen

        self.treeBox = FancyListbox(self.idPasswd, font=("Helvatica bold", 12),justify=CENTER)
        self.treeBox.grid(row=0, column=0, rowspan=4, columnspan=1, ipady=40)
        self.treeBox_id = FancyListbox(self.idPasswd, font=("Helvatica bold", 12),justify=CENTER)
        self.treeBox_id.grid(row=0, column=1, rowspan=4, columnspan=2, ipadx=50, ipady=40)
        self.treeBox_passwd = FancyListbox(self.idPasswd,  font=("Helvatica bold", 12),justify=CENTER)
        self.treeBox_passwd.grid(row=0, column=3, rowspan=4, columnspan=2, ipadx=50, ipady=40)

        self.id = Entry(self.idPasswd, font="Helvatica 12 bold")
        self.id.grid(row=4, column=0, columnspan=2, ipadx=50, padx=1)
        self.id.insert(0, "Kullanıcı Adı")
        self.id.bind("<Button-1>", self.clear_directory_id)
        self.passwd = Entry(self.idPasswd, font="Helvatica 12 bold")
        self.passwd.grid(row=4, column=2, columnspan=2, ipadx=50)
        self.passwd.insert(0, "Şifre")
        self.passwd.bind("<Button-1>", self.clear_directory_passwd)
        self.add = Button(self.idPasswd, text="EKLE", command=self.add_data)
        self.add.grid(row=4, column=4, columnspan=1, ipadx=20,pady=2)

        self.text = Label(self.expCalc, text="Exp  : ", font="Helvatica 12 bold")
        self.text.grid(row=0, column=0, columnspan=1)
        self.wExp = Entry(self.expCalc, font="Helvatica 12 bold")
        self.wExp.grid(row=0, column=2, columnspan=3)
        self.basla_x = Button(self.expCalc, text="Hesapla", command=self.calculate_exp, font="Helvatica 12 bold")
        self.basla_x.grid(row=1, column=2, ipadx=60, columnspan=4)
        self.label = Label(self.expCalc, textvariable=self.calc_exp_string, font="Helvatica 12 bold")
        self.label.grid(row=2, column=2, columnspan=4)
        # Timer Screen
        self.canvas = Canvas(self.timer, width=450, height=500)
        self.img = ImageTk.PhotoImage(Image.open("file/bg.png").resize((550, 320), Image.ANTIALIAS))  #
        self.canvas.background = self.img  #
        self.bg = self.canvas.create_image(0, 0, anchor=NW, image=self.img)
        self.canvas.grid(row=0, column=0, columnspan=94, rowspan=24)

        self.label_1 = Label(self.timer, text="Saat", font="Helvatica 12 bold", justify='center', bg="#CCCCCC")
        self.label_1.grid(row=0, column=0, columnspan=1)
        self.label_2 = Label(self.timer, text="Dakika", font="Helvatica 12 bold", justify='center', bg="#CCCCCC")
        self.label_2.grid(row=0, column=1, columnspan=1)
        self.label_3 = Label(self.timer, text="Zaman Fark(Sn)", font="Helvatica 12 bold", justify='center', bg="#CCCCCC")
        self.label_3.grid(row=0, column=2, columnspan=1)
        self.entry_1 = Entry(self.timer, font="Helvatica 12 bold", justify='center')
        self.entry_1.insert(0, "00")
        self.entry_1.grid(row=1, column=0, columnspan=1)
        self.entry_2 = Entry(self.timer, font="Helvatica 12 bold", justify='center')
        self.entry_2.insert(0, "00")
        self.entry_2.grid(row=1, column=1, columnspan=1)
        self.entry_3 = Entry(self.timer, font="Helvatica 12 bold", justify='center')
        self.entry_3.insert(0, "00")
        self.entry_3.grid(row=1, column=2, columnspan=1)

        self.sifirla = Button(self.timer, text="Sıfırla ", font="Helvatica 12 bold", justify='center',
                              command=self.reset)
        self.sifirla.grid(row=2, column=0, columnspan=1, ipadx=30)

        self.zaman_ayarla = Button(self.timer, text="Farkı Ayarla", font="Helvatica 12 bold", justify='center',
                               command=self.fark_ayarla)
        self.zaman_ayarla.grid(row=2, column=1, columnspan=1, ipadx=30)

        self.degistir = Button(self.timer, text="Değiştir ", font="Helvatica 12 bold", justify='center',
                               command=self.change)
        self.degistir.grid(row=2, column=2, columnspan=1, ipadx=30)
        self.batik = Button(self.timer, image=self.batik_img, command=self.batik_click)
        self.batik.grid(row=4, column=0, padx=9, columnspan=1)
        self.kul = Button(self.timer, image=self.kul_img, command=self.kul_click)
        self.kul.grid(row=5, column=0, padx=9, columnspan=1)

        self.batik_clock = Label(self.timer, textvariable=self.batik_time, font="Helvatica 30 bold", justify='center',
                                 bg="#CCCCCC")
        self.batik_clock.grid(row=4, column=1, columnspan=1)

        self.last_clock_batik = Label(self.timer, textvariable=self.last_batik, font="Helvatica 30 bold",
                                      justify='center',
                                      bg="#CCCCCC")
        self.last_clock_batik.grid(row=4, column=2, columnspan=1)

        self.last_batik.set("00:00:00")
        # 14:22
        self.batik_time.set("00:00:00")
        self.kul_clock = Label(self.timer, textvariable=self.kul_time, font="Helvatica 30 bold", justify='center',
                               bg="#CCCCCC")
        self.kul_clock.grid(row=5, column=1, columnspan=1)
        self.kul_time.set("00:00:00")

        self.last_clock_kul = Label(self.timer, textvariable=self.last_kul, font="Helvatica 30 bold", justify='center',
                                    bg="#CCCCCC")
        self.last_clock_kul.grid(row=5, column=2, columnspan=1)

        self.last_kul.set("00:00:00")
        # İtem Destroy Screen
        self.text_T = Label(self.iDestroy, text="İtem Sayısı : ", font="Helvatica 12 bold")
        self.text_T.grid(row=0, column=0, columnspan=2)
        self.numberOfItems_T = Entry(self.iDestroy, font="Helvatica 12 bold", width=10)
        self.numberOfItems_T.grid(row=0, column=2, columnspan=2)
        self.numberOfItems_T.insert(0, "1")
        self.text_satir = Label(self.iDestroy, text="Satir", font="Helvatica 12 bold")
        self.text_satir.grid(row=1, column=0, columnspan=1)
        self.text_satir1 = Entry(self.iDestroy, font="Helvatica 12 bold", width=5)
        self.text_satir1.grid(row=1, column=1, columnspan=1)
        self.text_satir1.insert(0, "1")
        self.text_sutun = Label(self.iDestroy, text="Sutun", font="Helvatica 12 bold")
        self.text_sutun.grid(row=1, column=2, columnspan=1)
        self.text_sutun1 = Entry(self.iDestroy, font="Helvatica 12 bold", width=5)
        self.text_sutun1.grid(row=1, column=3, columnspan=1)
        self.text_sutun1.insert(0, "1")
        self.basla_T = Button(self.iDestroy, text="Parçala", command=self.check_destroy, font="Helvatica 12 bold")
        self.basla_T.grid(row=2, column=1, ipadx=10, columnspan=4)
        # Upgrade Item Screen
        self.text = Label(self.upgrade, text="İtem Sayısı : ", font="Helvatica 12 bold")
        self.text.grid(row=0, column=0, columnspan=2)
        self.numberOfItems = Entry(self.upgrade, font="Helvatica 12 bold")
        self.numberOfItems.grid(row=0, column=2, columnspan=2)
        self.text_2 = Label(self.upgrade, text="Upgrade Sayısı : ", font="Helvatica 12 bold")
        self.text_2.grid(row=1, column=0, columnspan=2)
        self.upgradeOfItems = Entry(self.upgrade, font="Helvatica 12 bold")
        self.upgradeOfItems.grid(row=1, column=2, columnspan=2)
        self.basla_ = Button(self.upgrade, text="Basla", command=self.check_upgrade, font="Helvatica 12 bold")
        self.basla_.grid(row=2, column=0, ipadx=60, columnspan=3)
        self.checkButton = Checkbutton(self.upgrade, text="e5 Upgrade", variable=self.var)
        self.checkButton.grid(row=2, column=3, columnspan=1)
        # Auto Buff Screen
        self.relog_time_text = Label(self.autoBuff,text = "Relog Süresi (Sn) ", font="Helvatica 12 bold")
        self.relog_time_text.grid(row=0,column=0)
        self.relog_time_entry = Entry(self.autoBuff, font="Helvatica 12 bold")
        self.relog_time_entry.grid(row=0,column=1)
        self.relog_time_entry.insert(0,0)
        self.autobuf_continuous = Button(self.autoBuff,text = "Başlat",command= self.buf_control, font="Helvatica 12 bold")
        self.autobuf_continuous.grid(row=1,column=0,ipadx=100,ipady=5,padx=25,columnspan=2,pady=10)
        # Main Screen

        self.appName = ["Airrivals","Table Builder"]
        self.appFrame = [self.air_main_frame, self.table_builder_frame]
        self.appGeometry = ["385x30", "50x50"]
        self.appNames = Listbox(self.mainFrame, font=("Helvatica bold", 12), justify=CENTER)
        self.appNames.grid(row=0, column=0, rowspan=4, columnspan=1, ipady=40)
        scrollbar = Scrollbar(self.mainFrame)
        scrollbar.grid(row=0,column=1,ipady=100)
        self.appNames.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command=self.appNames.yview)
        for values in self.appName:
            self.appNames.insert(END, values)
        self.mainFrame_button = Button(self.mainFrame, text = "Open App",command = self.open_app, font = ("Helvatica bold",12))
        self.mainFrame_button.grid(row=5,column=0,columnspan=2,ipadx=40)
        self.appNames.selection_set(0)


    def variables(self):
        self.timer = Frame(self.parent)
        self.upgrade = Frame(self.parent)
        self.expCalc = Frame(self.parent)
        self.idPasswd = Frame(self.parent)
        self.iDestroy = Frame(self.parent)
        self.autoBuff = Frame(self.parent)
        self.killmark = Frame(self.parent)
        self.buff_contunie =Frame(self.parent)
        self.buf_discontunie = Frame(self.parent)
        self.air_main_frame = Frame(self.parent)
        self.air_toolbox = Frame(self.air_main_frame)
        self.air_toolbox.grid(row=0,column=0)
        #self.air_main_frame.grid(row=0,column=0)
        self.mainFrame = Frame(self.parent)
        self.table_builder_frame = Frame(self.parent)
        self.mainFrame.grid(row=0,column=0)



        self.click = [False, False]
        self.database = database()
        self.database.create()
        self.movement = movemont
        self.sayac = 0
        self.calc_exp_string = StringVar()
        self.exp = []
        self.batik_img = ImageTk.PhotoImage(
            Image.open("file/batik.png").resize((125, 60), Image.ANTIALIAS))
        self.kul_img = ImageTk.PhotoImage(
            Image.open("file/kul.PNG").resize((125, 60), Image.ANTIALIAS))
        self.batik_bg = ImageTk.PhotoImage(Image.open("file/batik_bg.png").resize((550, 320), Image.ANTIALIAS))
        self.kul_bg = ImageTk.PhotoImage(Image.open("file/kul_bg.png").resize((550, 320), Image.ANTIALIAS))
        self.batik_time = StringVar()
        self.kul_time = StringVar()
        self.last_batik = StringVar()
        self.last_kul = StringVar()
        self.login = True
        self.path = "file\\"
        self.info = configparser.ConfigParser()
        self.info.read(self.path + "config.ini")
        self.islem = [False, False]
        self.var = IntVar()
        self.autoBuff_tick = False
    def open_app(self):
        selected_app = self.appNames.get(ACTIVE)

        for appName, appFrame,appGeo in zip(self.appName,self.appFrame,self.appGeometry):
            if appName == selected_app:
                self.mainFrame.grid_remove()

                appFrame.grid(row=0,column=0)
                self.parent.geometry(appGeo)
    def remove_all_frame(self):
        self.timer.grid_remove()
        self.upgrade.grid_remove()
        self.expCalc.grid_remove()
        self.idPasswd.grid_remove()
        self.iDestroy.grid_remove()
        self.buf_discontunie.grid_remove()
        self.buff_contunie.grid_remove()
        self.killmark.grid_remove()
        self.autoBuff.grid_remove()
    def run_otoBuf(self):
        self.popup = Toplevel()
        self.verification_label_1 = Label(self.popup,
                                          text="Bu uygulamayı yönetici tarafından şifrelenmiştir. \nUygulamayı kullanmak için şifre girmeniz gerekmektedir.",font="Helvatica 12 bold")
        self.verification_label_1.grid(row=0, column=0,columnspan=3)
        self.verification_label_2 = Label(self.popup, text="Şifre :",font="Helvatica 12 bold")
        self.verification_label_2.grid(row=1, column=0)
        self.verification_entry = Entry(self.popup,font="Helvatica 12 bold")
        self.verification_entry.grid(row=1, column=1)
        self.verification_button = Button(self.popup, text="Onayla", command=self.run_otoBuf_start,font="Helvatica 12 bold")
        self.verification_button.grid(row=2, column=0,columnspan=3)
    def run_otoBuf_start(self):
        passwd = self.verification_entry.get()
        self.popup.destroy()
        if passwd == "147896325":
            self.parent.title("Auto Buff")
            showinfo("Uyarı", "Oyuna Etki etmesi için\n Yönetici olarak çalıştırınız. !")
            self.parent.geometry("385x100")
            self.remove_all_frame()
            self.autoBuff.grid(row=1,column=0)
        else:
            showinfo("Uyarı", "Şifreyi yanlış girdiniz. !")
    def buf_control(self):
        question = messagebox.askquestion('Doğrulayınız', "Relog Süresi 0 ise 6 dk bir buff vermektendir. Relog süresi 0'dan farklı ise buf verip girilen süre kadar sonra relog'a çıkıp tekrar buf vermektedir. \n 0 - Akıllı Sp 1, 2 ve 3. skill barına istediğiniz buf skilini koyabilirsiniz. Bu ayarlamalar 1. skill penceresi için geçerlidir. Gerekli ayarlamalardan emin misiniz ? ",
                                           icon='warning')
        if question == "yes":
            self.autoBuff_tick = True
            sleep(3)
            self.autobuff_loop()
        else:
            showinfo("Uyarı", "Gerekli ayarlamalar sonra tekrar bekleriz !")
    def autobuff_loop(self):

        if self.relog_time_entry.get() == "0":
            self.open_buf()
            if self.autoBuff_tick:
                root.after(360000, run.autobuff_loop)
        elif int(self.relog_time_entry.get()) < 0:
            pass
        else:
            self.open_buf()
            if self.autoBuff_tick:
                sleep(int(self.relog_time_entry.get()))
                self.relog()
    def autobuff_relog_timer(self):
        root.after(1000, run.autobuff_loop)
    def open_buf(self):
        self.movement.move(810, 1050)
        self.movement.doubleClick()
        sleep(0.3)
        self.move(840, 1050)
        self.movement.doubleClick()
        sleep(0.3)
        self.movement.move(870, 1050)
        self.movement.doubleClick()
        sleep(0.3)
        self.movement.move(900, 1050)
        self.movement.doubleClick()
    def relog(self):
        keyboard.press("escape")
        keyboard.release("escape")
        self.movement.move(1000, 760)
        self.move.click_button()
        sleep(20)
        self.movement.doubleClick()
        sleep(10)
        keyboard.press_and_release('b')
        keyboard.press("enter")
        keyboard.release("enter")
        root.after(100, run.autobuff_loop)
    def check_upgrade(self):
        if self.numberOfItems.get() == "" or self.upgradeOfItems.get() == "":
            showinfo("HATA !", "Boş Bırakılamaz !!")
        else:
            if self.numberOfItems.get().isnumeric() and self.upgradeOfItems.get().isnumeric():
                showinfo("UYARI !", "3 Saniye İçinde Ekrana Geçiniz.")
                self.date = datetime.datetime.today() + datetime.timedelta(seconds=3)
                self.waiting_upgrade()
            else:
                showinfo("HATA !", "Harf Girilemez !")
    def waiting_upgrade(self):
        if datetime.datetime.today() > self.date:
            self.start_upgrade()
        else:
            root.after(500, run.waiting_upgrade)
    def start_upgrade(self):
        yukseltim = int(self.upgradeOfItems.get()) * int(self.numberOfItems.get())
        for i in range(0, yukseltim):
            self.movement.move(640, 720)# kart
            self.movement.doubleClick()
            sleep(0.1)
            self.movement.move(670, 720) # item
            self.movement.doubleClick()
            sleep(0.1)
            self.movement.move(1270, 690) # onay
            self.movement.click_button()
            self.movement.click_button()
            sleep(0.1)
            self.movement.move(540, 550)
            sleep(0.1)
            if int(self.var.get()) == 0:
                self.movement.move(1270, 690) # onay
                self.movement.click_button()
                self.movement.click_button()
                sleep(0.1)

            else:
                self.movement.move(955, 555)
                self.movement.click_button()
                self.movement.click_button()
                sleep(0.1)
                self.movement.move(1270, 690)
                self.movement.click_button()
                self.movement.click_button()
                sleep(0.1)
                self.movement.move(995, 555)
                sleep(0.1)
                self.movement.move(1270, 690)
                self.movement.click_button()
                self.movement.click_button()
    def run_autoUpgrade(self):
        self.parent.title("Auto Upgrade")
        showinfo("Uyarı", "Oyuna Etki etmesi için\n Yönetici olarak çalıştırınız. !")
        self.parent.geometry("385x100")
        self.remove_all_frame()
        self.upgrade.grid(row=1, column=0)
    def check_destroy(self):
        if self.numberOfItems_T.get() == "":
            showinfo("HATA !", "Boş Bırakılamaz !!")
        else:
            if self.numberOfItems_T.get().isnumeric():
                if int(self.text_sutun1.get()) > 10 or int(self.text_satir1.get()) > 10:
                    showinfo("HATA !", "Satır ve Sutun 10'dan fazla olamaz !")
                else:
                    showinfo("UYARI !", "3 Saniye İçinde Ekrana Geçiniz.")

                    self.date = datetime.datetime.today() + datetime.timedelta(seconds=3)
                    self.waiting_destroy()
            else:
                showinfo("HATA !", "Harf Girilemez !")
    def waiting_destroy(self):
        if datetime.datetime.today() > self.date:
            self.start_destroy()
        else:
            root.after(500, run.waiting_destroy)
    def start_destroy(self):
        yukseltim = int(self.numberOfItems_T.get())
        for i in range(0, yukseltim):
            if int(self.text_sutun1.get()) < 5:
                self.movement.move(640 + (int(self.text_sutun1.get()) - 1) * 30, 720 + (int(self.text_satir1.get()) - 1) * 30)
            else:
                self.movement.move(480 + (int(self.text_sutun1.get()) - 1) * 30, 570 + (int(self.text_satir1.get()) - 1) * 30)
            self.movement.doubleClick()
            sleep(0.05)
            self.movement.move(1130, 770)  # parçaladı
            self.movement.click_button()
            self.movement.click_button()
            sleep(1)
            self.movement.move(1190, 770)  # topla üzerine geldi
            sleep(0.05)
            self.movement.click_button()
            self.movement.click_button()
    def run_destroy(self):
        self.parent.title("Item Destroy")
        showinfo("Uyarı", "Oyuna Etki etmesi için\n Yönetici olarak çalıştırınız. !")
        self.parent.geometry("385x100")
        self.remove_all_frame()
        self.iDestroy.grid(row=1, column=0)
    def fark_ayarla(self):
        self.database.update_config(self.entry_3.get())
    def run_timer(self):
        self.parent.title("Boss Timer")
        self.parent.geometry("450x320")
        self.remove_all_frame()
        self.timer.grid(row=1,column=0)
        self.entry_3.delete(0,"end")
        self.entry_3.insert(0,self.database.return_config_time())

        self.client = pymongo.MongoClient(
            "mongodb+srv://bosstimer:timerboss@cluster0.zxtp6.mongodb.net/Cluster0?retryWrites=true&w=majority")
        tre = threading.Thread(target=self.pull_data)
        tre.start()
        root.after(250, run.loop)
    def return_mongodb(self):
        conn = self.client["Cluster0"]
        db = conn['boss']
        simple = db.find_one({"id": "001"})
        simple = str(simple)
        simple = simple.strip().split(",")
        return_data = [True, True]
        for i in simple:
            split_ = i.strip().split(":")
            if split_[0].split("'")[1] == "kul":
                return_data[1] = split_[1].split("'")[1]
            elif split_[0].split("'")[1] == "batik":
                return_data[0] = split_[1].split("'")[1]
            else:
                pass
        return return_data
    def pull_data(self):
        self.return_data = self.return_mongodb()
        root.after(1000, run.pull_data)
    def reset(self):
        hour = (datetime.datetime.today()).strftime("%H")
        minute = (datetime.datetime.today()).strftime("%M")
        date = hour + "/" + minute + "/" + "00"

        if self.islem[0]:
            self.update_database("kul", date)
        elif self.islem[1]:
            self.update_database("batik", date)
        else:
            showinfo("Hata Mesajı", "Kristal Seçilmedi.")
    def change(self):
        today = datetime.datetime.today().strftime("%d:%m:%y")
        time = self.entry_1.get() + "/" + self.entry_2.get()
        time = datetime.datetime.strptime(time + "/00_" + today, "%H/%M/%S_%d:%m:%y")
        value = time.strftime("%H/%M/%S")
        if self.islem[0]:
            self.update_database("kul", value)
        elif self.islem[1]:
            self.update_database("batik", value)
        else:
            showinfo("Hata Mesajı", "Kristal Seçilmedi.")
    def kul_click(self):
        self.islem[0] = True
        self.islem[1] = False
        self.canvas.itemconfig(self.bg, image = self.kul_bg)
    def batik_click(self):
        self.islem[0] = False
        self.islem[1] = True
        self.canvas.itemconfig(self.bg, image=self.batik_bg)
    def update_database(self, typew, value):
        conn = self.client["Cluster0"]
        db = conn['boss']
        if typew == "kul":
            db.update_one({}, {"$set": {'kul': value}})
        else:
            db.update_one({}, {"$set": {'batik': value}})
    def loop(self):

        today = datetime.datetime.today().strftime("%d:%m:%y")
        if self.login:
            self.return_data = self.return_mongodb()
            self.login = False

        self.batik_saat = (datetime.datetime.strptime(str(self.return_data[0]) + "_" + today,"%H/%M/%S_%d:%m:%y") + datetime.timedelta(hours=3) + datetime.timedelta(seconds=int(self.database.return_config_time())) - datetime.datetime.today()).seconds
        data = str(self.return_data[0]).split("/")
        self.last_batik.set("{}:{}:?".format(data[0], data[1]))
        saat = self.batik_saat // 3600
        dakika = (self.batik_saat - saat * 3600) // 60
        saniye = (self.batik_saat - saat * 3600 - dakika * 60)
        if saat < 10:
            saat = "0" + str(saat)
        if dakika < 10:
            dakika = "0" + str(dakika)
        if saniye < 10:
            saniye = "0" + str(saniye)
        if int(saat) < 4:
            self.batik_time.set("{}:{}:{}".format(saat, dakika, saniye))
        self.kul_saat = (datetime.datetime.strptime(self.return_data[1] + "_" + today,
                                                    "%H/%M/%S_%d:%m:%y") + datetime.timedelta(
            hours=1) + datetime.timedelta(seconds=int(self.database.return_config_time())) - datetime.datetime.today()).seconds
        data = str(self.return_data[1]).split("/")

        self.last_kul.set("{}:{}:?".format(data[0], data[1]))

        saat = self.kul_saat // 3600
        dakika = (self.kul_saat - saat * 3600) // 60
        saniye = (self.kul_saat - saat * 3600 - dakika * 60)
        if saat < 10:
            saat = "0" + str(saat)
        if dakika < 10:
            dakika = "0" + str(dakika)
        if saniye < 10:
            saniye = "0" + str(saniye)
        if int(saat) < 2:
            self.kul_time.set("{}:{}:{}".format(saat, dakika, saniye))
        root.after(1000, run.loop)
    def run_calcExp(self):
        self.parent.title("Experiment Calculator")
        self.parent.geometry("385x80")
        self.remove_all_frame()
        self.expCalc.grid(row=1, column=0)
        self.exp = []
        self.experiment()
    def experiment(self):
        dat = """1 0 -
2 91 91
3 232 141
4 453 221
5 844 391
6 1.555 711
7 2.796 1.241
8 4.837 2.041
9 8.008 3.171
10 12.699 4.691
11 19.360 6.661
12 28.501 9.141
13 40.692 12.191
14 56.563 15.871
15 76.804 20.241
16 102.165 25.361
17 133.456 31.291
18 171.547 38.091
19 217.368 45.821
20 271.909 54.541
21 336.220 64.311
22 411.411 75.191
23 498.652 87.241
24 599.173 100.521
25 714.264 115.091
26 845.275 131.011
27 993.616 148.341
28 1.160.757 167.141
29 1.348.228 187.471
30 1.557.619 209.391
31 1.790.580 232.961
32 2.048.821 258.241
33 2.334.112 285.291
34 2.648.283 314.171
35 2.993.224 344.941
36 3.370.885 377.661
37 3.783.276 412.391
38 4.232.467 449.191
39 4.720.588 488.121
40 5.249.829 529.241
41 5.822.440 572.611
42 6.440.731 618.291
43 7.107.072 666.341
44 7.823.893 716.821
45 8.593.684 769.791
46 9.418.995 825.311
47 10.302.436 883.441
48 11.246.677 944.241
49 12.254.448 1.007.771
50 13.328.539 1.074.091
51 14.471.800 1.143.261
52 15.687.141 1.215.341
53 16.977.532 1.290.391
54 18.346.003 1.368.471
55 19.795.644 1.449.641
56 21.329.605 1.533.961
57 22.951.096 1.621.491
58 24.663.387 1.712.291
59 26.469.808 1.806.421
60 28.373.749 1.903.941
61 30.378.660 2.004.911
62 32.784.553 2.405.893
63 35.671.624 2.887.071
64 39.136.109 3.464.485
65 43.293.491 4.157.382
66 48.282.349 4.988.858
67 54.268.978 5.986.629
68 61.452.932 7.183.954
69 70.073.676 8.620.744
70 80.418.568 10.344.892
71 92.832.438 12.413.870
72 107.729.082 14.896.644
73 125.605.054 17.875.972
74 147.056.220 21.451.166
75 172.797.619 25.741.399
76 203.687.297 30.889.678
77 240.754.910 37.067.613
78 285.236.045 44.481.135
79 338.613.407 53.377.362
80 402.666.241 64.052.834
81 479.529.641 76.863.400
82 571.765.721 92.236.080
83 682.449.017 110.683.296
84 815.268.972 132.819.955
85 974.652.918 159.383.946
86 1.165.913.653 191.260.735
87 1.395.426.535 229.512.882
88 1.670.841.993 275.415.458
89 2.001.340.542 330.498.549
90 2.397.938.800 396.598.258
91 2.873.856.709 475.917.909
92 3.444.958.199 571.101.490
93 4.130.279.987 685.321.788
94 4.952.666.132 822.386.145
95 5.939.529.506 986.863.374
96 7.123.765.554 1.184.236.048
97 8.544.848.811 1.421.083.257
98 10.250.148.719 1.705.299.908
99 12.296.508.608 2.046.359.889
100 14.752.140.474 2.455.631.866
101 17.698.898.713 2.946.758.239
102 20.645.656.952 2.946.758.239
103 23.592.415.191 2.946.758.239
104 26.539.173.430 2.946.758.239
105 29.485.931.669 2.946.758.239
106 32.432.689.908 2.946.758.239
107 35.379.448.147 2.946.758.239
108 38.326.206.386 2.946.758.239
109 41.272.964.625 2.946.758.239
110 44.219.722.864 2.946.758.239
"""
        dat = dat.split(" ")
        for i in range(1, len(dat), 2):
            veri = dat[i].split(".")
            num = ""
            for z in veri:
                num += z

            self.exp.append(float(num))
    def calculate_exp(self):
        stt = ""
        exp = str(self.wExp.get()).strip().split(".")
        space = ""
        for i in exp:
            space += i
        exp = space.replace(",", ".")
        exp = float(exp)
        try:
            lvl = 2
            for i in self.exp:
                if self.exp[lvl - 1] < exp and exp < self.exp[lvl]:
                    stt += str(lvl)
                    num = (exp - self.exp[lvl - 1]) * 100 / (self.exp[lvl] - self.exp[lvl - 1])
                    stt += "  Seviye  "
                    stt += "%" + str(round(num, 2))
                    self.calc_exp_string.set(str(stt))
                lvl += 1
        except:
            pass
    def run_passworDirectory(self):
        self.parent.title("Password Directory")
        self.parent.geometry("645x300")
        self.remove_all_frame()
        self.idPasswd.grid(row=1, column=0)
        self.click = [False, False]
        self.database.create()

        self.update_contacs()
    def update_contacs(self):

        self.treeBox.delete_all()
        self.treeBox_id.delete_all()
        self.treeBox_passwd.delete_all()

        id, passwd = self.database.return_users()
        self.sayac = 0
        for i in range(0, len(id)):
            self.treeBox.insert('end',self.sayac+1)
            self.treeBox_id.insert('end',id[self.sayac])
            self.treeBox_passwd.insert('end',passwd[self.sayac])
            self.sayac += 1
        self.id.delete(0,END)
        self.id.insert(0, "Kullanıcı Adı")
        self.passwd.delete(0,END)
        self.passwd.insert(0, "Şifre")
    def delete_contacs(self):
        try:
            pass
            #curItem = self.tree.focus()
            #self.database.delete(self.tree.item(curItem)["values"][0])
            #self.tree.delete(curItem)
        except:
            showinfo("HATA ! ", "Silinecek veri seçilmedi.")
        self.update_contacs()
    def add_data(self):
        self.database.add([self.id.get(),self.passwd.get()])
        self.update_contacs()
    def clear_directory_id(self,_):
        self.click = [True, False]
        if str(self.passwd.get()) == "":
            self.passwd.insert(0, "Şifre")
        if str(self.id.get()) == "Kullanıcı Adı":
            self.id.delete(0, END)
    def clear_directory_passwd(self, _):
        self.click = [False, True]
        if str(self.id.get()) == "":
            self.id.insert(0, "Kullanıcı Adı")
        if str(self.passwd.get()) == "Şifre":
            self.passwd.delete(0, END)

class database:
    def __init__(self):
        self.path = "file\\"
        self.info = configparser.ConfigParser()
        self.info.read(self.path + "config.ini")

    def create(self):
        if not (os.path.exists(self.path)):
            os.mkdir(self.path)
        if not (os.path.isfile(self.path + self.info["info"]["databaseName_passwd"])):
            baglan = sqlite3.connect( self.path + self.info["info"]["databaseName_passwd"])
            veri = baglan.cursor()
            veri.execute("""CREATE TABLE {} (
                                'id'	TEXT UNIQUE,
                                'sifre'	TEXT,
                                PRIMARY KEY(id));""".format("password"))
            baglan.commit()
            baglan.close()
        else:
            pass
        if not (os.path.isfile(self.path + self.info["info"]["databaseName_config"])):
            baglan = sqlite3.connect( self.path + self.info["info"]["databaseName_config"])
            veri = baglan.cursor()
            veri.execute("""CREATE TABLE {} ('delay'	TEXT);""".format("config"))
            baglan.commit()
            baglan.close()
        else:
            pass
    def update_config(self,time):
        baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_config"])
        veri = baglan.cursor()

        veri.execute("INSERT INTO config VALUES(" + time + ")")
        baglan.commit()
        baglan.close()
    def return_config_time(self):
        baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_config"])
        veri = baglan.cursor()
        values = veri.execute("select * from config").fetchall()
        return values[-1][0]

    def add(self,variable):
        if str(variable[0]) == "Kullanıcı Adı" or str(variable[1]) == "Şifre":
            showinfo("Hata Mesajı", "Kullanıcı Adı veya Şifre Boş bırakılamaz.")
        else:
            try:
                baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_passwd"])
                veri = baglan.cursor()
                veri.execute("INSERT INTO password (id, sifre) VALUES (?,?)", (variable[0], variable[1]))
                baglan.commit()
                baglan.close()
            except sqlite3.IntegrityError:
                showinfo("HATA ! ", "Kullanıcı Adı Zaten Eklenmiş.")
    def delete(self,id):

        baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_passwd"])
        veri = baglan.cursor()
        read = veri.execute("select * from password").fetchall()
        syc = 1
        for i in read:
            if syc == id+1:
                id = i[0]
            syc += 1
        print(id)
        veri.execute("DELETE from password where id = '" + id + "'")
        baglan.commit()
        baglan.close()
    def return_users(self):
        baglan = sqlite3.connect(self.path + self.info["info"]["databaseName_passwd"])
        veri = baglan.cursor()
        id = []
        passwd = []
        values = veri.execute("select * from password").fetchall()
        for i in values:
            id.append(i[0])
            passwd.append(i[1])
        return id, passwd
class FancyListbox(tkinter.Listbox):

    def __init__(self, parent, *args, **kwargs):
        tkinter.Listbox.__init__(self, parent, *args, **kwargs)
        self.popup_menu = tkinter.Menu(self, tearoff=0)
        self.popup_menu.add_command(label="Kopyala",
                                    command=self.copy)
        self.bind("<Button-3>", self.popup)
        self.popup_menu.add_command(label="Delete",
                                    command=self.delete_selected)
        self.database = database()
    def popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def copy(self):
        self.event_generate('<<Copy>>')

    def delete_all(self):
        self.selection_set(0, 'end')
        for i in self.curselection()[::-1]:
            self.delete(i)

    def delete_selected(self):
        MsgBox = messagebox.askquestion('Onaylayınız', 'Bak silcem emin misin ?',
                                           icon='warning')
        if MsgBox == 'yes':
            for i in self.curselection()[::-1]:
                self.database.delete(i)

        else:
            messagebox.showinfo('İptal ', 'Az daha siliyordum :)')
class movemont:
    def click_button():
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
    def doubleClick():
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    def move(X, Y):
        ctypes.windll.user32.SetCursorPos(X, Y)

if __name__ == "__main__":
    root = Tk()
    root.call('tk', 'scaling', 1.0)
    run = tkinterGui(root)
    root.mainloop()
