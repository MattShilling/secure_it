# DATA ENCODE AND DECODE   #
# Written by Matt Shilling #

import sys, getopt


def encode(file):
    line_buffer = ""
    result = ""
    f = open(file, 'r')
    for line in f:
        line_buffer = line[::-1]
        for char in line_buffer:
            #print(char)
            result+=chr(ord(char) - 10)
            
    f.close()
    f = open("encoded.txt", 'w')
    f.write(result)
    print("Encoded file @ encoded.txt")


def decode(file):
    result = ''
    f = open(file, 'r')
    for line in f:
        line_buffer = line[::-1]
        for char in line_buffer:
            result += (chr(ord(char) + 10))
    print (result)

def main(argv):
    file = ''
    try:
        opts, args = getopt.getopt(argv,"e:d:")
    except getopt.GetoptError:
        print ('security.py -d <file to decode>')
        print ('security.py -e <file to encode>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-d"):
            print("decoding...")
            file = arg
            decode(file)
        elif opt in ("-e"):
            print("encoding...")
            file = arg
            print ('the file is: ')
            print (file)
            encode(file)
         
   

if __name__ == "__main__":
   main(sys.argv[1:])
