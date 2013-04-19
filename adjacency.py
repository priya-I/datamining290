import networkx as nx
import numpy as np
DG=nx.DiGraph()

DG.add_nodes_from([2,3,5,7,8,9,10,11])

DG.add_edges_from([(5,11),(3,8),(3,10),(8,9),(7,8),(7,11),(11,2),(11,9),(11,10)])

nx.write_adjlist(DG,"list")
result=nx.adjacency_matrix(DG)
print "***Adjacency List for Graph 1***"
for line in nx.generate_adjlist(DG)
	print line

print "\n***Adjacency Matrix for Graph 1***"
print result

G=nx.Graph()
G.add_nodes_from([1,2,3,4,5,6])
G.add_edges_from([(1,2),(2,1),(1,5),(5,1),(2,3),(3,2),(2,5),(5,2),(3,4),(4,3),(4,5),(5,4),(4,6),(6,4)])

print "***Adjacency List for Graph 2***"
for line in nx.generate_adjlist(G):
	print line

print "\n***Adjacency Matrix for Graph 2***"
result2=nx.adjacency_matrix(G)
print result2
