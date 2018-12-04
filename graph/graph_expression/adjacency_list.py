"""
@auther:JeffWb
@date:2018.12.4
@version:py3.6

adjacency list of graph
"""

class Node:
	def __init__(self,val,next_ = None,weight = None):
		self.val = val
		self.next = next_
		self.weight = weight
		
class Graph:
	def __init__(self,name_list = None):
		self.name_list = name_list
		self.node_list = [Node(i) for i in self.name_list]
		
	def node_num(self):
		"""
		return node num
		"""
		return len(node_list)
		
	def add_node(self,elem):
		"""
		add node
		"""
		self.name_list.append(elem)
		self.node_list.append(Node(elem))
		
	def add_edge(self,v1,v2,weight = 1):
		"""
		add edge between v1 and v2, weight default 1
		"""
		node_v1 = node_list[name_list.index(v1)]
		node_v2 = node_list[name_list.index(v2)]
		
		def insert(node1,node2):
			"""
			insert v2 
			"""
			node2.weight = weight
			node1_list = [node2]
			node1_name_list = []
			if node1.next == None:
				node1.next = node2
			else:
				temp = node1.next
				while temp:
					node1_list.append(temp)        #save node
					node1_name_list.append(temp.val)       #save node val
					temp = temp.next
				node1_list.sort(key = lambda node:node.val,reverse = False)
			for i in node1_list:
				node1.next = i
				node1 = node1.next
			node1.next = None
			
		insert(node_v1,node_v2)
		insert(node_v2,node_v1)
		
					
