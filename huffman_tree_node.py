#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Aimen CHERIF

The Huffman binary tree implementation
"""

class TreeNode :

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
        self.left = None
        self.right = None
        
    def is_leaf(self):
        
        """
            method to check if a node is a leaf or not
            a leaf is a single node with nothing on its right and left
            Returns:
                bool: True if it's a leaf, False if not
        """
        return self.left is None and self.right is None
        
        
        
        
        
        
        
        
        
        
        
        
        
        