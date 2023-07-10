#!/usr/bin/env python

import argparse
from helpers import getter
from helpers import parsers
from helpers.parsers import Node
import sys

# defining joint chars
char_pipe   = "│"
char_middle = "├─"
char_end    = "└─"

def show(N:Node, pretab = ''):
    nchildren = len(N.children)

    for i,ci in enumerate(N.children):
        # adding joints and pipes
        tab_ = f'{pretab}  '

        flag_last = False
        if i < nchildren - 1:
            tab_ = f'{tab_}{char_middle}'
        else:
            flag_last = True
            tab_ = f'{tab_}{char_end}'
            
        # writing message
        msg = f'{tab_}{ci.value}'
        print(msg)

        # if there is no children, continue
        if not N.hasChildren:
            continue
        
        if flag_last:
            nexttab = f'{pretab}  '
        else:
            nexttab = f'{pretab}  {char_pipe}'
        show(N.getChild(ci.value), nexttab)

def main(params = None):
    
    if not params:
        params = sys.stdin.read().split('\n') 
    
    tree = parsers.Buffer2Tree(params)
    print(' ')
    show(tree)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Shows the output of the git `compare` as a tree')
    parser.add_argument('--test', action="store_true")
    parser.add_argument('-f', '--file', type=str, help="read from 'file' with git output")

    args = parser.parse_args()
    
    if args.test:
        main(getter.DummyDataFromFile('ref.txt'))
    elif args.file:
        main(getter.DummyDataFromFile(args.file))
    else:
        main()