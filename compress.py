#Yury Namgung
#CS Black
# Due 8 Nov 2017

import binary


"""reads file and returns dict w freq of ea symbol"""
def freq(fileInput):
    f1 = open(fileInput, 'r')
    inputList = f1.readlines()
    f1.close()
    
    inputChars = ''
    """make list of chars"""
    for i in range(len(inputList)):
        inputChars += inputList[i]
    """calculate frequency of ea word"""
    countDict = countSymbol(inputChars)
    freqDict = freqCalc(inputChars, countDict) #converts count into freq (probability)
    return [freqDict, inputChars]

"""counts occurances of ea letter and returns count of ea letter"""
def countSymbol(chars, dict ={}):
    for i in range(len(chars)):
        if chars[i] in dict:
            dict[chars[i]] += 1
        else:
            dict[chars[i]] = 1
    return dict

"""calculates freq of ea symbol based on # of occurances"""
def freqCalc(chars, dict):
    for key in dict: 
        dict[key] = dict[key]/len(chars) #divide char count by tot # chars
    return dict

"""returns tuple aka Huffman encoding tree for this set of symbols"""
def build_huffman_tree(frequencies):
    while len(frequencies) >= 2:
        low1 = minfrequency(frequencies)
        freq1 = frequencies[low1]
        del frequencies[low1]
        low2 = minfrequency(frequencies)
        freq2 = frequencies[low2]
        del frequencies[low2]
        frequencies[(low1, low2)] = freq1 + freq2
    return list(frequencies.keys())[0]

"""returns key w smallest freq"""
def minfrequency(dict):
    min = 2
    minKey = ''
    for key in dict:
        if dict[key] < min:
            min = dict[key]
            minKey = key
    return minKey

"""build prefix code from tree"""
def buildPrefix(tree, dict = {}, carry =''): #carry starts w nothing
    left, right = tree
    if type(left) != tuple: #it's a leaf
        dict[left] = carry + '0'
    else: 
        buildPrefix(left, dict, carry + '0')
    if type(right) != tuple:
        dict[right] = carry + '1'
    else:
        buildPrefix(right, dict, carry + '1')
    return dict

"""encodes contents of file into prefix code and returns encoded string"""
def encodeText(prefixDict, chars):
    finStr = '' #final string to return
    for i in range(len(chars)):
        finStr += prefixDict[chars[i]]
    return finStr

"""packs encoded string into chunks of 8 bits"""
def packCode(prefixStr):
    chunkList = []  

    """make sure prefixStr is a multiple of 8
    if not, pack w zeros (we stop decoding at # of original chars)"""
    remainder = len(prefixStr)%8
    if remainder != 0:
        prefixStr += '0'*(8-remainder)

    for i in range(0, len(prefixStr), 8):
        chunkList.append(prefixStr[:8]) #add to list first 8 bits
        prefixStr = prefixStr[8:] #cut out first 8 bits from prefixStr

    return chunkList

"""saves file test.txt.HUFFMAN"""
def saveFile_Huffman(chunkList, fileName):
    numList = list(map(lambda x: binary.BinaryToNum(x), chunkList))
    encList = list(map(lambda x: chr(x), numList)) #binary in char form

    f1 = open(fileName, 'w')
    for word in encList:
        f1.write(word)
    f1.close()
    return 

"""saves file test.txt.HUFFMAN.KEY"""
def saveFile_Huffman_Key(prefixDict, chars, chunkList, fileName):
    numDistChars = len(prefixDict) # num of distinct chars in file
    inputBytes = len(chars)
    compBytes = len(chunkList)
    aRatio = compBytes/inputBytes

    #print these stats to user
    print("\tDistinct characters: " + str(numDistChars))
    print("\tTotal bytes: " + str(inputBytes))
    print("\tCompressed text length in bytes: " + str(compBytes))
    print("\tAsymptotic compression ratio: " + str(aRatio))

    f1 = open(fileName, 'w')
    f1.write(str(numDistChars)+"\n")
    f1.write(str(compBytes*8)+"\n")
    for key in prefixDict:
        f1.write(key + prefixDict[key]+"\n")
    return

def main():
    inputFileName = input("Enter a file to compress: ")
    print("Original file: " + inputFileName) 

    huffFile = inputFileName + ".HUFFMAN"
    keyFile = inputFileName + ".HUFFMAN.KEY"

    """run all the functions"""
    tempList = freq(inputFileName) #reads file, dict w freq of ea char
    freqDict = tempList[0]
    inputChars = tempList[1]
    huffmanTree = build_huffman_tree(freqDict)
    prefixDict = buildPrefix(huffmanTree) #bin prefix code for ea char
    encodedList = encodeText(prefixDict, inputChars)
    chunkList = packCode(encodedList) #pack bin into 8 bit chunks
    saveFile_Huffman(chunkList, huffFile)
    saveFile_Huffman_Key(prefixDict, inputChars, chunkList, keyFile)

    return 
