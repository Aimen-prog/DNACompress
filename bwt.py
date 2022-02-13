#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Aimen CHERIF

The Burrows–Wheeler transform (BWT): 
    the transformation permutes the order of the characters

"""

class BurrowsWheeler :

    """Class of the transformation of Burrows-Wheeler"""
    
    def __init__(self, sequence : str):
        
        """
        Args:
            sequence(str): DNA sequence to be transformed by BWT matrix

        """
        self.sequence= sequence.upper() + "$"


    def bwt_construction(self):

        """ 
        method to obtain the BWT sequence using a BWT construction matrix
        
        Returns :
            BWT sequence of the initial DNA sequence
        
        """

        seq_len = len(self.sequence)
        previous_sequence = self.sequence
        
        # Initialization of the BWT construction matrix
        construction_matrix=[self.sequence]
        
        # Completing the BWT construction matrix      
        for i in range (0, seq_len-1, 1) :
            next_sequence=previous_sequence[-1] + previous_sequence[0:seq_len-1]
            
            #adding it to the matrix      
            construction_matrix.append(next_sequence)

            #previous variable takes this sequence for next iteration
            previous_sequence = next_sequence
        
        # Sorting the BWT construction matrix
        construction_matrix_sorted= sorted(construction_matrix)
        
        # Getting the BWT sequence as the accumulation of the last character of each row
        bwt = ""
        for row in construction_matrix_sorted :
            bwt+=row[-1]

        return bwt
    
    
    def bwt_reconstruction (self, bwt : str):
        
        """
        method to obtain the original sequence from BWT sequence using a BWT 
        reconstruction matrix
        
        Args:
            bwt(str): sequence already transformed by BWT algorithm.
        Returns:
            initial DNA sequence

        """
        reconstruction_matrix=list(bwt)
        reconstruction_matrix=sorted(reconstruction_matrix)
        pass
        











