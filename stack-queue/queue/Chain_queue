"""
_*_ coding:utf-8 _*_

@Auther:JeffWb

@data:2018.11.22

@Version:3.6
"""

""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Chain to queue<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
class queueError(ValueError):
	pass
	
class Node:
	def __init__(self,elem = None,next = None):
		self.elem = elem
		self.next = next
		
class CQueue:
	def __init__(self):
		self.first = None
		self.last = None
		
	#empty？
	def is_empty(self):
		return self.first == None
		
	#return first 
	def queue_first(self):
		if self.first == None:
			raise queueError("queue is empty,no first")
		else:
			return self.first.elem
			
	#return last
	def queue_last(self):
		if self.first == None:
			raise queueError("queue is empty,no last")
		else:
			return self.last.elem
			
	#enqueue
	def enqueue(self,elem):
		p = Node(elem)                 #neccessary
		if self.first == None:
			self.first = p
			self.last = p
		else:
			self.last.next = p
			self.last = p
			
	#dequeue
	def dequeue(self):
		if self.first == None:
			raise queueError("queue is empty,dequeue fail")
		else:
			e = self.first.elem
			self.first = self.first.next
			return e
			
	#return length
	def length(self):
		if self.first == None:
			return 0
		else:
			i = 1
			p = self.first
			while p.next != None:
				p = p.next
				i += 1
			return i
	
if __name__ == '__main__':
	cq = CQueue()
	cq.enqueue(1)
	cq.enqueue(2)
	cq.is_empty()
	print(cq.queue.first())
	print(cq.lenght())
	print(cq.dequeue())
	print(cq.queue_last())
