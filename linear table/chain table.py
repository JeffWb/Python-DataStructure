"""
_*_ coding:utf-8 _*_

@Auther:JeffWb

@data:2018.11.22

@Version:3.6
"""
#
#node
class LNode:
	def __init__(self, elem,next_ = None):
		self.elem = elem
		self.next = next_

#error
class LinkedListUnderflow(ValueError):
	pass


#single chain table
class LList():
	#initialize
	def __init__(self,head = None):
		self._head = head                  #head node
		self.num = 1                     #num of node

	#empty or not
	def is_empty(self):
		return self._head is None

	#length
	def len(self):
		return self.num

	""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>loc<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
	#loc
	def located(self,loc):
		if(loc < 1 or loc > self.num):
			raise LinkedListUnderflow("loc fail")
		temp = self._head
		i = 1
		if loc == 1:
			return temp
		else:
			while i < loc:
				i += 1
				temp = temp.next
			return temp
		
	#loc then add elem
	def located_add(self,loc,elem):
		node = LNode(elem)                  #node = LNode(elem)
		if loc == 1:
			node.next = self._head
			self._head = node
		else:
			temp = self.located(loc-1)
			node.next = temp.next
			temp.next = node
		self.num += 1

	#loc and del loc
	def located_del(self,loc):
		if loc == 1:
			self._head = self._head.next
		else:
			temp = self.located(loc-1)
			temp.next = temp.next.next
		self.num -= 1

	""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>add or del<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
	#header add elem
	def prinsert(self,elem):
		self._head = LNode(elem,self._head)
		# node = LNode(elem)
		# node.next = self._head
		# self._head = node
		self.num += 1

	#return header elem and del it 
	def  pre_del(self):
		if self._head is None:
			return LinkedListUnderflow("del header fail")
		e = self._head.elem
		self.head = self._head.next
		self.num -= 1
		return e

	#footer add
	def tail_add(self,elem):
		if self._head is None:
			self._head = LNode(elem)
			self.num += 1
			return
		p = self._head
		while p.next is not None:
			p = p.next
		p.next = LNode(elem)
		self.num += 1

	#return footer elem then del it
	def tail_del(self):
		if self._head is None:
			return LinkedListUnderflow("del footer fail")
		p = self._head
		if p.next is None:
			e = p.elem
			self._head = None
			self.num -= 1
			return e
		while p.next.next is not None:
			p = p.next
		e = p.next.elem
		p.next = None
		self.num -= 1
		return e

	""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>travel<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
	#travel all elem and print
	def  traverse(self):
		if self._head is None:
			return LinkedListUnderflow("chain table is NULL")
		p = self._head
		if p.next is None:
			print(p.elem)
		while p.next is not None:
			print(p.elem)
			p = p.next
		print(p.elem)

	#iter
	def  iterator(self):
		p = self._head
		while p is not None:
			yield p.elem
			p = p.next

	""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>copy<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
	#copy
	def deepCopy(self):
		Co = copy.deepcopy(self)
		return Co

if __name__ == '__main__':
	head = LNode(0)
	l = LList(head)
	l.tail_add(1)
	l.traverse()
	l.located_add(1,2)
	l.traverse()
	l.located_del(3)
	l.traverse()
