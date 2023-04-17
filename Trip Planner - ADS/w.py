# Function to print an array
def printArray(arr, n):
	
	#printing the hashtable(Array)
	for i in range(n):
		print(arr[i], end = " ")
	
# quadratic probing
def hashing(table, tsize, arr, N):
	
	for i in range(N):
		
		hv = len(arr[i]) % tsize

		if (table[hv] == -1):
			table[hv] = arr[i]
			
		else:
			
			for j in range(tsize):
				
				t = (hv + j * j) % tsize
				
				if (table[t] == -1):
					
					table[t] = arr[i]
					break

	 #   printArray(table, L)

arr = [ "Marina-Beach","VGP-Snow-Kingdom","Mahabalipuram","EA-Mall","Santhome-Church",
	"Pondy_Bazar","Kabali_Temple","Senmozhi_Poonga", "Vandaloor_Zoo","Muttukadu-Boat-House"]

N = 10

# Size of the hash table
L = 2*N

hash_table = [0] * L

# Initializing the hash table
for i in range(L):
	hash_table[i] = -1
	
hashing(hash_table, L, arr, N)

index_arr=[None]*L
j=0
for i in range(0,L):
	if (hash_table[i]!=-1):
		index_arr[j]=i
		j+=1

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
vertices = []
# stores the number of vertices in the graph
vertices_no = 0
graph = []
# Add vertices to the graph
sample= [1,2,3,4,5]
for i in range(sample):
  x = sample[i]
  add_vertex(x)
  

# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
for i in  range (10):
  for j in range(10):
      add_edge(i,8,2)
'''
add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)
print_graph()
'''
print("Internal representation: ", graph)

