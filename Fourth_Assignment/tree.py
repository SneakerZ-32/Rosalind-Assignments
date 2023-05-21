#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:23:30 2023

@author: nicolai
"""
# load the input data
with open("/home/nicolai/Desktop/Homework 4 Rosalind/rosalind_tree.txt", "r") as f:
    # read the number of nodes in the tree
    n = int(f.readline())
    # read the adjacency list
    adjacency_list = [line.strip().split(" ") for line in f]

# initialize lists to store subtrees and nodes
subtrees = []
nodes = set()

# iterate over edges in the adjacency list
for i, j in adjacency_list:
    # if one of the nodes is already in a subtree, add the other node to the same subtree
    if i in nodes or j in nodes:
        for st in subtrees:
            if i in st or j in st:
                subtrees[subtrees.index(st)].append(i)
                subtrees[subtrees.index(st)].append(j)
                nodes.add(i)
                nodes.add(j)
    # if both nodes are new, create a new subtree
    else:
        subtrees.append([i, j])
        nodes.add(i)
        nodes.add(j)

# merge subtrees that have overlapping nodes
l = len(subtrees)
for i in range(l):
    for j in range(l):
        if i == j:
            break
        if len(set(subtrees[i] + subtrees[j])) < len(subtrees[i]) + len(subtrees[j]):
            subtrees[i] = list(set(subtrees[i] + subtrees[j]))
            subtrees[j] = []

# remove empty subtrees
subtrees = [i for i in subtrees if i]

# calculate the number of edges needed to connect all subtrees
result = (n - len(nodes)) + len(subtrees) - 1

# print the result
print(result)
