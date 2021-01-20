# https://www.acmicpc.net/problem/1991
from collections import defaultdict
from sys import stdin

def preorder(root):
    global result
    if root == '.':
        return

    result += root
    preorder(G[root][0])
    preorder(G[root][1])

def inorder(root):
    global result
    if root == '.':
        return

    inorder(G[root][0])
    result += root
    inorder(G[root][1])

def postorder(root):
    global result
    if root == '.':
        return

    postorder(G[root][0])
    postorder(G[root][1])
    result += root


LINE = int(input())
G = defaultdict(list)
result = ''

for _ in range(LINE):
    root, left, right = stdin.readline().split()
    tmp = [left, right]
    G[root].extend(tmp)

preorder('A')
print(result)
result = ''

inorder('A')
print(result)
result = ''

postorder('A')
print(result)
result = ''
