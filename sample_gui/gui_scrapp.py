import tkinter as tk
from tkinter import messagebox,ttk
from threading import Thread
import pandas as pd
import sample_webscrapp as sw
import databasee_scrapp as ds


root=tk.Tk()
root.title("web_scrapp_gui")

displayLabel=tk.Label(root,text="web scrapper",font=("Helvetica", 16))
# displayLabel.grid(row=0,column=1)
displayLabel.pack()

scrapbutton=tk.Button(root,text="scrapp",font=("Sylfaen", 8), command=lambda : scrappData())
# scrapbutton.grid(row=1,column=0)
scrapbutton.pack()

loadButton=tk.Button(root,text="load",font=("Sylfaen", 8), command=lambda : loadData())
# loadButton.grid(row=1,column=1)
loadButton.pack()

showButton=tk.Button(root,text="show",font=("Sylfaen", 8), command= lambda  : showData())
# showButton.grid(row=1,column=2)
showButton.pack()
def scrappData():
    ThreadTask("scrapp").start()
    messagebox.showinfo("Success", "scrapped.")

def loadData():
    ThreadTask("load").start()
    messagebox.showinfo("Success", "Values have been loaded successfully.")

def showData():
    ThreadTask("show").start()
    messagebox.showinfo("Success", "yes it happened.")


class ThreadTask(Thread):


    def __init__(self,value):
        Thread.__init__(self)
        self.value=value



    def run(self):

        if (self.value == "scrapp"):
            print("Started Webscrapping")
            sw.startScrapping()
            print("Webscrapping done")

        if (self.value == "load"):
            connection = ds.startDatabase()
            data=pd.read_csv("poetry_book.csv")
            data=data.set_index("BOOK_ID")
            data.to_sql("webscrapp", connection,if_exists='append')
            print("data inserted")

        if (self.value == "show"):
            cursor=ds.read_data()
            createNewFrame(cursor)

def createNewFrame(data):
    displayroot=tk.Tk()

    displayLabel2=tk.Label(root,text="scrapped data")
    displayLabel2.pack()

    treeview=ttk.Treeview(displayroot)
    treeview["columns"]=(1,2)
    treeview.heading(1,text="book name")
    treeview.heading(2,text="book price")

    i=0
    for row in data:
        treeview.insert('',i,text=str(i+1),values=(row[1],row[2]))
        i=i+1
    treeview.pack()
    displayroot.mainloop()


root.mainloop()