# Trip-planner
One of the main difficulties faced by many people is planning a proper trip. To solve this issue, the 
proposed project is a trip planner which gives people the optimised travel plan. 
The input data given by the users are the following:
- Number of passengers
- Date of Journey
- Origin location
- Destination location
- 
From the given input data, I formulate the most efficient itinerary, which includes most important 
places to visit keeping in mind the constraints like time availability, date of journey, number of 
people. To implement this project, the following data structures are be used.

1. Graphs: 
Graph is a non-linear data structure consisting of nodes and edges. Here in this case, I use graphs 
to compute the shortest path between two locations. The optimum plan with what places to visit will 
be suggested (taking into account shortest distance between places) , however if the user wants to 
change the places to visit, the most efficient path will be suggested to the user. The algorithm for 
computing the distance uses graphs as we calculate the value for each path using weighted graphs.

2. Hash Table:
The list of places to visit will be stored in a hash table. The hash table keys will hence be stored in a 
priority queue. This is done as each place will have its corresponding key value, and hence easier to 
objectively choose the more important place to visit.

3. Priority Queue:
Priority queue is used to store all the nodes in the graph along with their distance to the starting 
node. And hence we get the node with the minimum distance as until the priority queue is not empty 
we extract the node with the current shortest known distance to our starting node.
Another usage of the priority queue will be storing the hash keys in priority queue. These hash keys 
correspond to different places, and hence giving the hash key as priority queue elements, each hash 
key will have a priority value. This priority value will help to find out the higher priority place to 
visit.

Hence, this project will act as a solution to a wide range of audience, ranging from school or college 
students to elderly people. This application implements various data structures to effectively store 
data and use the same and computes an efficient itinerary. 
