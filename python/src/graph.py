"""
Graph module that provides weighted edge, directed and undirected graph data structures
"""


class Edge:
    """
    Weighted directed edge
    """

    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Graph:
    """
    Weighted directed graph
    """

    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, start, end, weight):
        """
        Add edge with specified weight connecting start and end nodes
        """
        self.add_vertex(start)
        self.add_vertex(end)
        self.adjacency_list[start].append(Edge(start, end, weight))

    def add_vertex(self, vertex):
        """
        Add vertex
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def get_adjacency_list(self):
        """
        Get graph as adjacency list
        """
        return self.adjacency_list

    def get_edges(self, vertex=None):
        """
        Get all edges of the graph
        """
        if vertex is None:
            return [edge for edges in self.adjacency_list.values() for edge in edges]
        return self.adjacency_list[vertex]

    def get_vertices(self):
        """
        Get all vertices of the graph
        """
        return self.adjacency_list.keys()


class UndirectedGraph:
    """
    Weighted undirected graph
    """

    def __init__(self):
        self.graph = Graph()

    def add_edge(self, start, end, weight):
        """
        Add edge with specified weight connecting start and end nodes
        """
        self.graph.add_edge(start, end, weight)
        self.graph.add_edge(end, start, weight)

    def add_vertex(self, vertex):
        """
        Add vertex
        """
        self.graph.add_vertex(vertex)

    def get_adjacency_list(self):
        """
        Get graph as adjacency list
        """
        return self.graph.get_adjacency_list()

    def get_edges(self, vertex=None):
        """
        Get all edges of the graph
        """
        return self.graph.get_edges(vertex)

    def get_vertices(self):
        """
        Get all vertices of the graph
        """
        return self.graph.get_vertices()
