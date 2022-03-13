#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Controller class of the program

"""

__author__ = 'Aimen CHERIF'

from view_gui import View
from bwt import BurrowsWheeler
from huffman_tree_node import HuffmanNode, HuffmanTree

class Controller:
    def __init__(self):
        self.view = View(self)
        self.BurrowsWheeler = BurrowsWheeler(self)
        self.sequence=''
        self.count=0

    def start_view(self):
        """
        Method for interface visibility
        """
        self.view.create_space()
        self.view.create_field()
        self.view.create_buttons()
        self.view.menu()
        self.view.main()


    def bwt_encryption_steppers(self):
        """
        Method to help the step by step bwt encryption by returning matrix as an addition
        to the final bwt sequence
        
        Returns:
            bwt_unsorted_matrix, bwt_sequence:tuple: the unsorted matrix of bwt encryption 
            and the final bwt sequence
            
        """
        self.BurrowsWheeler.bwt_construction(self.sequence)
        bwt_unsorted_matrix = self.BurrowsWheeler.bwt_construction_steppers
        bwt_sequence = self.BurrowsWheeler.bwt_construction(self.sequence)
        return (bwt_unsorted_matrix, bwt_sequence)


    def bwt_decryption_steppers(self):
        """
        This method helps the step by step the Burrows Wheeler decryption. Same logic as encryption
        steppers method
        
        Returns:
            bwt_reconstruction_matrix, original_sequence:tuple: the matrix of bwt decryption for step
            by step process and the final bwt sequence          
        """
        self.BurrowsWheeler.seq_reconstruction(self.sequence) 
        bwt_reconstruction_matrix = self.BurrowsWheeler.bwt_reconstruction_steppers
        original_sequence = self.BurrowsWheeler.seq_reconstruction(self.sequence)
        return (bwt_reconstruction_matrix, original_sequence)



  
           
if __name__ == "__main__":
    controller = Controller()
    controller.start_view()
    controller.bwt_encryption_steppers()
    controller.bwt_decryption_steppers()






