# DATA ENCODE AND DECODE   #
# Written by Matt Shilling #

import sys, getopt

#encode the file given
def encode(file):
    line_buffer = ""
    result = ""
    f = open(file, 'r')
    for line in f:
        line_buffer = line[::-1] #flip the line backwards
        for char in line_buffer: #go thru each char in the line)
            result+=chr(ord(char) + 10) #adds 10 to the ascii value
            
    #saves the result in encoded.txt
    f.close()
    f = open("encoded.txt", 'w')
    f.write(result)
    f.close()
    print("Encoded file @ encoded.txt\n")
    print("Contents:")
    print(result)
    print("\n")
    print("Decodes to:")
    decode("encoded.txt")

#decode the file given 
def decode(file):
    line_buffer = ''
    result = ''
    f = open(file, 'r')
    for line in f:
        line_buffer = line[::-1] #flip the line back arround
        for char in line_buffer:
            result += (chr(ord(char) - 10)) #subtracts the added value
    print (result) #print out the decoded result

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"e:d:")
    except getopt.GetoptError:
        print ('security.py -d <file to decode>')
        print ('security.py -e <file to encode>')
        sys.exit(2)
    for opt, arg in opts: #arg will be the filename
        if opt in ("-d"):
            print("decoding...")
            decode(arg)
        elif opt in ("-e"):
            print("encoding...")
            encode(arg)

if __name__ == "__main__":
    main(sys.argv[1:])
