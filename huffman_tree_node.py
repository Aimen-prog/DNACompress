#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Aimen CHERIF

The Huffman binary tree implementation
"""

class HuffmanNode:

    """Class for tree node"""
 
    def __init__(self, char: str, value: int):
        """
        Class constructor
        Args:
            char:str: Character to be treated by Huffman's algorithm
            value:int: The frequency of a character
        """
        self.char = char
        self.value = value
        # Node left of current node
        self.left = None
        # Node right of current node
        self.right = None
        # The tree direction
        self.direction = ''
        
    def is_leaf(self):     
        """
            method to check if a node is a leaf or not
            a leaf is a single node with nothing on its right and left
            Returns:
                bool: True if it's a leaf, False if not
        """
        return self.left is None and self.right is None
        

class HuffmanTree:
    """Class for Huffman's binary tree """
        
    def __init__(self, sequence: str):
        """
        Class constructor
        Args:
            sequence:str: representing the sequence to be encoded.
        """      
        self.sequence=sequence
        
        
        
        
        
        
        
        
        