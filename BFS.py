from collections import defaultdict
import numpy as np

def enqueue(queue, s):
	queue.append(s)
	return queue

def dequeue(queue, s):
	queue.pop(s)
	return queue

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	
	def appendedge(self, u, v):
		self.graph[u].append(v)
	
	def BFS(self, start_node):
		encountered = np.zeros(len(self.graph))
		
 
		queue = []
		queue = enqueue(queue, start_node)
		encountered[start_node] = 1
		
		while queue:
			start_node = queue.pop(0)
			print start_node
			for i in self.graph[start_node]:
				if encountered[i] == 0:
				    queue.append(i)
				    encountered[i] = 1

if __name__ == "__main__":
	g = Graph()
	g.appendedge(0, 1)
	g.appendedge(0, 2)
	g.appendedge(1, 2)
	g.appendedge(2, 0)
	g.appendedge(2, 3)
	g.appendedge(3, 3)
	g.appendedge(3, 4)
	g.appendedge(4, 5)
	g.appendedge(5, 1)
	print "BFS traversal with 2 as starting node"
	g.BFS(2)
 
			

	
		
