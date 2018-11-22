"""
_*_ coding:utf-8 _*_

@Auther:JeffWb

@data:2018.11.22

@Version:3.6
"""

""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Chain to stack<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
class StackUnderFlow(ValueError):
	pass

class Node:
	def __init__(self,elem,next):
		self.elem = elem
		self._next = next
		
class CStack:
	def __init__(self,top = None):
		self.top = top
		
	def is_empty(self):
		return self.top == None
	
	#elem push
	def push(self,elem):
		self.top = Node(elem,self.top)
		
	#stack out and return elem
	def stack_out(self):
		if self.top == None:
			raise StackUnderFlow("stack is empty,stack out fail")
		else:
			e = self.top.elem
			self.top = self.top._next
			return e
	
	#return top elem
	def top(self):
		if self.top == None:
			raise StackUndeFlow("stack is empty,top fail")
		return self.top.elem
		
	#return deepth of stack
	def deepth(self):
		if self.top == None:
			return 0
		else:
			i = 0
			temp = self.top
			while temp != None:
				temp = temp.next
				i += 1
			return i
		
if __name__ == '__main__':
	cs = CStack(Node(1))
	cs.is_empty()
	cs.push(2)
	cs.push(3)
	print(cs.top())
	print(cs.stack_out())
	print(cs.deepth())
	
	
	
	
	
	
	
