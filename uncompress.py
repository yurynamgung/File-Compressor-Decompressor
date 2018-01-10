#Yury Namgung
#CS Black
# Due 8 Nov 2017

import binary

"""main function"""
def uncompress():

    """takes in fileName from user that ends w .HUFFMAN"""
    while True:
        inputFile = input("What file would you like to decode? ")
        if inputFile[-8:] == '.HUFFMAN':
            break
        else:
            print("This file does not end with .HUFFMAN")
    
    keyFile = inputFile + ".KEY" 

    f1 = open(inputFile, "rb")
    readBytes = f1.read()
    f1.close()
    byteList = list(readBytes)

    f2 = open(keyFile, 'r') #read in huffman key
    keyList = f2.readlines()
    f2.close()

    #remake prefix dictionary
    prefixDict = make_prefixDict(keyList)
    
    #turn huffman file into binary chunkList 
    totChars = keyList[1][:-1]
    return

"""remake prefix dictionary from .HUFFMAN.KEY file"""
def make_prefixDict(inputList):
    prefixList = inputList[2:] # cut off # dist char & # bits
    dict = {}

    for l in range(len(prefixList)):
        if prefixList[l] == '\n': # b/c spaces are formatted weird
            dict[prefixList[l]] = prefixList[l+1][:-1]
            l+=1
        else:
            dict[prefixList[l][0]] = prefixList[l][1:-1] #cut out the last 2 chars (\n)
    return dict

"""turn byteList into binary and convert to words"""
def interpret_binary(byteList, totChars):
    list(map(lambda x: binary.EightBitNumToBinary(x), byteList))
    
    #take out padding (0s at end)
    
    
