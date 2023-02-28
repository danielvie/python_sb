#!/usr/bin/env python

import argparse
from helpers import getter
from pathlib import PurePath
import re
import sys

# defining joint chars
char_pipe   = "│"
char_middle = "├─"
char_end    = "└─"

def Buffer2Tree(params):
    patt = r'(?P<type>[A-Z])[\s\t]+' \
           r'(?P<param>\S+)'
    
    P = []
    for param in params:
        match = re.match(patt, param)
        if match:
            value = match.groupdict()
            P.append(f"{value['param']} [{value['type']}]")
        else:
            patt_rename = r'(?P<type>\w+)[\s\t]+' \
                          r'(?P<param1>\S+)[\s\t]+' \
                          r'(?P<param2>\S+)'
            
            match_rename = re.match(patt_rename, param)
            if match_rename:
                value_r = match_rename.groupdict()
                p1 = PurePath(value_r['param1'])
                p2 = PurePath(value_r['param2'])
                p  = p1.parent.joinpath(f'({p1.name} -> {p2.name})')
                
                P.append(f"{p} [{value_r['type'][0]}]")

    tree = {}
    
    for pi in P:
        path = PurePath(pi)
        tree_   = tree
        
        for part in path.parts:
            if part not in tree_:
                tree_[part] = {}

            tree_ = tree_[part]
    
    return tree

def show(N, tab = 0):
    numel_p = len(N)

    for i,ni in enumerate(N):
        nchildren = len(N[ni])
        
        # adding joints and pipes
        tab_ = f'{char_pipe}  '*tab

        if i < numel_p - 1:
            tab_ = f'{tab_}{char_middle}'
        else:
            tab_ = f'{tab_}{char_end}'
            
        # writing message
        msg = f'{tab_}{ni}'
        print(msg)

        # if there is no children, continue
        if nchildren == 0:
            continue
        
        show(N[ni], tab + 1)

def main(params = None):
    
    if not params:
        params = sys.stdin.read().split('\n') 
    
    tree = Buffer2Tree(params)
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