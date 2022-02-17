#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Aimen CHERIF

The Huffman binary tree implementation
"""

class HuffmanNode:

    """Class for tree node"""
 
    def __init__(self, char: str, value: int, left=None ,right=None):
        """
        Class constructor
        Args:
            char:str: Character to be treated by Huffman's algorithm
            value:int: The frequency of a character
        """
        self.char = char
        self.value = value
        # Node left of current node
        self.left = left
        # Node right of current node
        self.right = right
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
        self.dict_frequency = self.frequency()
        
        
    def frequency(sequence: str):
        
        """ 
        This method calculates the frequency of each character in the sequence
        and stores it in a dictionnary
        
        Args:
            sequence:str: the sequence to be used
            
        Returns:
            dict:{str:int}: The key is the character and its value represents its frequency
        """ 
        freq_char={}
        for char in sequence:
            if not char in freq_char :
                freq_char[char] = 1
            else :
                freq_char[char] = freq_char[char] + 1
        
        return freq_char
    
    
    def tree_implementation(self) :
        """ 
        This method creates the tree

        Returns:
            HuffmanNode: The root node of the tree (first element of a list)
        """ 
        tree_leafs= []
        for char, freq in dict_frequency.items() :
            tree_leafs.append(HuffmanNode(char, freq))
        
        while len(tree_leafs)>1 :
            #Sorting the list to have the smallest values in st place
            tree_leafs=sorted(tree_leafs , key=lambda x:x.value)
            
            #merging the two first nodes :
            # The new frequency is the sum of both frequencies
            new_freq = tree_leafs[0].data + tree_leafs[1].data
            # The new character
            new_char = tree_leafs[0].char + tree_leafs[1].char

            # The new resulting root node
            root = HuffmanNode(new_char, new_freq, tree_leafs[0], tree_leafs[1])
            
            # Set 0 for the first direction
            tree_list[0].direction = '0'
            # Delete it from the list
            tree_leafs.pop(0)
            # Set 1 for the second direction
            tree_leafs[0].direction = '1'
            # Delete it from the list
            tree_list.pop(0)


            # The new resulting root node added to the node list
            tree_leafs.append(root)

        return tree_leafs[0]



    def char_codes(self, node: HuffmanNode, bins: str):

        """ A method to create the binary code according to its path in the Huffman 
            binary tree. Each character will have a binary code as a value in dictionnary.

        Args:
            node:TreeNode: root of the tree
            bins:str: current binary code
        
        Returns:
            codings:dict{str:int}: final dictionnary character and its binary code
        """
        coding={}
        bin_char= bins + node.direction 
        
        
        
        
        
        
        
        

        