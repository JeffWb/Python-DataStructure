"""
_*_ coding:utf-8 _*_
@auther: JeffWb
@date: 2018.11.29
@version: py3.6

Huffman tree and Huffman coding
"""

class Node:
	def __init__(self,name = None,value = None,left = None,right = None):
		self.name = name
		self.value = value
		self.left = left
		self.right = right
		
class HuffmanTree:
	def __init__(self,dict):
		"""
		HuffmanTree initialize
		"""
		#generate node list
		node_list = []
		for k,v in dict.items():
			node = Node(name = k,value = v)
			node_list.append(node)
			
		#Huffmancoding use
		self.coding = [0] * len(node_list)
		
		#generate HuffmanTree
		while len(node_list) != 1:
			#sort node list
			node_list.sort(key = lambda x:node.value,reverse = False)
			weight_add = Node(value = node_list[0].value + node_list[1].value)
			weight_add_left = node_list.pop(0)
			weight_add_right = node_list.pop(0)
			node_list.insert(0,weight_add)
		
		#HuffmanTree's root
		self.root = node_list[0]
		
	def pre_traverse(self,root):
		if root != None:
			print(root.value)
			self.pre_traverse(root.left)
			self.pre_traverse(root.right)
		
	def HuffmanCoding(self,root,length):
		if root != None:
			if root.name != None:
				s = ""
				for i in range(length):
					s += str(self.coding[i])
				print(root.name,"coding:",s)
				return
			else:
				self.coding[length] = 0
				self.HuffmanCoding(root.left,length + 1)
				
				self.coding[length] = 1
				self.HuffmanCoding(root.right,length + 1)
				
if __name__ == "__main__":
	dict = {"a": 9, "b": 12, "c": 6, "d": 3,"e":5, "f": 15}
	Huffmantree = HuffmanTree(dict)
	pre_traverse(Huffmantree.root)
	HuffmanCoding(Huffmantree.root,0)
	
			
