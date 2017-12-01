import matplotlib.pyplot as plot
import networkx as nx
import sys
import re

G = nx.Graph()
positions = {} # a position map of the nodes (cities)

#create the graph from the text file
inFile = sys.stdin
for line in inFile:
	elmts = [x.strip() for x in line.split(',')]
	nodeName = elmts[0] + ',' + elmts[1]
	#print(nodeName)

	indentedLines = int(elmts[4])
	G.add_node(nodeName, pos=(float(elmts[2]), float(elmts[3])))

	#add edges between nodes(indented elements)
	while indentedLines > 0:
		nextLine = next(inFile)
		indentedLines -= 1
		connectElements = [x.strip() for x in nextLine.split(',')]
		#print(connectElements)
		otherNodeName = connectElements[0] + ',' + connectElements[1]
		G.add_edge(nodeName, otherNodeName, weight=int(connectElements[2]))

#print(nx.get_edge_attributes(G, "weight"))
#weights = nx.get_edge_attributes(G, 'weight')

#print(weights)
#for edge in G.edges(data=True):
#	print(edge)

#print(nx.edge_betweenness_centrality(G, weight='weight'))
#for betweenness in sorted(nx.edge_betweenness_centrality(G, weight='weight').items(), key=lambda x: -x[1]):
i = 0
removedEdges = []
while(nx.is_connected(G)):
	betweenness = sorted(nx.edge_betweenness_centrality(G).items(), key=lambda x: -x[1])
	u = betweenness[0][0][0]
	v = betweenness[0][0][1]

	removedEdges.append([u, v, G[u][v]['weight']])
	G.remove_edge(betweenness[0][0][0], betweenness[0][0][1])
	i += 1

print("Edges removed: " + str(i))

i = 0
for edge in removedEdges:
	u = edge[0]
	v = edge[1]
	w = edge[2]
	G.add_edge(u, v, weight=w)
	i += 1
	if (nx.is_connected(G)):
		G.remove_edge(u, v)
		i -= 1

print("Edges added back: " + str(i))

#for betweenness in sorted(nx.edge_betweenness_centrality(G).items(), key=lambda x: -x[1]):
#	print(betweenness)

#print(betweenness)



#print(G.number_of_nodes())
positions = nx.get_node_attributes(G, 'pos')
# plot the city graph
plot.figure(figsize=(8,8))
nx.draw(G,
        positions,
        node_size   = [4 for v in G],
        with_labels = False)

plot.savefig('city-plot.png')
plot.show()