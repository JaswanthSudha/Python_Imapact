from Queue import queue
from dictionary import g1
def bfs(q,vertex,visited):
    q.enqueue(vertex)
    while not q.isEmpty():
        element=q.dequeue()
        if element not in visited:
            visited.append(element)
        for value in g1.list[element]:
            if value not in visited:
                q.enqueue(value)
q=queue()
visited=[]
bfs(q,"A",visited)
print(visited)






