"""
_*_ coding:utf-8 _*_

@Auther:JeffWb

@data:2018.11.22

@Version:3.6
"""

""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Sequence to queue<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
class queueError(ValueError):
	pass
	
class SQueue:
	def __init__(self):
		self.elem = []
		
	#empty?
	def is_empty(self):
		return self.elem == []
		
	#length of queue
	def length(self):
		return len(self.elem)
	
	#enqueue
	def enqueue(self,elem):
		self.elem.append(elem)
		
	#dequeue
	def dequeue(self):
		if self.elem == []:
			raise queueError("queue is empty,dequeue fail")
		else:
			return self.elem.pop(0)
			
	#queue first
	def queue_first(self):
		if self.elem == []:
			raise queueError("queue is empty,queue first is None")
		else:
			return self.elem[0]
			
	#clear queue
	def clear(self):
		self.elem = []
		
if __name__ == '__main__':
	sq = SQueue()
	sq.enqueue(1)
	sq.enqueue(2)
	sq.is_empty()
	sq.length()
	print(sq.top())
	print(sq.dequeue())
	print(sq.length())
		
