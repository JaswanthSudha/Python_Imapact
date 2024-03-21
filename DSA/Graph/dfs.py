from dictionary import g1
def dfs(key,stack,visited):
    if key not in visited:
        visited.append(key)
        stack.append(key)
        element=stack[-1]
        if g1.list[element]==None:
            stack.pop()
        else:
            for adjancy_element in g1.list[element]:
                dfs(adjancy_element,stack,visited)
visted=[]
stack=[]
dfs("A",stack,visted)
print(visted)
print(stack)

