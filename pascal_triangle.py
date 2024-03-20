#!/usr/bin/python3

import sys

def Pas(line, pos):
    if pos == 0 or pos == line:
        return 1
    else:
        return Pas(line-1, pos-1) + Pas(line-1, pos)

def get_triangle(toline):
    # init string variable
    triangle = ""
    for i in range(0, toline + 1):
        # calculate spaces between ":" and line
        spaces = " " + " " * (len(str(toline))-len(str(i)))
        # get current line
        line = str(i) + ":" + spaces
        for i2 in range(0, i + 1):
            line += str(Pas(i, i2)) + "|"
        # add line to string
        triangle += line[:-1] + "\n"
    return triangle[:-1]

def main(args):
    # only proceed if first arg is an integer
    # otherwise print usage information
    if len(args) > 1 and args[1].isdigit():
        print(get_triangle(int(args[1])))
    else:
        print("Usage:\npas_dreieck.py <integer number>\n number: to which line it should calculate")
        exit(1)

main(sys.argv)