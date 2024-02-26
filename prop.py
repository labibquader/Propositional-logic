import pandas as pd
def negation(z):
     n = []
     for x in range(4):
        n.append(not z[x])
     return n

def conjunction(p, q):
    n = []
    for x in range(4):
        n.append(p[x] and q[x])
    return n


def disjuntion(p,q):
    n = []
    for x in range(4):
        n.append(p[x] or q[x])
    return n

def implication(p,q):
    n = []
    for x in range(4):
        if p[x] == False and q[x] == False:
            n.append(True)
        elif p[x] == False and q[x] == True:
            n.append(True)
        elif p[x] == True and q[x] == False:
            n.append(False)
        else:
            n.append(True)
    return n

def biconditional (p,q):
    n = []
    for x in range(4):
        if p[x] == True and q[x] == True:
            n.append(True)
            continue
        if p[x] == False and q[x] == False:
            n.append(True)
            continue
        else:
            n.append(False)
            continue
    return n


p = [False, False, True, True]
q = [False, True, False, True]
y = negation(p)

z = conjunction(p,q)

d = disjuntion(p,q)

i = implication(p,q)

b = biconditional(p,q)


propo_log = zip(p,q,y,z,d,i,b)
df = pd.DataFrame(data = propo_log, columns = ['p', 'q', 'not_p ', 'p_and_q', 'p_or_q', 'p_implies_q', 'p_biconditional_q'])
print()
print (df)

