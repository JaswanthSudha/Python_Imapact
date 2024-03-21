class Graph:
    def __init__(self):
        self.list=dict()
    def append_vertex(self,vertex):
        self.list[vertex]=[]
    def add_edges(self,v1,v2):
        if v2 not in self.list[v1]:
            self.list[v1].append(v2)
        if v1 not in self.list[v2]:
               self.list[v2].append(v1)
    def remove_edge(self,start,end):
         for value in self.list[start]:
              if value ==end:
                   self.list[start].remove(end)
         for value in self.list[end]:
            if value ==start:
              self.list[end].remove(start)
        #  list1=self.list[start]
        #  if end in list1:
        #       list1.remove(end)
        #       self.list[start]=list1
        #  list2=self.list[end]
        #  if start in list2:
        #       list2.remove(start)
        #       self.list[end]=list2
    def remove_vertex(self,vertex):
         self.list.pop(vertex,None)
         for key in self.list.keys():
              if vertex in self.list[key]:
                   list2=self.list[key]
                   list2.remove(vertex)
                   self.list[key]=list2      
g1=Graph()
g1.append_vertex("A")
g1.append_vertex("B")
g1.append_vertex("C")
g1.append_vertex("D")
g1.append_vertex("E")
g1.append_vertex("F")
g1.append_vertex("G")
g1.append_vertex("H")
g1.add_edges("A","B")
g1.add_edges("A","C")
g1.add_edges("B","D")
g1.add_edges("B","E")
# g1.add_edges("D","F")
g1.add_edges("F","E")
g1.add_edges("E","G")
# g1.add_edges("C","G")
g1.add_edges("G","H")



