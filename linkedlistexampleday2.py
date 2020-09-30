class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __repr__(self):
		return f'Node({repr(self.value)})'

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_head(self, node):
		node.next = self.head
		self.head = node

	def find(self, value):
		cur = self.head

		while cur is not None:
			if cur.value == value:
				return cur

			cur = cur.next

		# If we get here, it's not in the list
		return None
		
	def delete(self, value):

		# Special case of empty list

		if self.head is None:
			return None

		# Special case of deleting the head of the list

		if self.head.value == value:
			old_head = self.head
			self.head = self.head.next
			old_head.next = None
			return old_head

		# General case

		prev = self.head
		cur = self.head.next

		while cur is not None:
			if cur.value == value:
				prev.next = cur.next
				cur.next = None
				return cur

			prev = prev.next
			cur = cur.next

		# If we get here, we didn't find it
		return None
			


	def __str__(self):
		r = ""

		# Traverse the list
		cur = self.head

		while cur is not None:
			r += f'{cur.value}'

			if cur.next is not None:
				r += ' -> '

			cur = cur.next
		
		return r


ll = LinkedList()

ll.insert_at_head(Node(10))
ll.insert_at_head(Node(20))
ll.insert_at_head(Node(30))
ll.insert_at_head(Node(40))
ll.insert_at_head(Node(50))
ll.insert_at_head(Node(60))

print(ll)

#print(ll.find(30))
#print(ll.find(9999999))

ll.delete(60)

print(ll)