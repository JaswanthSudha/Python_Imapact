class Graph:
    def __init__(self):
        self.matrix=[]
        self.vertices=[]
    def add_vertex(self,vertex):
        self.vertices.append(vertex)
        rows=[]
        for _ in range(len(self.vertices)-1):
            rows.append(0)
        self.matrix.append(rows)
        for each_row in self.matrix:
            each_row.append(0)
    def add_edge(self,start,end):
        start_index=self.vertices.index(start)
        end_index=self.vertices.index(end)
        self.matrix[start_index][end_index]=1
        self.matrix[end_index][start_index]=1    
    def remove_vertex(self,vertex):
        vertex_index=self.vertices.index(vertex)
        self.vertices.remove(vertex)
        self.matrix.pop(vertex_index)
        for each_row in self.matrix:
            each_row.pop(vertex_index) 
    def remove_edge(self,start,end):
        start_index=self.vertices.index(start)
        end_index=self.vertices.index(end)
        self.matrix[start_index][end_index]=0
        self.matrix[end_index][start_index]=0 
g1=Graph()
g1.add_vertex('A')
g1.add_vertex('B')
g1.add_vertex("C")
g1.add_vertex("D")
g1.add_edge("A","B")
g1.add_edge("B","D")
g1.add_edge("B","C")
g1.add_edge("D","C")
print(g1.vertices)
print(g1.matrix)
g1.remove_vertex("C")
print(g1.matrix)
