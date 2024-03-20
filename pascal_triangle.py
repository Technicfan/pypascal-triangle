#!/usr/bin/python3

import sys

def Pas(line, pos):
    if pos == 0 or pos == line:
        return 1
    else:
        return Pas(line-1, pos-1) + Pas(line-1, pos)

def get_line(iline):
    sline = ""
    for i in range(0,iline+1):
        sline += str(Pas(iline,i)) + "|"
    return sline[:-1]

def main(args):
    if len(args) < 2:
        print("Usage:\npas_dreieck.py <int number>\n number: to which line it should calculate")
        exit(1)
    elif int(args[1]):
        length = len(args[1])
        for i in range(0,int(args[1]) + 1):
            space = " "
            for i2 in range(0,length-len(str(i))):
                space += " "
            print(str(i) + ":" + space + get_line(i))
    else:
        exit(1)

main(sys.argv)