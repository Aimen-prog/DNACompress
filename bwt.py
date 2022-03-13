#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Aimen CHERIF

The Burrows–Wheeler transform (BWT): 
    the transformation permutes the order of the characters
"""

class BurrowsWheeler :

    """Class of the transformation of Burrows-Wheeler"""
    
    def __init__(self, controller):
        """
        Class constructor
        Args:
            sequence:str: DNA sequence to be transformed by BWT matrix

        """
        self.controller = controller
        self.bwt_construction_steppers = []
        self.bwt_construction_final = []
        self.bwt_reconstruction_steppers = []

    def bwt_construction(self, seq:str):

        """ 
        method to obtain the BWT sequence using a BWT construction matrix

        Args:
            seq:str: DNA sequence to be transformed by BWT matrix

        Returns:
            str: The BWT result of the sequence
        
        """

        # Unify and add '$' 
        sequence = seq.upper() + "$"
        seq_len = len(sequence)
        previous_sequence = sequence
       
        # Initialization of the BWT construction matrix
        construction_matrix=[sequence]
        self.bwt_construction_steppers.append(sequence)

        # Completing the BWT construction matrix      
        for i in range (0, seq_len-1, 1) :
            next_sequence = previous_sequence[-1] + previous_sequence[0:seq_len-1]
            # Adding it to class's property construction list
            self.bwt_construction_steppers.append(next_sequence)
            # Adding it to the matrix      
            construction_matrix.append(next_sequence)
            # Previous variable takes this sequence for next iteration
            previous_sequence = next_sequence

        # Sorting the BWT construction matrix
        construction_matrix_sorted= sorted(construction_matrix)
        # Keeping the final matrix in class's property list
        self.bwt_construction_final = construction_matrix_sorted
        # Getting the BWT sequence as the accumulation of the last character of each row
        bwt = ""
        for row in construction_matrix_sorted :
            bwt+=row[-1]

        return bwt

    
    def seq_reconstruction (self, bwt : str):
        
        """
        method to obtain the initial sequence from its BWT sequence using a sequence
        reconstruction matrix

        Args:
            bwt:str: sequence already transformed by BWT algorithm
        Returns:
            str: initial DNA sequence

        """
        # Initialization of the reconstruction matrix with a sorted BWT sequence
        reconstruction_matrix=list(bwt)
        reconstruction_matrix.sort()
        # Assign the sequence as the first step of reconstruction class's list
        self.bwt_reconstruction_steppers.append(reconstruction_matrix)
        
        # Filling the reconstruction matrix
        for i in range(0, len(bwt)-1, 1):
            for j in range(0, len(bwt), 1):
                reconstruction_matrix[j] = bwt[j] + reconstruction_matrix[j]
            # Sort each line according to lexicographical order
            reconstruction_matrix.sort()
            # Next steps addition to class's reconstruction list
            self.bwt_reconstruction_steppers.append(reconstruction_matrix)
        # Getting the line with '$' as last character
        for row in reconstruction_matrix :
            if row[-1] == "$" :
                sequence = row
                return sequence
