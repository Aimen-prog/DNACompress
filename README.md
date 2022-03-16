README
======

# About DNACompress
A DNA compression tool using Burrows-Wheeler and Huffman algorithms.

# Content
1) User enters a DNA sequence manually by writing in the text box in the menu of the program or by selecting a '.txt' file thanks to the bar menu above or by pressing ctrl + o using the keyboard
2) Once sequence selected, user can choose one of the following 4 programs:

- <b>Encryption</b> section: 

i. BWT encryption : Converts a DNA sequence to Burrows-Wheeler format (a transform).
<br>
ii. Huffman compression : Compresses a sequence by passing to Byte format. A resulting BWT sequence can be used for full zip.
<br>
Both of these buttons propose either pedagogical (step by step) processing or getting final result directly. They also propose to save final results in .txt format. The huffman compression saves the final result but also patterns (dictionnary of binary sequence and informations ) crucial for decompression process below.

- <b>Decryption</b> section:

i. BWT decryption : Takes the transform of Burrows-Wheeler and reconstructs the original DNA sequence from it.
<br>
ii. Huffman decompression : Decompresses the unicode (resulted from compression) to give the original sequence (sequence before Huffman compression process). <b>Only</b> a file resulting from the Huffman compression will be necessary (no need to enter sequence manually) as it contains path to orientate the identification of the unicode sequence and therefore for the decompression. The file selection will be directly when clicking the button.
<br>
BWT decryption button propose either pedagogical (step by step) processing or getting directly final result only, while Huffman decryption does the integrality of the steps. These two also propose to save final results in .txt files.

<br>

<b>caution</b>: For the entry of BWT and Huffman (except decompression where input is directly from button), if a .txt file is selected, the text box is disabled thus not considered, to make only one way of entry not both. The button reset give you the possibility to clear entries and re-enter sequence before executing.
<br>
<b>Important: </b> Please restart program after each program use, especially after using step by step mod

# How to execute
This Gui program is executable like this:

```bash
cd ~/Desktop
python3 controller.py

```
# Author
CHERIF Aimen

# License
Open source
