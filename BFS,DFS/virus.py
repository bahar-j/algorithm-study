from sys import stdin

num_cpt = int(input())

num_line = int(input())

graph = [[0]*num_cpt for i in range(num_cpt)]

visited = []

for i in range (num_line):
    cpt1, cpt2 = map(int, stdin.readline().split())
    graph[cpt1-1][cpt2-1] = 1
    graph[cpt2-1][cpt1-1] = 1

def DFS(v):
    visited.append(v)
    for i in range (num_cpt):
        if ( graph[v][i] == 1 ):
            if( i not in visited ):
                DFS(i)

DFS(0)
print(len(visited)-1)
