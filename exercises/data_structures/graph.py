'''
Graphs:

A graph is a non linear data structure. A graph consists of two pieces

- vertex or node       - edges or links

Nodes are our data, and edges connect more nodes. If a node has an edge to another node, they are known as adjacent.
For example,

        (A)  <- node
        |  \                  In this mini graph, Node (A) is adjacent with Nodes (C) and (B).
        |   \  <-edge         Node (C) is adjacent to Nodes (A) and (B)
        |    \                Same concept applies for Node (B)
edge -> |   (C)  <- node
        |    /
        |   /  <- edge 
        |  /         
        (B)  <- node

The visual above is known as an undirected graph. This means that the edges are pointing in a particular
direction to a node. Think of the edges in an undirected graph as a biconditional,  <--> it flows either
way.


Below is a visual of the same graph in terms of nodes, however now we have a directed graph


        (A)  <---------         In this directed graph we now have edges that are pointing to a specific direction.
         ^           |          Node (B) is adjacent to Node (A), but Node (A) IS NOT ADJACENT TO Node (B).
         |           |          Node (B) is adjacent to both Node (A) and Node (B)
         |           |
         |           |
        (B) ------> (C)


        
Mathematics Representation:

In Math, we represent graphs as a Power Set essentially. We denote a graph as following

G = { V, E }

G - Graph     V - vertex (node)    E - edges (link)      where V and E are sets.

    Let's do the visual for our UNDIRECTED GRAPH ABOVE:

        G = {  { A, B, C }  ,  {  { A , B }  , { A , C, }  , { B, C }  }  }
                    V                               E


    Let's do the visual for our DIRECTED GRAPH ABOVE:

        G = {  { A, B, C }  ,  {  ( B, A )  , ( B , C, )  , ( C, A )  }  }
                    V                                         E

    
    The core difference is in directed graphs our edges are denoted as ordered pairs for our edges, where the x pair 
    is the starting node and the y pair is the ending node. In a undirected graph, we just put adjacent nodes in sets.

    


Coding Representation:

We have two forms to represent graphs in code, 

  -  adjacency matrix       - adjacency list


The adjacency matrix is as following:

    Given the following visual represent w/ an adjacency matrix:

            (A) <---------         
             ^           |
             |           |
             |           |
            (B) ------> (C)


            A  B  C
        A   0  0  0
        B   1  0  1
        C   1  0  0

        We denote a 1 where a node is adjacent to another. In this case Node B connects to Nodes A and C
        and Node C only connects to Node A. In this example Node A never connects to another node so all
        of it's entries are 0's.

        We associate the element in the column first and then read each of it's elements in the row.
        In plain english:

        "Node A does not have a link w/ Node A. Node A does not have a link w/ Node B. Node A does not have a link w/ Node C."
        "Now we drop one in the column to start at B, and we begin reading left to right.."




        The adjacency list is as following:

            Given the following visual represent w/ an adjacency matrix:

            
            (A) <---------         
             ^           |
             |           |
             |           |
            (B) ------> (C)

            
            [
                [A]
                [B, A, C]
                [C, A]
            ]

            For an adjacency list we have a linkedlists within a list.
            The first node of each linked list is the node that is adjacent to the following nodes in the list.
            In this case Node A is first but since it has no links with other nodes it's a singular element.
            Node B has links with A and C thus B is first in that list and it contains those additional nodes after it.

            
Those are the essential concepts of graphs. Now let's get into the coding:

'''

#Class Node, we will use this for both adjacency matrix and list implementations

class Node:
    def __init__(self, data):
        self.data = data
    



#ADJACENCY MATRIX

class Graph_Matrix:
    def __init__(self, size):
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]
        self.nodes = []


    def addNode(self, node):
        if len(self.nodes) < len(self.matrix):
            self.nodes.append(node)
        else:
            print("Error: Node limit reached.")


    def addEdge(self, src, dst):
        if src < 0 or src >= len(self.nodes) or dst < 0 or dst >= len(self.nodes):
            print("Error: Source or destination is out of bounds.")
            return
        self.matrix[src][dst] = 1


    def checkEdge(self, src, dst):
        if src < 0 or src >= len(self.nodes) or dst < 0 or dst >= len(self.nodes):
            return False
        return self.matrix[src][dst] == 1


    def displayMatrix(self):
        # Fetch the labels of nodes
        labels = [node.data for node in self.nodes]
        
        # Print column headers
        print("      ", end="")
        for label in labels:
            print(f"{label:4}", end="")
        print()
        
        # Print rows with row labels
        for i, row in enumerate(self.matrix):
            # Print row header
            print(f"{labels[i]}: ", end="")
            for val in row:
                # Print each column value with spacing for alignment
                print(f"{val:4}", end="")
            print()


# Example usage:
graph = Graph_Matrix(4)
graph.addNode(Node("A"))
graph.addNode(Node("B"))
graph.addNode(Node("C"))
graph.addNode(Node("D"))
graph.addEdge(0, 1)
graph.addEdge(1, 2)
graph.addEdge(2, 3)

graph.displayMatrix()
             
'''
#OUTPUT:

      A   B   C   D   
A:    0   1   0   0
B:    0   0   1   0
C:    0   0   0   1
D:    0   0   0   0

'''

#ADJACENCY LIST


class Graph_List:
    def __init__(self):
        self.entire_list = []


    def addNode(self, node):
        sub_list = [node]
        self.entire_list.append(sub_list)
    

    def addEdge(self, src, dst):
        if src < len(self.entire_list) and dst < len(self.entire_list):
            sub_list = self.entire_list[src]
            dstNode = self.entire_list[dst][0]
            if dstNode not in sub_list:
                sub_list.append(dstNode)
        else:
            print("Error: Source or destination index out of bounds.")
    

    def checkEdge(self, src, dst):
        if src < len(self.entire_list) and dst < len(self.entire_list):
            sub_list = self.entire_list[src]
            dstNode = self.entire_list[dst][0]
            return dstNode in sub_list
        return False
    

    def displayList(self):
        for sub_list in self.entire_list:
            for i, node in enumerate(sub_list):
                if i < len(sub_list) - 1:
                    print(f"{node.data} --> ", end="")
                else:
                    print(node.data, end="")
            print()  # Move to the next line after printing each sublist


# Example usage
graph_list = Graph_List(4)
graph_list.addNode(Node("A"))
graph_list.addNode(Node("B"))
graph_list.addNode(Node("C"))
graph_list.addNode(Node("D"))
graph_list.addEdge(0, 1)
graph_list.addEdge(1, 2)
graph_list.addEdge(2, 1)
graph_list.addEdge(2, 3)


graph_list.displayList()


'''
OUTPUT:

A --> B
B --> C
C --> B --> D
D

'''
    






# Congrats, you just learned about graphs!
 



