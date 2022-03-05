#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Controller class of the program

"""

__author__ = 'Aimen CHERIF'

from view_gui import View
from bwt import BurrowsWheeler
from huffman_tree_node import HuffmanNode, HuffmanTree

class Controller():
    def __init__(self):
        self.view = View(self)

    def start_view(self):
        """
        Method interface visibility
        """
        self.view.create_space()
        self.view.main()
        
    def seq_to_bwt(self) :
        if self.view.get_value("Sequence") :
            seq = f"{self.view.get_value('Sequence')}"
            bt= BurrowsWheeler(seq)
            bwt=bt.bwt_construction()
            self.view.display_bwt_seq(bwt)


    def button_press_handle(self, button_id):
        """
        Method for executing search() or delete() or insert() methods
        """
        print("[Controller][button_press_handle] "+ button_id)

        if button_id == "Sequence to BWT":
            self.seq_to_bwt()
        elif button_id == "BWT to sequence":
            pass
        elif button_id == "Huffman compression":
            pass
        elif button_id == "Huffman decompression":
            pass
        elif button_id == "Full compression":
            pass
        elif button_id == "Full decompression":
            pass
                
           
if __name__ == "__main__":
    controller = Controller()
    controller.start_view()






