#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Aimen CHERIF

The Huffman binary tree implementation with compression and decompression process
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

    def __str__(self):
        if self.right is None and self.left is None:
            return str(self.value)

        return "Node(%s, freq=%s, right=%s, left=%s)"%(self.char,
                                                        self.value,
                                                        self.right,
                                                        self.left)

    def is_leaf(self):     
        """
            method to check if a node is a leaf or not
            a leaf is a single node with nothing on its right and left
            Returns:
                bool: True if it's a leaf, False if not
        """
        return self.left is None and self.right is None


class HuffmanTree:
    """Class for Huffman's binary tree: Compression + Decompression """
    
    def __init__(self, sequence: str):
        """
        Class constructor
        Args:
            sequence:str: representing the sequence to be encoded.
        """      
        self.sequence=sequence
        self.dict_frequency = self.frequency()
        self.char_codings={}
        self.seq_bin_coding = ''   #for the binary sequence
        self.padding_count=0
        self.unicode= ''
        #decompression process
        self.binary_seq = ''
        self.binary_seq_nopad = ''

    def frequency(self):
        
        """ 
        This method calculates the frequency of each character in the sequence
        and stores it in a dictionary
            
        Returns:
            dict:{str:int}: The key is the character and its value represents its frequency
        """ 

        frequency = {}
        for char in self.sequence.upper():
            if char in frequency.keys():
                frequency[char] += 1
            else:
                frequency[char] = 1
        return frequency


    def tree_implementation(self) :
        """ 
        This method creates the binary tree

        Returns:
            HuffmanNode: The root node of the tree (first element of a list)
        """

        tree_leafs= []
        for char, freq in self.dict_frequency.items() :
            tree_leafs.append(HuffmanNode(char, freq))
        
        while len(tree_leafs)>1 :
            #Sorting the list to have the smallest values in st place
            tree_leafs=sorted(tree_leafs , key=lambda x:x.value)
            
            #merging the two first nodes :
            # The new frequency is the sum of both frequencies
            new_freq = tree_leafs[0].value + tree_leafs[1].value
            # The new character
            new_char = tree_leafs[0].char + tree_leafs[1].char

            # The new resulting root node
            root = HuffmanNode(new_char, new_freq, tree_leafs[0], tree_leafs[1])
            
            # Set 0 for the first direction
            tree_leafs[0].direction = '0'
            # Delete from the list
            del tree_leafs[0]
            
            # Set 1 for the second direction
            tree_leafs[0].direction = '1'
            # Delete from the list
            del tree_leafs[0]

            # The new resulting root node added to the node list
            tree_leafs.append(root)

        return tree_leafs[0]


    def char_codes(self, node: HuffmanNode, bins=''):

        """ A method to create character's binary code according to its path in the Huffman 
            binary tree. Each character will have a binary code as a value in class's 
            dictionary char_codings
        Args:
            node:TreeNode: root of the tree
            bins:str: current binary code- empty by default
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

        for char in self.sequence.upper():
            if char in self.char_codings.keys():
                self.seq_bin_coding += self.char_codings[char]

    def padding_to_binary(self, seq_bin : str):

        """ A method that transforms a binary sequence by adding zeros (padding) 
        to its end to make it divisible by 8 (sequence will be coded in 8-bits afterwards)
        Also stores number of added zeros as preparation for the decompression process.

        Args:
            seq_bin:str: binary sequence from original sequence

        Returns:
            str: the binary sequence after padding additions
        """
        # Count of the number of added zeros
        padding = 0

        while len(seq_bin) % 8 != 0:
            seq_bin = seq_bin + '0'
            padding += 1

        self.padding_count = padding
        return seq_bin


    def binary_to_unicode(self):

        """ A method that codes the binary sequence in 8-bits """

        pad_seqbin = self.padding_to_binary(self.seq_bin_coding)

        for bit in range(0, len(pad_seqbin), 8):
            byte = pad_seqbin[bit:bit+8]
            bin_code = int(byte, 2)
            self.unicode += chr(bin_code)


    ####Decompression section####
    
    def get_binary_from_unicode(self):
        
        """ A method that gets the binary sequence from unicode """

        # Coverting unicode sequence to binary sequence
        for char in self.unicode:
            ord_char = ord(char)
            self.binary_seq = '' + format(ord_char, '08b')
        # Padding removal
        self.binary_seq_nopad = self.binary_seq[:-self.padding_count]



    def decompression(self, rebuilder:dict):
        """ A method that decompresses the unicode sequence into the initial sequence 
        
        Args:
            rebuilder:dict: dictionnary of characters and their corresponding paths
        
        Returns:
            str: decompressed (initial) sequence

        """       
        # Rebuilding the initial DNA sequence and returning it
        sequence=''
        for bins in self.binary_seq_nopad:
            path = "" + bins
            for key, value in rebuilder.items():
                if value == path:
                    sequence += key
                    path = ""
        return sequence
