from linkedlist import LinkedList

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.array_adj = [] # to hold edges

        for i in range(vertices):
            self.array_adj.append(LinkedList())

    def add_edge(self, source, destination):
        if source<self.vertices and destination<self.vertices:
            self.array_adj[source].insert_at_head(destination)
            #self.arr_adj[destination].insert_at_head(source) # for undirected graph

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array_adj[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next
            print("None")

