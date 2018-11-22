"""
_*_ coding:utf-8 _*_

@Auther:JeffWb

@data:2018.11.22

@Version:3.6
"""

class StackUnderFlow(ValueError):
	pass
	
""">>>>>>>>>>>>>>>>>>>>>>>>>>sequence to stack<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
class SStack:
	def __init__(self):
		self._elem = []
		
	def is_empty(self):
		return self._elem == []
		
	def push(self,elem):
		self._elem.append(elem)
	
	#stack out and return top elem
	def stack_out(self):
		if self._elem == []:
			raise StackUnderFlow("stack is empty,stack out fail")
		return self._elem.pop()
	
	#return top elem
	def top(self):
		if self._elem == []:
			raise StackUnderFlow("stack is empty,top fail")
		return self._elem[-1]
		
	#return deepth of stack
	def deepth(self):
		return len(self._elem)

if __name__=='__main__':
	ss = SStack()
	ss.is_empty()
	ss.push(1)
	ss.push(2)
	print(ss.deepth())
	print(ss.stack_out())
	print(ss.top())	
