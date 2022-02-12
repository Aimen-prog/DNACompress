#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Aimen CHERIF

The Burrows–Wheeler transform (BWT): the transformation permutes the order of the characters

"""

class BurrowsWheeler :

    """Class of the transformation of Burrows-Wheeler"""
    
    def __init__(self, sequence : str):
        
        """
        Args:
            sequence(str): DNA sequence to be transformed by BWT algorithm.

        """
        self.sequence= sequence.upper() + "$"


    def bwt_construction(self):

        """ The method to obtain the BWT sequence """

        seq_len = len(self.sequence)
        previous_sequence = self.sequence
        
        # Initialization of the BWT construction matrix
        contruction_matrix=[self.sequence]
        
        # Completing the BWT construction matrix      
        for i in range (0, seq_len-1, 1) :
            next_sequence=previous_sequence[-1] + previous_sequence[0:seq_len-1]
            
            #adding it to the matrix      
            contruction_matrix.append(next_sequence)

            #previous variable takes this sequence for next iteration
            previous_sequence = next_sequence
        
        # Sorting the BWT construction matrix
        construction_matrix= sorted(contruction_matrix)
        
        # Getting the BWT sequence as the accumulation of the last character of each row
        bwt = ""
        for row in construction_matrix :
            bwt+=row[-1]

        #return bwt
        print(bwt)
        print(construction_matrix)



if __name__=='__main__':
    b = BurrowsWheeler('AGTAC')
    b.bwt_construction()
    



















