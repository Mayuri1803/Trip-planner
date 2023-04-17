
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

	printArray(table, L)


# Driver code
arr=["Marina-Beach","VGP-Snow-Kingdom","Mahabalipuram","EA-Mall"]
#arr = [ "Marina-Beach","VGP-Snow-Kingdom","Mahabalipuram","EA-Mall","Santhome-Church",
	#"Pondy_Bazar","Kabali_Temple","Senmozhi_Poonga", "Vandaloor_Zoo","Muttukadu-Boat-House"]
N = 4

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

print("\n\nIndex Array: ")
for i in range(0,len(index_arr)):
	if (index_arr[i]!=None):
		print(index_arr[i], end = " ")
#print(index_arr)

# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations
V = N

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):

	# store all vertex apart from source vertex
	vertex = []
	for i in range(V):
		if i != s:
			vertex.append(i)

	# store minimum weight Hamiltonian Cycle
	min_path = maxsize
	next_permutation=permutations(vertex)

	for i in next_permutation:
		#print(next_permutation)

		# store current Path weight(cost)
		current_pathweight = 0

		# compute current path weight
		k = s
		for j in i:
			current_pathweight += graph[k][j]
			#print(i)
			k = j
		current_pathweight += graph[k][s]

		# update minimum
		min_path = min(min_path, current_pathweight)
		perm_arr.append(i)
		min_vals.append(min_path)

	#print(min_vals)
	#print(perm_arr)
	x=0
	for a in range(0,len(min_vals)):
		if min_vals[a]==min_path:
			x=a
			break

	#printing the path
	'''print("\n\n",s,end=" ")
	for y in range(0,V-1):
		print(" -> ",perm_arr[x][y],end=" ")
	print(" ->",s,end=" ")'''
	
	#storing the path in an array
	path_arr=[0]*5
	path_arr[0]=0
	for i in range(0,V-1):
		path_arr[i+1]=perm_arr[x][i]
		#print("\n\n",perm_arr[x][i])
	print(path_arr)
	return min_path


# matrix representation of graph
graph = [[0, 10, 15, 20], [10, 0, 35, 25],
		[15, 35, 0, 30], [20, 25, 30, 0]]
z=index_arr[0]        
s = 0
min_vals=[]
perm_arr=[]
travellingSalesmanProblem(graph, s)


