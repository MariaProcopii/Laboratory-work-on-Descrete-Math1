''''2 XNOR'''

def xnor(a, b):
    g = ((a or (not b)) and (not (a) or b))
    print(g)

xnor(1, 1)