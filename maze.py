# This program creates a maze by backtracking
from itertools import product, repeat, islice, tee, chain
import random

random.seed(100)

# Generate the pairings
NC = 12
NR = 12
N = NC * NR

def groups(it, n):
    return zip(*([iter(it)] * n))

def pairwise(k):
    a, b = tee(k)
    next(b)
    return zip(a, b)

indexes = list(groups(range(N), NC))
row_edges = chain(*map(pairwise, indexes))
col_edges = chain(*map(pairwise, zip(*indexes)))
edges = list(chain(row_edges, col_edges))

nodes = [[] for i in range(N)]

for a, b in edges:
    nodes[b].append(a)
    nodes[a].append(b)


connectivity = list(map(list, nodes))

#lolnodes = list(list(i) for i in nodes)
stack = []
to_visit = N - 1
visited = [False] * N
current = random.randrange(N)

while to_visit:
    node = nodes[current]
    neighbours = [n for n in node if not visited[n]]

    if not visited[current]:
        visited[current] = True
        to_visit -= 1

    if neighbours:
        n = random.choice(neighbours)
        nodes[n].remove(current)
        node.remove(n)
        stack.append(current)
        current = n
    elif stack:
        current = stack.pop()

#print(nodes)
#barrier = '+' + '=' * (3 * NC - 1) + '+'
#print(barrier)
#for line in indexes:
#    ks = ['|']
#    for i in line:
#        n = nodes[i]
#        down_wall = (i + NC) in n
#        right_wall = (i + 1) in n
#        norm = down_wall and '_' or ' '
#        ks.append(norm * 2 + (right_wall and '|' or norm))
#    ks.append(ks.pop()[:-1])
#    ks.append('|')
#    print("".join(ks))
#
#    #print('|' + wall_string + '|')
##    [(i+NC) in edges[i] else  for i in line]:
#print(barrier)

import turtle

t = turtle.Turtle()

points = list(product(range(NC), range(NR)))

t.speed(0)

#turtle.tracer(10, 25)
#
#t.pensize(3)
#t.penup()
#t.goto(0, 0)
#t.pendown()
#t.goto(20 * NC, 0)
#t.goto(20 * NC, 20 * NR)
#t.goto(0, 20 * NR)
#t.goto(0, 0)
#for i, ns in enumerate(nodes):
#    y1, x1 = points[i]
#    for n in (n for n in ns if n > i):
#        y2, x2 = points[n]
#        t.penup()
#        if n == i + 1:
#            t.goto(20 * x2, 20 * y1)
#            t.pendown()
#            t.goto(20 * x2, 20 * (y1 + 1))
#        else:
#            t.goto(20 * x1, 20 * y2)
#            t.pendown()
#            t.goto(20 * (x1 + 1), 20 * y2)

start = random.randrange(N)
end = random.randrange(N)
y1, x1 = points[start]
y2, x2 = points[end]

t.penup()
t.goto(10 + 20 * x1, 10 + 20 * y1)
t.dot()
t.goto(10 + 20 * x2, 10 + 20 * y2)
t.dot()
t.penup()
t.goto(10 + 20 * x1, 10 + 20 * y1)
t.pencolor(1, 0, 0)

turtle.tracer(1)
t.speed(3)
t.pendown()
t.pensize(1)

current, d = start, 0
t.seth(0)

DIRS = [+1, -NC, -1, +NC]
print(nodes[current])

def rt():
    global d
    t.rt(90) 
    d = (d + 1) % 4
def lt():
    global d
    t.lt(90)
    d = (d - 1) % 4

def check():
    nxt = (current + DIRS[d])
    return nxt in connectivity[current] and nxt not in nodes[current]

def fd():
    # Check if we can go forwards
    global current
    nxt = (current + DIRS[d])
    if nxt in connectivity[current] and nxt not in nodes[current]:
        current = nxt
        t.fd(20)

def c4():
    lt()
    l = check()
    rt()
    f = check()
    rt()
    r = check()
    lt()
    return l, f, r

def fc():
    fd()
    return c4()
