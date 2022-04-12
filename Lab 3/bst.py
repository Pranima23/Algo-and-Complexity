from platform import node


class BinarySearchTree:

	class _BSTNode:
		def __init__(self, key, value):
			self.key = key
			self.value = value
			self.left = None
			self.right = None
			self.parent = None

	def __init__(self):
		self._size = 0
		self._root = None
	
	def size(self):
		return self._size		

	def add(self, key, value):
		z = self._BSTNode(key, value) 
		y = None 
		x = self._root
		while x is not None:  
			y = x			  
			if z.key < x.key:
				x = x.left	  
			else:			 
				x = x.right	 
		z.parent = y
		if y is None:
			self._root = z	 
		elif z.key < y.key:	 
			y.left = z
		else:
			y.right = z		 
		self._size += 1

	def search(self, k):
		x = self._root
		while x is not None and k != x.key:
			if k < x.key:
				x = x.left
			else:
				x = x.right
		if x is not None:
			return x.value
		return False					

	def smallest(self):		
		x = self._root
		while x.left is not None:
			x = x.left
		return (x.key, x.value)	

	def largest(self):
		x = self._root
		while x.right is not None:
			x = x.right
		return (x.key, x.value)

	def _tree_min_node(self, x):
		while x.left is not None:
			x = x.left
		return x
	
	def _transplant(self, nodeToDelete, nodeToReplace):
		if nodeToDelete.parent is None:
			self._root = nodeToReplace
		elif nodeToDelete == nodeToDelete.parent.left:
			nodeToDelete.parent.left = nodeToReplace
		else:
			nodeToDelete.parent.right = nodeToReplace
		if nodeToReplace is not None:
			nodeToReplace.parent = nodeToDelete.parent	

	def _remove(self, x, k):
		if x.key == k:
			if x.left is None:
				self._transplant(x, x.right)
			elif x.right is None:
				self._transplant(x, x.left)
			else:
				nodeToReplace = self._tree_min_node(x.right)
				if nodeToReplace.parent != x:
					self._transplant(nodeToReplace, nodeToReplace.right)
					nodeToReplace.right = x.right
					nodeToReplace.right.parent = nodeToReplace
				self._transplant(x, nodeToReplace)
				nodeToReplace.left = x.left
				nodeToReplace.left.parent = nodeToReplace
			self._size -= 1
		elif k < x.key:
			return self._remove(x.left, k)
		else:
			return self._remove(x.right, k)

	def remove(self, k):
		return self._remove(self._root, k)

	def _inorder_walk(self, x, inorderList):				
		if x:
			self._inorder_walk(x.left, inorderList)
			inorderList.append(x.key)
			self._inorder_walk(x.right, inorderList)
			return inorderList

	def inorder_walk(self):		
		return self._inorder_walk(self._root, inorderList=[])

	def _preorder_walk(self, x, preorderList):
		if x:
			preorderList.append(x.key)
			self._preorder_walk(x.left, preorderList)
			self._preorder_walk(x.right, preorderList)
			return preorderList

	def preorder_walk(self):
		return self._preorder_walk(self._root, preorderList=[])

	def _postorder_walk(self, x, postorderList):
		if x:			
			self._postorder_walk(x.left, postorderList)
			self._postorder_walk(x.right, postorderList)
			postorderList.append(x.key)
			return postorderList

	def postorder_walk(self):
		return self._postorder_walk(self._root, postorderList=[])