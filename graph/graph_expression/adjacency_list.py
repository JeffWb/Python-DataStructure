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
		
	def add_node(self,index,elem):
		"""
		add node
		"""
		self.name_list.insert(index,elem)
		self.node_list.insert(index,Node(elem))
		
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
		
	def get_weight(self,val1,val2):
		"""
		get weight between node(val1) and node(val2)
		"""
		index_val1 = name_list.index(val1)
		temp = node_list[index_val1]
		while temp.val != val2:
			temp = temp.next
		return temp.weight
	
	def get_TD(self,v1):
		"""
		get TD of v1
		"""
		index_v1 = name_list(v1)
		temp = node_list[index_v1]
		i = 0
		while temp.next != None:
			temp = temp.next
			i += 1
		return i
	
	def get_edge_num(self):
		"""
		get total edge nums
		"""
		total_nums = 0
		for i in name_list:
			total_nums += get_TD(i)
		return total_nums//2
	
	def each_list(self):
		total_list = []
		for i in node_list:
			per_list = []
			temp = i
			while temp != None:
				per_list.append(temp.val)
				temp = temp.next
			total_list += per_list
		return total_list
	
if __name__ == '__main__':
	print(">>>>>>>>>>>>>>>初始化一个图<<<<<<<<<<<<<")
	name_list = ["a","b","d"]
	graph = Graph(name_list)
	print("初始化图的结点数为：",graph.node_num())
	print("初始化图的邻接表为：",graph.each_list())
	print(">>>>>>>>>>>>>>>添加三条边，权值分别5,4,3<<<<<<<<<<<<<<<<<<<<")
	graph.add_edge("a","b",5)
	graph.add_edge("b","d",4)
	graph.add_edge("d","a",3)
	print("添加边后结点数目为：",graph.node_num())
	print("b和d两个结点之间的权值为：",graph.get_weight("b","d"))
	print("结点a的度为：",graph.get_TD("a"))
	print("图的总边数为：",graph.get_edge_num())
	print("添加边后的邻接表为：",graph.each_list())
	print(">>>>>>>>>>>>>>>>添加结点c在第三个位置处<<<<<<<<<<<<<<<<<<<<<")
	graph.add_node(3,"c")
	print("添加结点后a和b的权值",graph.get_weight("a","b"))
	print("添加结点后的总结点数",graph.node_num())
	print("添加结点后的a度数",graph.get_TD("a"))
	print("添加结点后的总边数",graph.get_edge_num())
	print("添加结点后的邻接表",graph.each_list())
	print(">>>>>>>>>>>>>>>>>>>>>添加结点c后，再添加边<<<<<<<<<<<<<<<<<<<<<<<<")
	graph.add_edge("a","c",1)
	print("添加结点后在添加边后a和c的权值",graph.get_weight("a","c"))
	print("添加结点后在添加边后的总结点数",graph.node_num())
	print("添加结点后在添加边后的a度数",graph.get_TD("a"))
	print("添加结点后在添加边后的总边数",graph.get_edge_num())
	print("添加结点后在添加边后的邻接表",graph.each_list())
	
	
	
	
		
					
