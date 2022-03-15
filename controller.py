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
        self.unicode_seq=''

    def start_view(self):
        """
        Method for interface visibility
        """
        self.view.protocol("WM_DELETE_WINDOW", self.quit_program)
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
              (tree_bin, binary_no_pad, binary_with_padding, unicode, rebuilder):tuple: tree as string,
              Binary sequence without padding, with padding (if needed), the final unicode sequence
              of Huffman's compression and finally the rebuilder (dict) for each character path used 
              (saved for decompression use)
              
        """
        # Initialization
        self.huff = HuffmanTree(self.sequence.upper())
        
        # Tree 
        tree = self.huff.tree_implementation()
        tree_bin= tree.__str__()

        # Binary
        self.huff.char_codes(tree)
        rebuilder = self.huff.char_codings #will be important for decompression
        self.huff.sequence_to_binary()    
        binary_no_pad=self.huff.seq_bin_coding 
    
        # Unicode
        self.huff.padding_to_binary(self.huff.seq_bin_coding)
        binary_with_padding= self.huff.padding_to_binary(self.huff.seq_bin_coding)
        self.huff.binary_to_unicode()
 
        unicode = self.huff.unicode
        return (tree_bin, binary_no_pad, binary_with_padding, unicode, rebuilder)


    def huffman_decompression_steppers(self, rebuilder: dict):
        """
        This method helps the step by step Huffman decompression
        Args:
            rebuilder:dict: A dictionnary with the path of each character as value, used to help rebuilding
            the sequence of origin
        Returns:
            (bins_pad,bins,binary_to_sequence):tuple: binary sequence of the unicode with padding,without paddings
            and the original sequence from unicode

        """
        # Initialization
        self.huff = HuffmanTree("")     
        # Binary sequence processing         
        self.huff.get_binary_from_unicode(self.unicode_seq, rebuilder)

        self.huff.sequence_to_binary()
        # Binary sequence pad    
        bins_pad = self.huff.binary_seq_pad
        # Binary sequence no padding
        bins= self.huff.binary_seq_nopad

        # Original sequence
        binary_to_sequence=self.huff.decompression(rebuilder)

        return (bins_pad, bins, binary_to_sequence)


    def quit_program(self):
        """
        Method that calls "quit_secure" for quit program confirmation
        """
        self.view.quit_secure()
           
if __name__ == "__main__":
    controller = Controller()
    controller.start_view()
    controller.bwt_encryption_steppers()
    controller.bwt_decryption_steppers()
    controller.huffman_compression_steppers()





