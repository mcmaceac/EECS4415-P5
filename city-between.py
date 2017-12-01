import matplotlib.pyplot as plot
import networkx as nx
import sys
import re

G = nx.Graph()
positions = {} # a position map of the nodes (cities)

inFile = sys.stdin
for line in inFile:
	elmts = [x.strip() for x in line.split(',')]
	nodeName = elmts[0] + ',' + elmts[1]
	#print(nodeName)

	indentedLines = int(elmts[4])
	G.add_node(nodeName, pos=(float(elmts[2]), float(elmts[3])))
	while indentedLines > 0:
		nextLine = next(inFile)
		indentedLines -= 1
		connectElements = [x.strip() for x in nextLine.split(',')]
		#print(connectElements)
		otherNodeName = connectElements[0] + ',' + connectElements[1]
		G.add_edge(nodeName, otherNodeName)
	#if indentedLines > 0:

	#else:

positions = nx.get_node_attributes(G, 'pos')
# plot the city graph
plot.figure(figsize=(8,8))
nx.draw(G,
        positions,
        node_size   = [4 for v in G],
        with_labels = False)

#plot.savefig('city-plot.png')
plot.show()