#!/usr/bin/python3

import sys
from tabulate import tabulate

def Pas(line, pos):
    if pos == 0 or pos == line:
        return 1
    else:
        return Pas(line-1, pos-1) + Pas(line-1, pos)

def get_grid(toline):
    grid = []
    for i in range(0,toline + 1):
        grid.append([str(i) + ":"])
        for i2 in range(0,i+1):
            grid[i].append(str(Pas(i,i2)))
    return grid

def get_line(iline):
    sline = ""
    for i in range(0,iline+1):
        sline += str(Pas(iline,i)) + "|"
    return sline[:-1]

def main(args):
    if len(args) == 2:
        args.append("simple")
    elif len(args) < 2:
        print("Usage:\npas_dreieck.py <int number> <mode>\n modes:\n simple: just print it\n grid: print in grid format\n if non given defaulting to \"simple\"")
        exit(1)

    if int(args[1]):
        match args[2]:
            case "grid":
                print(tabulate(get_grid(int(args[1])), tablefmt="grid"))
            case "simple":
                length = len(args[1])
                for i in range(0,int(args[1]) + 1):
                    space = " "
                    for i2 in range(0,length-len(str(i))):
                        space += " "
                    print(str(i) + ":" + space + get_line(i))

main(sys.argv)