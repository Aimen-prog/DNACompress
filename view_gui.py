#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Aimen CHERIF

User interface
"""
import os
from tkinter import Tk
from tkinter import ttk
from tkinter import Menu, filedialog, Button
from tkinter import Entry, Text, Scrollbar, messagebox
from tkinter import Label, Toplevel, END
from tkinter import StringVar
from tkinter.filedialog import asksaveasfile
from tkinter import PhotoImage
from tkinter.messagebox import askquestion


class View(Tk):
    def __init__(self, controller):
        """
        View class's constructor          
        """    
        super().__init__()
        self.configure(bg='white smoke')
        self.title("DNACompress")
        self.controller = controller
        self.file = None
        self.sequence = ''
        self.text_box_content=''

    def create_space(self):
        """
        This method creates the space (image and labels) of the home page
        """    

        logo = PhotoImage(file="DNACompress_logo.png")
        label = Label(self,image=logo,bg="white smoke")
        label.image = logo
        label.grid(row=0)


        title = "A DNA compression tool \n using Burrows-Wheeler transform and Huffman algorithms"
        Label(self, text=title, bg='white smoke',fg='SlateBlue4', font=("Courier", 11, 'bold',"italic")).grid(row=1) 
        

        Label(self, text="Encryption", bg='white smoke',fg='grey',  font=(None, 13, 'bold')).grid(row=4)
        hr1 = ttk.Separator(self, orient='horizontal').grid(row=5, ipadx=300)

        hr2 = ttk.Separator(self, orient='horizontal').grid(row=9, ipadx=300) 
        Label(self, text="Decryption", bg='white smoke',fg='grey',  font=(None, 13, 'bold')).grid(row=8)


    def create_field(self):
        """
        This method creates the text box and scrollbar of the home page
            
        """         

        # creating a text box and scrollbar for the input
        global text_box
        yscrollbar = Scrollbar(self)
        text_box = Text(self, height=10, width=60, yscrollcommand=yscrollbar.set)
        text_box.tag_add('center', 1.0 , 'end')
        title="Please submit your sequence if you haven't a .txt file:"
        Label(self, text=title, bg='white smoke',fg='grey', font=("Arial", 10, "bold", "italic")).grid(row=2)
        text_box.grid(row=3)
        
        # Placing the scrollbar

        yscrollbar.place(in_=text_box, relx=1, relheight=1, bordermode='outside')
        yscrollbar.config(command=text_box.yview)


    def get_input(self) :
        """
        This method is used to get the sequence entered manually from the user
        Returns:
            
        """
        self.text_box_content += text_box.get(1.0, END)
        return self.text_box_content

    def create_buttons(self):  
        """
        This method creates the five buttons of the home page
            
        """            
        Button(self, text="BWT encryption",command=self.bwt_encryption, width = 20,height=2,bg='SlateBlue4', fg='white').grid(row=6,column=0,padx=70 ,sticky='w')
        Button(self, text="Huffman compression", command=self.bwt_decryption, width = 20,height=2,bg='SlateBlue4', fg='white').grid(row=6,padx=70,sticky='e')
        
        Button(self, text="BWT decryption",width = 20,height=2,bg='SlateBlue4', fg='white').grid(row=10,column=0,padx=70 ,sticky='w')
        Button(self, text="Huffman decompression",width = 20,height=2,bg='SlateBlue4', fg='white').grid(row=10,padx=70,sticky='e')
        
        Button(self, text="Quit",width = 20,height=2,bg='SlateBlue4', fg='white').grid(row=11, pady=15)


    def menu(self):
        """
        This method creates a menu bar that contains choose file tab
        """

        menu_bar = Menu(self)

        bar = Menu(menu_bar, tearoff=0)
        bar.add_command(label="Open File",command=self.open_and_get_file, accelerator="Ctrl+o")
        menu_bar.add_cascade(label="Open File", menu=bar)
        self.bind_all("<Control-o>", lambda o: self.open_and_get_file())
        self.config(menu=menu_bar)
        
    def open_and_get_file(self):
        """
        This method opens and gets the file content when selected by storing it in the class's
        property sequence
        """

        self.file = filedialog.askopenfilename(title="Select open file :",
                                              initialdir=os.getcwd()+"/data",
                                              filetypes=(("Text Files","*.txt"),))
        if self.file:
            messagebox.showinfo("Selected file", "Successfully selected: %s"%(self.file))
            with open(self.file, 'r') as f:
                line = f.read()
                for char in line:
                    if char != '\n':
                        self.sequence += char

    def get_text_or_file(self):
        """ 
        A method to get content of sequence entered manually or file if selected

        """   
        if self.file is not None:
            return self.sequence
        else :
            return self.get_input()
            

    def popup(self, title:str):
        """ A method that creates a toplevel (popup) window

        Args:
            title:str: the title of the toplevel window
        """
        global top, next_button, next_text
        top = Toplevel()
        top.geometry("500x230")
        top.title(title)
        next_text = StringVar()
        next_button = Button(top, textvariable=next_text, bg='SlateBlue4', fg='white', height=2, width=20)
        next_text.set('next')
        next_button.grid(row=4)
        
    def insert_in_text_box(self, inserted_object:str):
        """ A method to insert in the text box

        Args:
            inserted_object:str: text to insert
        """
        global popup_text_box 

        # adding a scroll bar
        yscrollbar = Scrollbar(top)

        # creating the text box
        popup_text_box = Text(top, height=10, width=60 , yscrollcommand=yscrollbar.set)     
        popup_text_box.insert(END, inserted_object)
        popup_text_box.tag_configure('center', justify='center')
        popup_text_box.tag_add('center', 1.0, END)
        popup_text_box.grid(row=3)
        yscrollbar.place(in_=popup_text_box, relx=1, relheight=1)
        yscrollbar.config(command=popup_text_box.yview)


    def bwt_encryption(self):
        """ 
        A method to proceed the Burrows Wheeler Transform encryption from the input (text or file)
        Asking for doing it in a pedagogical way (step by step) or not ( displaying final bwt sequence)

        """
        global inbox
        global bwt_sequence
        global content
        global results_bwt

        # Content of the file or manually entered sequence
        content = self.get_text_or_file()
        # Remove spaces and saving sequence as controller's property
        self.controller.sequence = content.strip()
        ask_quest = askquestion('Bwt encryption', 'Would you like to go step by step ?')
        results_bwt = self.controller.bwt_encryption_steppers()

        # Getting bwt resulting sequence for the non pedagogic way
        bwt_sequence = results_bwt[1]

        if ask_quest == 'yes':
            inbox = 'Step 1: Rotations'
            self.popup('BWT encryption')
            self.insert_in_text_box(inbox)
            next_button.configure(command=lambda:self.get_next(inbox))

        else:  #only final result
            self.popup('BWT encryption')
            text = 'The final BWT sequence is:\n' + bwt_sequence
            self.insert_in_text_box(text)
            # Saving process when choosing to get final sequence directly
            next_text.set('Save')
            next_button.configure(command= lambda : self.save_results(bwt_sequence))



    def get_next(self, inbox:str):
        """ 
        Method to get the next steps of BWT when clicking on next button
        Args:
            inbox:str: the informations used for the text box (steps and/or final bwt sequence)

        """
        # Getting the unsorted matrix for 1st step
        bwt_matrix = results_bwt[0]
        # End step 1 if length of the matrix is equal to unduplicated matrix
        if len(bwt_matrix) != len(list(dict.fromkeys(bwt_matrix))) :
            try :
                inbox = ''
                inbox += popup_text_box.get("1.0", END) + next(iter(bwt_matrix))
                self.insert_in_text_box(inbox)           
                del bwt_matrix[0]

            except BaseException: 
                print("Oops..Something went wrong..")
        # Start step 2 (sorting and identifying transform) when step 1 ends
        else:
            lines = []
            bwt_sorted_matrix = ''
                
            for i in sorted(results_bwt[0]):
                bwt_sorted_matrix += str(i) + '\n'
                lines.append(str(i))
                
            inbox = 'Step 2: Sorted Rotations\n' \
                + bwt_sorted_matrix + '\nThe final BWT sequence is: ' + bwt_sequence
            self.insert_in_text_box(inbox)

            # Coloration of the transform
            index = 2
            for i in lines:
                col = str(index) + '.' + str(len(i) - 1)
                popup_text_box.tag_add('color', col)
                popup_text_box.tag_config('color', foreground='red')
                index += 1
            # Saving after the step by step method
            next_text.set('Save')
            next_button.configure(command= lambda : self.save_results(bwt_sequence))



    def bwt_decryption(self):
        """ 
        A method to proceed the Burrows Wheeler Transform decryption from the input (text or file)
        Asking for doing it in a pedagogical way (step by step) or not (displaying final sequence)

        """
        # Content of the file or manually entered sequence
        content = self.get_text_or_file()
        # Remove spaces and saving sequence as controller's property
        self.controller.sequence = content.strip()
        ask_quest = askquestion('Bwt decryption', 'Would you like to go step by step ?')
        results_bwt = self.controller.bwt_encryption_steppers()

        # Getting bwt resulting sequence for the non pedagogic way
        bwt_sequence = results_bwt[1]

        if ask_quest == 'yes':
            inbox = 'Step 1: Rotations'
            self.popup('BWT encryption')
            self.insert_in_text_box(inbox)
            next_button.configure(command=lambda:self.get_next(inbox))

        else:  #only final result
            self.popup('BWT encryption')
            text = 'The final BWT sequence is:\n' + bwt_sequence
            self.insert_in_text_box(text)
            # Saving process when choosing to get final sequence directly
            next_text.set('Save')
            next_button.configure(command= lambda : self.save_results(bwt_sequence))

TODO: finish decryption same logic a s encryption

    def save_results (self, seq: str):
        """ 
        Method to save the results of each algorithm

        Args:
            seq:str: The result to to be saved in a file
        """
        file = asksaveasfile(initialdir=os.getcwd(), title="Select File", mode='w', defaultextension='.txt')
        with open(file.name, 'w') as f:
            f.write(seq)
        messagebox.showinfo('Done', 'File saved successfully!')
            


    def main(self):
        print("[View] main")
        self.mainloop()















