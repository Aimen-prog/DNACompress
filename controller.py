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
        self.huff = None

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
        This method helps the step by step the Burrows Wheeler decryption. 
        Same logic as encryption steppers method's way
        
        Returns:
            (bwt_reconstruction_matrix, original_sequence):tuple: the matrix of bwt decryption for step
            by step process and the final bwt sequence          
        """
        self.BurrowsWheeler.seq_reconstruction(self.sequence) 
        bwt_reconstruction_matrix = self.BurrowsWheeler.bwt_reconstruction_steppers
        original_sequence = self.BurrowsWheeler.seq_reconstruction(self.sequence)
        return (bwt_reconstruction_matrix, original_sequence)


    def huffman_compression_steppers(self):
        """
        This method helps the step by step Huffman compression by calling all steps in order to be
        exploited later.
        Returns:
              (tree_bin, binary_no_pad, binary_with_padding, unicode):tuple: tree as string,
              Binary sequence without padding, with padding (if needed) and the final
              unicode sequence of Huffman's compression
              
        """
        # Initialization
        self.huff = HuffmanTree(self.sequence.upper())
        
        # Tree 
        tree = self.huff.tree_implementation()
        tree_bin= tree.__str__()

        # Binary
        self.huff.char_codes(tree)
        self.huff.sequence_to_binary()    
        binary_no_pad=self.huff.seq_bin_coding 
    
        # Unicode
        self.huff.padding_to_binary(self.huff.seq_bin_coding)
        binary_with_padding= self.huff.padding_to_binary(self.huff.seq_bin_coding)
        self.huff.binary_to_unicode()


        char_codes = self.huff.char_codings     
        unicode = self.huff.unicode
        return (tree_bin, binary_no_pad, binary_with_padding, unicode)


           
if __name__ == "__main__":
    controller = Controller()
    controller.start_view()
    controller.bwt_encryption_steppers()
    controller.bwt_decryption_steppers()
    controller.huffman_compression_steppers()





