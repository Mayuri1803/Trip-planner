
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

print("\n\nIndex Array: ")
for i in range(0,len(index_arr)):
	if (index_arr[i]!=None):
		print(index_arr[i], end = " ")
#print(index_arr)
