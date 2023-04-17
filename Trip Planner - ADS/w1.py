import random
# Add a vertex to the set of vertices and the graph
def add_vertex(v):
  global graph
  global vertices_no
  global vertices
  if v in vertices:
    print("Vertex ", v, " already exists")
  else:
    vertices_no = vertices_no + 1
    vertices.append(v)
    if vertices_no > 1:
        for vertex in graph:
            vertex.append(0)
    temp = []
    for i in range(vertices_no):
        temp.append(0)
    graph.append(temp)

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices
    # Check if vertex v1 is a valid vertex
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
    # Check if vertex v1 is a valid vertex
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

# Print the graph
def print_graph():
  global graph
  global vertices_no
  for i in range(vertices_no):
    for j in range(vertices_no):
      if graph[i][j] != 0:
        print(vertices[i], " -> ", vertices[j], \
        " edge weight: ", graph[i][j])

# Driver code        
# stores the vertices in the graph
def final():
    vertices = []
    # stores the number of vertices in the graph
    vertices_no = 0
    graph = []
    # Add vertices to the graph
    add_vertex(1)
    add_vertex(2)
    add_vertex(3)
    add_vertex(4)
    add_vertex(5)
    add_vertex(6)
    add_vertex(7)
    add_vertex(8)
    add_vertex(9)
    add_vertex(10)
    # Add the edges between the vertices by specifying
    # the from and to vertex along with the edge weights.
    k = [3,7,9,4,3,2,3,4,5,6,7,11,34,66,89,34,55,10,9,2,34,6,2,95,38,24,20]
    for i in range(11): 
        for j in range(11):
            
            add_edge(i,j,random.choice(k))


    print_graph()
    return graph
    #print("Internal representation: ", graph)
