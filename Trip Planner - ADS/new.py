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

'''print("\n\nIndex Array: ")
for i in range(0,len(index_arr)):
    if (index_arr[i]!=None):
        print(index_arr[i], end = " ")
'''

class PriorityQueueNode:
    
 def __init__(self, value, pr):
    
    self.data = value
    self.priority = pr
    self.next = None
        
# Implementation of Priority Queue
class PriorityQueue:
    
    def __init__(self):
        
        self.front = None
 
    def isEmpty(self):
        
        return True if self.front == None else False
    
    def push(self, value, priority):
        
        if self.isEmpty() == True:
            
            self.front = PriorityQueueNode(value,
                                        priority)
            
            return 1
            
        else:
            if self.front.priority > priority:
                
                newNode = PriorityQueueNode(value,
                                            priority)
                
                newNode.next = self.front
                self.front = newNode
                return 1
                
            else:
                temp = self.front
                
                while temp.next:
                    
                    if priority <= temp.next.priority:
                        break
                    
                    temp = temp.next
                
                newNode = PriorityQueueNode(value,
                                            priority)
                newNode.next = temp.next
                temp.next = newNode
      
                return 1
    
    def pop(self):
        
  
        if self.isEmpty() == True:
            return
        
        else:
            
 
            self.front = self.front.next
            return 1
            
 
    def peek(self):
   
        if self.isEmpty() == True:
            return
        else:
            return self.front.data

    def traverse(self):
        
  
        if self.isEmpty() == True:
            return "Queue is Empty!"
        else:
            temp = self.front
            while temp:
                print(temp.data, end = "\n")
                temp = temp.next



# Driver code

    print("The optimised solution without weights: ")
    
    pq = PriorityQueue()
    p1 = [3,6,7,8,4,5,2,1,10,9] # solo trip
    p2 = [1,2,5,6,3,7,9,4,7,0]  # 2 people 
    p3 = [9,8,8,7,6,5,3,4,5,1] 	# fam 

    

def func_p1():
    for x in range(0,len(index_arr)):
        if (index_arr[x]!=None):
            y=index_arr[x]
            pq.push(hash_table[y], p1[x])
        #print(x)
   
    pq.traverse()
   
    pq.pop()

def fun_p2():
    for x in range(0,len(index_arr)):
        if (index_arr[x]!=None):
            y=index_arr[x]
            pq.push(hash_table[y], p2[x])
        #print(x)
   
    pq.traverse()
   
    pq.pop()

def fun_p3():
    for x in range(0,len(index_arr)):
        if (index_arr[x]!=None):
            y=index_arr[x]
            pq.push(hash_table[y], p3[x])
        #print(x)
   
    pq.traverse()
   
    pq.pop()

        
def menu():
    print("TRIP PLANNER ")
    number = int(input("Enter number of people"))
    if(number == 1) :
        func_p1()
    elif (number == 2):
        func_p2()
    else:
        func_p3()

    print("List of factors which will afect your trip:\n1.Distance\n2.Budget\n3.Familiy friendly ")