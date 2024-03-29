# de Bruijn assembly option
import argparse

class Node:
    def __init__(self, data):
        self.data = data
        self.edges = []
    def __str__(self):
        return self.data

class Edge:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
    def __str__(self):
        return str(self.begin) + "->" + str(self.end)

def walkFinder(edgesList):
    BFSarray = []

    for edge in edgesList:
        BFSarray.append((edge, [edge], set([edge]))) #change [edge] to set(edge) - gets error BFSarray.append((edge, set(edge)) TypeError: 'Edge' object is not iterable
    
    #for index, tuple in enumerate(BFSarray):
    #    element_one = tuple[0]
    #    element_two = tuple[1]
    #    element_three = tuple[2]
    #    print(str(element_one), str(element_two[0]), element_one in element_three)

    while len(BFSarray) != 0:
        (edge,visited,visitedSet) = BFSarray.pop(0)
        #find other edges 
        next = edge.end
        if len(visited) == len(edgesList):
            #visited gives me an array of Eulerian walk of edges, can use that to print
            return visited
        for edge in next.edges:
            if edge not in visitedSet:
                visitedCopy = visited
                visitedCopy.append(edge)
                visitedSetCopy = visitedSet
                visitedSetCopy.add(edge)
                BFSarray.append((edge,visitedCopy, visitedSetCopy))
    return None

parser = argparse.ArgumentParser()
parser.add_argument('reads')
args = parser.parse_args()

with open(args.reads) as reads_fh:
  reads = reads_fh.read().splitlines()
  
dictionary = {}
edgesList = []

#graph construction
for read in reads:
    Lmer = read[:-1]
    Rmer = read[1:]

    Lnode = None
    Rnode = None

    if Lmer not in dictionary.keys():
        Lnode = Node(Lmer)
        dictionary[Lmer] = Lnode
    else:
        Lnode = dictionary[Lmer]
    
    if Rmer not in dictionary.keys():
        Rnode = Node(Rmer)
        dictionary[Rmer] = Rnode
    else:
        Rnode = dictionary[Rmer]

    #so far, nodes constructed for each kmer
    edge = Edge(Lnode, Rnode)
    dictionary[Lmer].edges.append(edge)
    edgesList.append(edge)

#need to know when all edges have been visited, figure out if all edges can't be visited once, figure out eulerian walk

# print([str(edge) for edge in edgesList])
path = walkFinder(edgesList)

if path is None:
    print(-1)
else:
    #print([str(edge) for edge in path])
    output = ''
    outputArray = []
    for i,edge in enumerate(path):
        if i == 0:
            outputArray.append(edge.begin.data)
        elif i == len(path) - 1:
            outputArray.append(edge.begin.data[-1])
            outputArray.append(edge.end.data[-1])
        else:
            outputArray.append(edge.begin.data[-1])
    print(output.join(outputArray))



