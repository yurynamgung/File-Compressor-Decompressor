# File-Compressor-Decompressor
Huffman file compressor 

ENCODING AND COMPRESSING:
The program reads in a file and calculates the frequency of each symbol's occurence. 
Then it builds an encoding tree for this set of frequencies. 

Refer to the following page for more background on the type of encoding tree used:
https://www.wikiwand.com/en/Huffman_coding#/Compression

The program builds a prefix code from this tree, which it uses to convert the file into binary.
It then packs 8-bit 'chunks' of the binary code into bytes.

OUTPUT:
The program saves this encoded and compressed file into a filename.txt.HUFFMAN and a HUFFMAN key 
in a filename.txt.HUFFMAN.key file. 
The program also gives the user the compressed text length in bytes and the asymptotic compression ratio. 

DECOMPRESSOR:
The program uses the key and huffman files to uncompress the compressed file, which it then 
saves into a filename.txt.HUFFMAN.DECODED file. 

