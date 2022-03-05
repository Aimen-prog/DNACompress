#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Aimen CHERIF

User interface
"""

from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import StringVar
from tkinter import Tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox


class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.configure(bg='white smoke')
        self.title("DNACompress")
        self.controller = controller
        self.widgets_labs = {}
        self.widgets_entry = {}
        self.widgets_button = {}
        self.entries = ["Sequence"]
        self.buttons = ["Sequence to BWT", "BWT to sequence", "Huffman compression","Huffman decompression",
                        "Full compression","Full decompression"]


    def get_value(self, key):
        return self.widgets_entry[key].get()

    def create_space(self):

        logo = PhotoImage(file="DNACompress_logo.png")
        label = Label(self,image=logo,bg="white smoke")
        label.image = logo
        label.grid(row=0)



        title = "DNA compression tool \n using Burrows-Wheeler transform and Huffman algorithms"

        Label(self, text=title, bg='white smoke',fg='SlateBlue1', font=("Courier", 12, 'bold',"italic")).grid(row=1) 
        
        hr1 = ttk.Separator(self, orient='horizontal').grid(row=3, ipadx=300)
        Label(self, text="Compression section", bg='white smoke', font=(None, 13, 'bold')).grid(row=4)
        
        hr2 = ttk.Separator(self, orient='horizontal').grid(row=5, ipadx=300) 
        Label(self, text="Decompression section", bg='white smoke', font=(None, 13, 'bold')).grid(row=7)














    def display_bwt_seq(self, bwt) :

        """Method displaying message box showing searched person(s) informations"""

        messagebox.showinfo("bwt transformation: ", bwt)




    def main(self):
        print("[View] main")
        self.mainloop()















