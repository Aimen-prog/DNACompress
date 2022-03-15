README
======

# About DNACompress
A DNA compression tool using Burrows-Wheeler and Huffman algorithms.

# Content
1) User enters a DNA sequence manually by writing in the text box in the menu of the program or by selecting a '.txt' file thanks to the bar menu above or by pressing ctrl + o using the keyboard
2) Once sequence selected, user can choose one of the following 4 programs:

-<b>Encryption</b> section: 

i. BWT encryption : Converts a DNA sequence to Burrows-Wheeler format (a transform).
ii. Huffman compression : Compresses a sequence by passing to Byte format. A resulting BWT sequence can be used for full zip.

Both buttons propose either pedagogical (step by step) processing or getting final result directly. They also propose to save results. The huffman compression saves the final result but also patterns (dictionnary of binary sequence and informations ) crucial for decompression process below.

- <b>Decryption</b> section: 
i. BWT decryption : Takes the transform of Burrows-Wheeler and reconstructs the original DNA sequence from it
ii. Huffman decompression : Decompresses the unicode ( resulted from compression ) to give the original sequence ( sequence before huffman compression process)



# How to execute
This Gui program is executable like this:

```bash
cd ~/Desktop
python3 controller.py

```
