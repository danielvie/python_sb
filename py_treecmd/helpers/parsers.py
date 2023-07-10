from pathlib import PurePath
import re

class Node:
    def __init__(self, value = '') -> None:
        self.children: list[Node] = []
        self.value: str = value
    
    def hasChildren(self):
        return self.children > 0
    
    def getChild(self, name: str):
        for c in self.children:
            if c.value == name:
                return c

        return None

def Buffer2Tree(params):
    patt = r'(?P<type>[A-Z])[\s\t]+' \
           r'(?P<param>\S+)'
    
    P = []
    flag_tree = True
    for param in params:
        match = re.match(patt, param)
        if match:
            value = match.groupdict()
            P.append(f"{value['param']} [{value['type']}]")
            flag_tree = False
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

    if flag_tree:
        patt = r'\S+'
        for param in params:
            match = re.match(patt, param)
            if match:
                value = match[0]
                P.append(value)
    
    tree = Node('.')
    for pi in P:
        path  = PurePath(pi)
        tree_ = tree
        
        for part in path.parts:
            # is there is no reference, create node
            node = tree_.getChild(part)
            if not node:
                node = Node(part)
                tree_.children.append(node)
                
            # get reference for the node
            tree_ = node

    return tree
