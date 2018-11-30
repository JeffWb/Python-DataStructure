"""
_*_ coding: uft-8 _*_
@auther: JeffWb
@date:20018.11.30
@version: py3.6.7

graph expression of adjacencey matrix
"""

class Node:
	def __init__(self,value,next_ = None):
		self.value = value
		self.next = next_

class graph:
	def __init__(self,node_list = None):
		"""
		adjacency matrix initailize
		"""
		self.node_list = node_list
		mat = []
		for i in range(len(self.node_list)):
			mat.append([0] * len(self.node_list))
		self.adj_matrix = mat
		
	def adjmatrix(self):
		"""
		adjacency matrix
		"""
		return self.adj_matrix
		
	def node_num(self):
		"""
		node num of graph
		"""
		return len(self.node_list)
		
	def add_node(self,index,val):
		"""
		add node at index,node.value = val
		"""
		node = Node(val)
		self.node_list.insert(index,node)
		for i in self.adj_matrix:
			i.insert(index,0)
		self.adj_matrix.insert(index,[0]*len(node_list))
		
	def add_edge(self,v1,v2,weight):
		"""
		add edge with weight between v1 and v2
		"""
		def index(val):
			for i in range(self.node_list):
				if node_list[i].value = val
				break
			return i
		v1_index = index(v1)
		v2_index = index(v2)
		self.adj_matrix[v1_index][v2_index] = weight
		self.adj_matrix[v1_index][v2_index] = weight
