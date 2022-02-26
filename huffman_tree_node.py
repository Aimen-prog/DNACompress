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
            left:Default:None: left child of the node
            right:Default:None: right child of the node
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
        self.char_codings={}
        self.seq_bin = ''
        self.padding_count=0
        
    

    def frequency(sequence: str):
        
        """ 
        This method calculates the frequency of each character in the sequence
        and stores it in a dictionary
        
        Args:
            sequence:str: the sequence to be used
            
        Returns:
            dict:{str:int}: The key is the character and its value represents its frequency
        """ 
        freq_char={}
        for char in self.sequence:
            if not char in freq_char :
                freq_char[char] = 1
            else :
                freq_char[char] = freq_char[char] + 1
        
        return freq_char


    def tree_implementation(self) :
        """ 
        This method creates the binary tree

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
            # Set 1 for the second direction
            tree_leafs[1].direction = '1'
            # Delete from the list
            del tree_leafs[0]
            del tree_leafs[1]

            # The new resulting root node added to the node list
            tree_leafs.append(root)

        return tree_leafs[0]



    def char_codes(self, node: HuffmanNode, bins=''):

        """ A method to create character's binary code according to its path in the Huffman 
            binary tree. Each character will have a binary code as a value in class's 
            dictionary
        Args:
            node:TreeNode: root of the tree
            bins:str: current binary code
        """

        # The path currently setted
        bin_char= bins + node.direction

        if node.left:
            self.char_codes(node.left,bin_char) #recursion on the direction

        if node.right:
            self.char_codes(node.right,bin_char) #recursion on the direction

        if node.is_leaf() :
            self.char_codings[node.char]= bin_char #add the last character



    def sequence_to_binary(self):

        """A method that transforms a whole sequence into a binary sequence according to 
        the path of each character of that sequence
        """

        root_node = self.tree_implementation()
        encoder = HuffmanTree.char_codes(root_node)
        for char in self.sequence:
            self.seq_bin = self.seq_bin + encoder[char]


    def paddings_to_binary(seq_bin : str):

        """ This method transforms a binary sequence by adding zeros (paddings) 
        to its end to make it divisible by 8 (sequence will be coded in 8-bits afterwards)
        Also stores number of added zeros for decompression process.

        Args:
            seq_bin:str: binary sequence from original sequence

        Returns:
            seq_bin:str: binary sequence after padding additions
        """
        # Count of the number of added zeros
        paddings = 0

        while len(seq_bin) % 8 != 0:
            seq_bin = seq_bin + '0'
            paddings += 1

        self.padding_count = paddings
        return seq_bin
    








