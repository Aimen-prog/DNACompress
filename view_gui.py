#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Aimen CHERIF

User interface
"""
import re
import ast
import os
from tkinter import Tk
from tkinter import ttk
from tkinter import Menu, filedialog, Button
from tkinter import Entry, Text, Scrollbar, messagebox
from tkinter import Label, Toplevel, END
from tkinter import StringVar
from tkinter.filedialog import asksaveasfile
from tkinter import PhotoImage
from tkinter.messagebox import askquestion, askokcancel

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
        Button(self, text="Huffman compression",command=self.huffman_compression, width = 20,height=2,bg='SlateBlue4', fg='white').grid(row=6,padx=70,sticky='e')

        Button(self, text="BWT decryption",command=self.bwt_decryption,width = 20,height=2,bg='SlateBlue4', fg='white').grid(row=10,column=0,padx=70 ,sticky='w')
        Button(self, text="Huffman decompression", command=self.huffman_decompression, width = 20,height=2,bg='SlateBlue4', fg='white').grid(row=10,padx=70,sticky='e')
   
        Button(self, text="Reset", command=self.reset_entries, width = 20,height=2,bg='SlateBlue4', fg='white').grid(row=11, pady=15)


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
            text_box.configure(state="disabled")
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
        """ 
        A method that creates a toplevel (popup) window
        Args:
            title:str: the title of the toplevel window
        """
        global top, next_button, next_text
        top = Toplevel()
        top.geometry("500x230")
        top.title(title)
        next_text = StringVar()
        next_button = Button(top, textvariable=next_text, bg='SlateBlue4', fg='white', height=2, width=20)
        next_text.set('Next')
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
        global inbox, bwt_sequence, results_bwt, content
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
            # Coloring final BWT sequence
            popup_text_box.tag_config("start", foreground="red")
            popup_text_box.tag_add("start", "2.0", END)
            self.file = None
            self.sequence = ''
            self.controller.sequence = ''
            self.text_box_content=''
            

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
        global original_sequence, bwt_recon_matrix, in_box

        # Content of the file or manually entered sequence
        content = self.get_text_or_file()
        # Remove spaces and saving sequence as controller's property
        self.controller.sequence = content.strip()
        
        # step by step decryption
        ask_question = askquestion('Bwt decryption', 'Would you like to go step by step ?')

        # Getting bwt decryption resulting sequence for the non pedagogic way
        original_sequence= self.controller.bwt_decryption_steppers()[1]
        
        
        if ask_question == 'yes':
            in_box = 'Recuperating the BWT entered sequence..\n' + self.controller.sequence +\
                '\n\nStep 1: Sorting decryption matrix by lexicographical order:' 
            self.popup('BWT decryption')
            self.insert_in_text_box(in_box)
            next_button.configure(command=lambda:self.get_next_decryption(in_box)) 

        else:  #only final result
            try :
                self.popup('BWT decryption')
                text = 'The sequence after the BWT decryption is:\n' + original_sequence +\
                    "\n\n==>The final sequence is:\n" + original_sequence.strip()[: -1]
                self.insert_in_text_box(text)
                # Saving process when choosing to get final sequence directly
                next_text.set('Save')
                next_button.configure(command= lambda : self.save_results(original_sequence.strip()[: -1]))
                # Coloring final sequence
                popup_text_box.tag_config("start", foreground="red")
                popup_text_box.tag_add("start", "5.0", END)    
                self.file = None
                self.sequence = ''
                self.controller.sequence = ''
                self.text_box_content=''            

            #Error message
            except BaseException:
                self.insert_in_text_box("An Error has occured, please try again!")
                next_text.set('Help')
                next_button.configure(command=lambda:self.possible_reasons_bwt())
                self.file = None
                self.sequence = ''
                self.controller.sequence = ''
                self.text_box_content=''

    def get_next_decryption(self, inbox:str):
        
        """ 
        Method to get the next steps of decryption process of BWT when clicking on next button
        Args:
            inbox:str: the informations used for the text box (steps and/or final sequence)

        """
        # Getting the sorted reconstruction matrix of decryption
        bwt_recon_matrix= self.controller.bwt_decryption_steppers()[0][1]
        # Next clicks
        try :
            inbox = ''
            inbox += popup_text_box.get("1.0", END) + next(iter(bwt_recon_matrix))
            self.insert_in_text_box(inbox)           
            del bwt_recon_matrix[0]
        # Step 3 and Saving sequence
        except BaseException:

            inbox += popup_text_box.get("1.0", END) + \
                '\nStep 2: Getting the sequence ending with $ symbol:' + '\n'+ original_sequence + "\n==>The final sequence is:\n" + original_sequence.strip()[: -1]
            self.insert_in_text_box(inbox)
            
            # Saving after the step by step method
            next_text.set('Save')
            next_button.configure(command= lambda : self.save_results(original_sequence.strip()[: -1]))


    def huffman_compression(self):
        """ 
        A method to proceed the Huffman compression process from the input (text or file)
        Asking for doing it in a pedagogical way (step by step) or not (displaying final sequence)

        """
        # Result will be stocked here in global for next method
        global huff_unicode, rebuilder_str
        # Content of the file or manually entered sequence
        content = self.get_text_or_file()
        # Remove spaces and saving sequence as controller's property
        self.controller.sequence = content.strip()
        
        # step by step Huffman compression
        ask_question = askquestion('Huffman compression', 'Would you like to go step by step ?')

        # Getting result of Huffman compression for the non pedagogic way
        huff_unicode= self.controller.huffman_compression_steppers()[3]
        # Getting paths dict to be saved with unicode
        rebuilder = self.controller.huffman_compression_steppers()[4]
        rebuilder_str = str(rebuilder)
    
        if ask_question == 'yes':
            # Getting the tree as a str from controller
            huff_tree= self.controller.huffman_compression_steppers()[0]
            in_box = 'Recuperating the entered sequence..\n' + self.controller.sequence +\
                '\nStep 1: Building Huffman binary tree:\n\n' + huff_tree             
            self.popup('Huffmann Compression')
            self.insert_in_text_box(in_box)
            next_button.configure(command=lambda:self.get_next_huff(in_box))

        else:  #only final result (unicode sequence)
            try :
                self.popup('Huffmann compression')
                text = 'The unicode resulted from the Huffmann compression is:\n' + huff_unicode
                self.insert_in_text_box(text)
                # Saving process when choosing to get final sequence directly (save final sequence and paths)
                next_text.set('Save')
                next_button.configure(command= lambda : self.save_results(huff_unicode,rebuilder_str))
                # Coloring final Huffmann unicode
                popup_text_box.tag_config("start", foreground="red")
                popup_text_box.tag_add("start", "2.0", END)
                self.file = None
                self.sequence = ''
                self.controller.sequence = ''
                self.text_box_content=''  

            except BaseException:
                self.insert_in_text_box("An Error has occured, please try again!")
                next_text.set('')


    def get_next_huff(self, inbox:str):
        
        """ 
        Method to get the next steps of Huffman compression when clicking on next button
        Args:
            inbox:str: the informations used for the text box (steps and/or final result)

        """
        # Getting binary code with potential padding from Huffman compression: the pedagogic way
        huff_binary_no_pad = self.controller.huffman_compression_steppers()[1]        
        huff_binary_pad = self.controller.huffman_compression_steppers()[2]       

        inbox +='\n\nStep 2: The corresponding binary sequence with no padding:\n' + huff_binary_no_pad + \
            "\n\nStep 3: Binary sequence after possible padding addition :\n" + huff_binary_pad +\
                '\n\nStep 4: Translating to unicode (final result):\n' + huff_unicode
        self.insert_in_text_box(inbox)      
        # Saving paths + final result after the step by step method
        next_text.set('Save')
        next_button.configure(command= lambda : self.save_results(huff_unicode,rebuilder_str))
        
        
    def huffman_decompression(self):
        """ 
        A method to proceed the Huffman decompression process from the input (text or file)
        Doing it in a pedagogical way (step by step)

        """
        # Unicode entered manually stocked in controller's property
        self.controller.unicode_seq = self.get_input()

        # Content of the file:
        # This content need to have an encoder dict as str (paths of character) in the first line
        self.open_and_get_file()
        content = self.sequence
        self.controller.unicode_seq=content.strip()

        # Extracting only the dict (as str) from the contener
        found = re.search('{(.+?)}', content).group(1)
        content_found= "{" + found + "}"
        # Get dict as str from first line, and reconverting it into real str
        rebuilder_dict = ast.literal_eval(content_found)
        # Getting results of Huffman decompression
        seq_pad= self.controller.huffman_decompression_steppers(rebuilder_dict)[0]
        seq_no_pad= self.controller.huffman_decompression_steppers(rebuilder_dict)[1]
        origin_sequence= self.controller.huffman_decompression_steppers(rebuilder_dict)[2]

        try :
            self.popup('Huffman decompression')
            text = 'Step 1: Getting binary sequence with potential padding:\n' + seq_pad + '\n' +\
                '\nStep 2: Removal of potential padding:\n' + seq_no_pad + '\n' +\
                '\nThe sequence after the Huffman decompression is:\n' + origin_sequence
            self.insert_in_text_box(text)
            # Saving process when choosing to get final sequence directly
            next_text.set('Save')
            next_button.configure(command= lambda : self.save_results(origin_sequence))

        #Error message
        except BaseException:
            self.insert_in_text_box("An Error has occured, please try again!")
            next_text.set('')
            self.file = None
            self.sequence = ''
            self.controller.sequence = ''
            self.text_box_content=''  


    def save_results (self, seq: str, dict_str:str = ""):
        """ 
        Method to save the results of each algorithm

        Args:
            seq:str: The result to to be saved in a file
            dict_str:str:optional, is the dictionnary of paths but as str to be stucked at first line
            of .txt file (special to huffman compression)
        """
        file = asksaveasfile(initialdir=os.getcwd(), title="Select File", mode='w', defaultextension='.txt')
        with open(file.name, 'a') as f:
            f.write(dict_str + '\n' + seq)
        messagebox.showinfo('Done', 'File saved successfully!')

    def reset_entries(self):
        """ 
        Method to help the user reset entries file/text box content
        """
        text_box.configure(state="normal")
        text_box.delete(1.0, END)
        self.controller.sequence=""
        self.file = None
        if self.file is not None :
            self.input_deselection()

    def possible_reasons_bwt(self):
        """ 
        Method to help the user with a message about possible failure reasons in BWT decryption
        process
        """
        messagebox.showinfo("Possible failure reasons", "- Empty input/file \n- Not a BWT format \n ($ symbol missing)")

    def quit_secure(self):
        """ 
        Method quit the program properly
        """
        response = messagebox.askokcancel("Quit", "Are you sure you want to quit?")
        if response:
            self.destroy()
    
    def input_deselection(self):
        """ 
        Method to display a message when a file is deselected (reset button)
        """
        messagebox.showinfo("Reset done", "Input dropped.\nAll clear!")       

    def main(self):
        print("[View] main")
        self.mainloop()
