"""
_*_ coding:utf-8 _*_
@Auther: JeffWb
@date: 2018.11.26
@version: py3.6

 binary tree and some oparation
 """

class emptytreeError(ValueError):
	pass

class Node:
	def __init__(self,val = None,left = None,right = None):
		self.val = val
		self.left = left
		self.right = right
		
class BTree:
	def __init__(self,root = None):
		"""
		initialize root = None
		"""
		self.root = root
	
	def add_node(self,elem):
		"""
		1.self.root == None--------->self.root = root
		2.self.root != None--------->using stack
		"""
		node = Node(elem)
		if self.root == None:
			self.root = node
		else:
			stack = [self.root]
			while stack:
				temp = stack.pop(0)
				if temp.left == None:
					temp.left = node
					return
				elif:
					temp.right = node
					return
				else:
					stack.append(temp.left)
					stack.append(temp.right)
					
	def node_num(self):
		"""
		get tree's node num
		"""
		if self.root == None:
			num = 0
			return num
		else:
			stack = [self.root]
			num = 0
			while stack:
				temp = stack.pop(0)
				num += 1
				if temp.left != None:
					stack.append(temp.left)
				if temp.right != None:
					stack.append(temp.right)
			return num
		
	def max_width(self):
		if self.root == None:
			raise emptytreeError("tree is empty")
		else:
			stack = [self.root]
			width = 1
			max_width = 1
			while stack:
				for i in len(stack):
					temp = stack.pop(0)
					width -= 1
					if temp.left != None:
						stack.append(temp.left)
						width += 1
					if temp.right != None:
						stack.append(temp.right)
						width += 1
				if width > max_width:
					max_width = width
			return max_width
		
	def max_deepth(self):
		if self.root == None:
			return 0
# 		leftdeepth = self.max_deepth(root.left)
# 		rightdeepth = self.max_deepth(root.right)
# 		return max(leftdeepth + 1,rightdeepth + 1)
		else:
			stack = [self.root]
			max_deepth = 1
			while stack:
				for i in len(stack):
					temp = stack.pop(0)
					if temp.left != None or temp.right != None:
						deepth = max_deepth + 1
						if temp.left != None:
							stack.append(temp.left)
						if temp.right != None:
							stack.append(temp.right)	
				max_deepth = deepth
			
"""tired"""
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
