
def make_graph(filename):
    """Make a graph from the data stored inside the text file
    The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200.
    Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge.
    Input: filename - the name of the text file"""

    try: 
        f = open(filename, 'r')
    except IOError:
        sys.exit("No such file!")
    line_list = f.readlines()

    # populate the graph using data from the text file via dictionary comprehensions
    G = {int(line.split()[0]): {(int(tup.split(',')[0])): int(tup.split(',')[1])
                                for tup in line.split()[1:] if tup} for line in line_list if line}
    f.close()
    return G


def main():
    G = make_graph('dijkstraData.txt') #parse adjacency list text into graph representation G[source][edge] =  distance_between_nodes
    X={}
    source=1	
    X[source]=0 #length to vertex, source=1 , start with the first node
    next_node=source
    greedy_length_least=1000000		
    print 'X before', X
 
# traverse through graph until you reach the last node
# at each node, look for the shortest path to the next node 
# add distance to X
# result is the list of shortest distances between node 1 and all other nodes in the graph X[p]=shortest distance between node 1 and node p       
    while next_node!=[]:
		    			
    	for v in X:#for every node visited 
		
	    for w in G[v]:#check every node connected to v
	        if w not in X: # sift through the remaining nodes of the graph 

	
		   greedy_length=X[v]+G[v][w] #determine the distance to each


			
		   if greedy_length<greedy_length_least:	
		      greedy_length_least=greedy_length
		      next_node=w		# w with least distance is closest to node v
			  
	# Keep moving from node to node until there are no more nodes to see	
	if next_node not in X:		
		X[next_node]=greedy_length_least # add w to the list of visited nodes and store shortest distance
	else:
		next_node=[]

	greedy_length_least=1000000 #reset length before searching for the next closest node

    #test
    lst = [7,37,59,82,99,115,133,165,188,197] # a list of all the desired ending vertices
    #lst = [1,2,3,6] # small data set, a list of all the desired ending vertices
    
    for v in G:
	if v not in X:
	   X[v]=1000000	
	
    			
    for v in lst:
  	print 'Shortest distance between node 1 and node', v, 'is', X[v]
        
if __name__ == '__main__':
    main()
